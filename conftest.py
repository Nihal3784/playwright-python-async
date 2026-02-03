import os
import pytest
import pytest_asyncio
from datetime import datetime
from playwright.async_api import async_playwright
import allure
from utils.logger import get_logger

logger = get_logger()

ARTIFACT_DIRS = ["screenshots", "videos", "traces"]
for d in ARTIFACT_DIRS:
    os.makedirs(d, exist_ok=True)


@pytest_asyncio.fixture
async def page(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="videos/"
        )

        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = await context.new_page()
        yield page

        rep_call = getattr(request.node, "rep_call", None)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if rep_call and rep_call.failed:
            screenshot = f"screenshots/{request.node.name}_{timestamp}.png"
            trace = f"traces/{request.node.name}_{timestamp}.zip"

            await page.screenshot(path=screenshot, full_page=True)
            await context.tracing.stop(path=trace)

            allure.attach.file(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach.file(
                trace,
                name="Playwright Trace",
                attachment_type=allure.attachment_type.ZIP
            )

            logger.error("Test Failed")
            logger.error(f"Screenshot: {screenshot}")
            logger.error(f"Trace: {trace}")

        else:
            await context.tracing.stop()

        await context.close()
        await browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
