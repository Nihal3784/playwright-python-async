import pytest
import allure
from screenshots.screenshot import take_screenshot
from pages.Login import LoginPage
from pages.dashboard_page import DashboardPage
from pages.whatsapp_campaign_page import WhatsappCampaignPage
from utils.helpers import generate_campaign_name
from utils.logger import get_logger


@pytest.mark.asyncio
@allure.feature("Create whatsapp Campaign")
@allure.story("Execute whatsapp campaign based on segment audience and verify it is execute properly or not")
async def test_create_whatsapp_campaign(page):
    logger = get_logger()
    campaign_name = generate_campaign_name()

    logger.info(f"Creating WhatsApp campaign: {campaign_name}")

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    campaign = WhatsappCampaignPage(page)

    await login.login()

    await dashboard.open_whatsapp_campaign()

    await campaign.create_campaign(campaign_name)
    await campaign.verify_campaign_created_toast()
    await campaign.assert_campaign_name(campaign_name)

    logger.info("WhatsApp campaign created successfully")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")
