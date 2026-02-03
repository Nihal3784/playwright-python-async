import pytest
from playwright.async_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.email = page.get_by_role("textbox", name="Email id")
        self.password = page.get_by_role("textbox", name="Password")
        self.sign_in = page.get_by_role("button", name="Sign in")

    async def open(self):
        await self.page.goto("https://cloud.cronberry.com/admin/sign-in")

    async def login(self, email, password):
        await self.email.fill(email)
        await self.password.fill(password)
        await self.sign_in.click()

    @pytest.mark.asyncio
    async def verify_login_success(self):
        await expect(
            self.page.get_by_role("link", name="Dashboard")
        ).to_be_visible()

        await expect(
            self.page.get_by_text("Invalid")
        ).not_to_be_visible()

    async def verify_login_failure(self):
        await expect(
            self.page.get_by_text("Invalid")
        ).to_be_visible()

        await expect(
            self.page.get_by_role("link", name="Dashboard")
        ).not_to_be_visible()

