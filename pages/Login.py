from playwright.async_api import Page, expect
from config.settings import BASE_URL, USERNAME, PASSWORD


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def login(self):
        await self.page.goto(BASE_URL)
        await expect(self.page.get_by_role("heading", name="Cronberry")).to_be_visible()

        await self.page.get_by_role("textbox", name="Email id").fill(USERNAME)
        await self.page.get_by_role("textbox", name="Password").fill(PASSWORD)
        await self.page.get_by_role("button", name="Sign in").click()

        await expect(self.page.get_by_role("link", name="Dashboard")).to_be_visible()
