import pytest
import allure
from screenshots.screenshot import take_screenshot
from pages.Login import LoginPage
from pages.dashboard_page import DashboardPage
from pages.lead_status_page import LeadStatusPage
from utils.helpers import generate_lead_status_name
from utils.logger import get_logger


@pytest.mark.asyncio
@allure.feature("Create/update lead status ")
@allure.story("This test cases describe how to create and update the lead status")
async def test_create_and_update_lead_status(page):
    logger = get_logger()

    create_name = generate_lead_status_name("create")
    update_name = generate_lead_status_name("update")

    logger.info(f"Creating lead status: {create_name}")
    logger.info(f"Updating lead status to: {update_name}")

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    lead_status = LeadStatusPage(page)

    await login.login()

    await dashboard.navigate_to_lead_status()

    # CREATE
    await lead_status.add_lead_status(create_name)
    await lead_status.verify_created(create_name)

    # UPDATE
    await lead_status.update_lead_status(create_name, update_name)
    await lead_status.verify_updated(update_name)

    # DELETE
    logger.info(f"Deleting lead status: {update_name}")
    await lead_status.delete_lead_status(update_name)
    await lead_status.verify_deleted()

    logger.info("Create → Update → Delete lead status flow completed")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")
