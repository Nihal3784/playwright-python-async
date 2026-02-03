import pytest
import allure
from pages.Login import LoginPage
from pages.dashboard_page import DashboardPage
from screenshots.screenshot import take_screenshot
from pages.campaign_template_page import CampaignTemplatePage
from utils.helpers import generate_template_name
from utils.logger import get_logger


@allure.feature("Campaign Template")
@allure.story("Create and Delete Campaign Template")
@pytest.mark.asyncio
async def test_create_and_delete_campaign_template(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    template = CampaignTemplatePage(page)
    logger = get_logger()

    template_name = generate_template_name("template")
    heading_name = generate_template_name("heading")

    await login.login()
    await dashboard.go_to_campaign_template()

    await template.create_template(template_name, heading_name)
    logger.info(f"Created Role: {template_name,heading_name}")

    await template.delete_template(template_name)
    logger.info(f"Template is successfully deleted")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")

