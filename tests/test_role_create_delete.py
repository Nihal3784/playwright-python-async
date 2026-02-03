import allure
import pytest
from pages.Login import LoginPage
from screenshots.screenshot import take_screenshot
from pages.dashboard_page import DashboardPage
from pages.role_page import RolePage
from utils.helpers import generate_role_name
from utils.logger import get_logger


@pytest.mark.asyncio
@allure.feature("User Management")
@allure.story("Create and Delete Role")
async def test_create_and_delete_role(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    role = RolePage(page)
    logger = get_logger()

    role_name = generate_role_name("role")

    await login.login()

    await dashboard.open_user_management()

    # CREATE
    await role.create_role(role_name)
    await role.verify_created(role_name)
    logger.info(f"Created Role: {role_name}")

    # DELETE (only recently created role)
    await role.delete_role(role_name)
    await role.verify_deleted()
    logger.info(f"Role is successfully deleted")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")



