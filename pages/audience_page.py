from playwright.async_api import Page, expect


class AudiencePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate_to_audience(self):
        await self.page.locator("a", has_text="Leads").click()
        await self.page.get_by_role("link", name="Audience").click()
        await expect(self.page.get_by_role("heading", name="Audience")).to_be_visible()

    async def add_lead(self, name, email, mobile):
        await self.page.get_by_role("button", name="Add").click()
        await self.page.get_by_role("link", name="API").click()
        await expect(self.page.get_by_role("row", name="Parameter Value").first).to_be_visible()

        await self.page.get_by_role("textbox", name="Name", exact=True).fill(name)
        await self.page.get_by_role("textbox", name="Phone", exact=True).fill(mobile)
        await self.page.get_by_role("textbox", name="Email", exact=True).fill(email)

        await self.page.get_by_role("button", name="Submit").click()
        await expect(self.page.get_by_role("row", name="S.No. Name Email Mobile Lead")).to_be_visible()

    async def update_lead(self, comment):
        await self.page.get_by_role("row").nth(1).locator("a").nth(2).click()
        await expect(self.page.get_by_role("row", name="Mobile:")).to_be_visible()

        await self.page.get_by_role("combobox").click()
        await self.page.get_by_role("option", name="One").click()
        await self.page.get_by_role("button", name="Save Attribute").click()

        await self.page.get_by_role("radio", name="Converted").check()
        await self.page.locator("textarea").fill(comment)
        await self.page.get_by_role("button", name="Submit").click()

    async def delete_lead(self):
        await self.page.get_by_role("row").nth(1).locator("a").nth(3).click()
        await expect(self.page.get_by_role("heading", name="Delete Audience")).to_be_visible()

        await self.page.get_by_role("button", name="Yes", exact=True).click()
        await expect(self.page.get_by_text("Success Success")).to_be_visible()
