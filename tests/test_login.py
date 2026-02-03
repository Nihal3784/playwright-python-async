import allure
import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()


@allure.title("Login Test - Positive and Negative Scenarios")
@pytest.mark.parametrize(
    "username, password, expected_result, scenario",
    [
        ("testingdevice2123@gmail.com", "123456", "success",
         "Valid username and valid password"),

        ("invalid@email.com", "123456", "failure",
         "Invalid username and valid password"),

        ("testingdevice2123@gmail.com", "wrongpass", "failure",
         "Valid username and invalid password"),

        ("", "", "failure",
         "Blank username and blank password"),
    ]
)
@pytest.mark.asyncio
async def test_login_scenarios(page, username, password, expected_result, scenario):
    login = LoginPage(page)

    await login.open()
    await login.login(username, password)

    if expected_result == "success":
        await login.verify_login_success()
        logger.info(f"Login successful – {scenario}")

    elif expected_result == "failure":
        await login.verify_login_failure()
        logger.info(f"Login failed as expected – {scenario}")

    else:
        pytest.fail(f"Invalid expected_result value: {expected_result}")
