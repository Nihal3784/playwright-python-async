import pytest
import allure
from pages.Login import LoginPage
from screenshots.screenshot import take_screenshot
from pages.dashboard_page import DashboardPage
from pages.excel_upload_page import ExcelUploadPage
from utils.logger import get_logger


@allure.title("Excel File Upload – Success Flow")
@pytest.mark.asyncio
@allure.feature("Upload Excel")
@allure.story("Uploading excel file")
async def test_excel_file_upload(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    excel = ExcelUploadPage(page)
    logger = get_logger()

    await login.login()

    await dashboard.navigate_to_excel_upload()

    await excel.open_cloud_form()
    await excel.upload_excel_file("automation_excel_data.xlsx")
    await excel.verify_upload_success()
    logger.info(f"Excel form is successfully uploaded")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")



