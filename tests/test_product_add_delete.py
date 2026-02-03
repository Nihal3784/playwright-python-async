import pytest
import allure
from pages.Login import LoginPage
from screenshots.screenshot import take_screenshot
from pages.dashboard_page import DashboardPage
from pages.product_page import ProductPage
from utils.logger import get_logger
from utils.helpers import (random_text, random_rate, random_hsn)


@pytest.mark.asyncio
@allure.title("Add and Delete Product")
@allure.feature("Invoice and quotation product")
@allure.story("Create and Delete Product")
async def test_add_and_delete_product(page):
    product_name = random_text("product")
    description = random_text("desc")
    rate = random_rate()
    hsn = random_hsn()
    logger = get_logger()

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    product = ProductPage(page)

    await login.login()

    await dashboard.go_to_product_page()

    await product.open_add_product_dialog()
    await product.add_product(product_name, description, rate, hsn)
    logger.info(f"Created Role: {product_name}")
    await product.delete_product(product_name)
    logger.info(f"Product is successfully deleted: {product_name}")

    await dashboard.sign_out()
    logger.info(f"Your account is successfully sign out")
