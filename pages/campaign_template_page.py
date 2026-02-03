import re
from playwright.async_api import expect


class CampaignTemplatePage:
    def __init__(self, page):
        self.page = page

    async def create_template(self, name, heading):
        await self.page.get_by_role("button", name="Add").click()
        await self.page.get_by_role("textbox").nth(1).fill(name)
        await self.page.get_by_role("textbox").nth(2).fill(heading)

        await expect(
            self.page.get_by_role("heading", name=heading)
        ).to_be_visible()

        await self.page.get_by_role("listbox").locator("div").nth(1).click()
        await self.page.get_by_role("combobox").fill("name")
        await self.page.get_by_role("option", name="Name", exact=True).click()
        await self.page.get_by_role("button", name="Save").click()

        await expect(
            self.page.locator("div.toast-message", has_text="Template Created")
        ).to_be_visible()

    async def delete_template(self, template_name):
        row = self.page.get_by_role("row", name=template_name)
        await expect(row).to_be_visible()

        await row.locator("a").nth(1).click()
        await expect(
            self.page.get_by_role("heading", name="Delete Template")
        ).to_be_visible()

        await self.page.get_by_role("button", name="Yes").click()

        await expect(
            self.page.locator("div.toast-message", has_text="Template Deleted Successfully")
        ).to_be_visible()
