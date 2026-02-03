import pytest
import allure
from playwright.async_api import async_playwright
from pages.Login import LoginPage
from pages.audience_page import AudiencePage
from screenshots.screenshot import take_screenshot
from utils.logger import get_logger
from utils.data_generate import generate_random_lead_data


@pytest.mark.asyncio
@allure.feature("Create Lead")
@allure.story("Create lead, update and delete")
async def test_create_update_delete_lead():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Login
        login = LoginPage(page)
        await login.login()

        # Audience actions
        audience = AudiencePage(page)
        await audience.navigate_to_audience()
        logger = get_logger()

        data = generate_random_lead_data()
        logger.info(f"Generated lead data: {data}")

        await audience.add_lead(data["name"], data["email"], data["mobile"])
        await audience.update_lead(data["text"])
        await audience.delete_lead()

        await context.close()
        await browser.close()
