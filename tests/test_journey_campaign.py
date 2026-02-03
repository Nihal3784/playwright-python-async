import pytest
import allure
from screenshots.screenshot import take_screenshot
from pages.Login import LoginPage
from utils.logger import get_logger
from pages.dashboard_page import DashboardPage
from pages.journey_campaign_page import JourneyCampaignPage
from utils.helpers import random_campaign_name


@allure.feature("Journey Campaign")
@allure.story("Create and Delete Journey Campaign")
@pytest.mark.asyncio
async def test_create_and_delete_journey_campaign(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    journey = JourneyCampaignPage(page)
    logger = get_logger()

    campaign_name = random_campaign_name()

    await login.login()
    await dashboard.open_campaign_manager()

    await journey.create_journey_campaign(campaign_name)
    logger.info(f"Journey campaign template is: {campaign_name} created")

    await journey.delete_journey_campaign(campaign_name)
    logger.info(f"Journey campaign template is successfully deleted")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")
