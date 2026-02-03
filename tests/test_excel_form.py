import pytest
import allure
from pages.Login import LoginPage
from screenshots.screenshot import take_screenshot
from pages.dashboard_page import DashboardPage
from pages.excel_form_page import ExcelFormPage
from utils.helpers import random_excel_name
from utils.logger import get_logger


@pytest.mark.asyncio
@allure.title("Add and Delete Excel Form")
@allure.feature("Excel Form")
@allure.story("Create and Delete Excel Form")
async def test_add_delete_excel_form(page):

    excel_name = random_excel_name()
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    excel = ExcelFormPage(page)
    logger = get_logger()

    await login.login()

    await dashboard.navigate_to_excel_upload()

    await excel.add_form(excel_name)
    logger.info(f"Created Role: {excel_name}")
    await excel.delete_form(excel_name)
    logger.info(f"Excel form is successfully removed")
    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")

