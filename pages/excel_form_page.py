from playwright.async_api import expect


class ExcelFormPage:

    def __init__(self, page):
        self.page = page

    async def add_form(self, excel_name):
        await self.page.get_by_role("link", name="Add Add Form").click()
        await self.page.locator('input[name="excelAlias"]').fill(excel_name)
        await self.page.get_by_role("button", name="Save").click()

        await expect(
            self.page.get_by_role("link", name=f"[object Object] {excel_name}")
        ).to_be_visible()

        await self.page.locator("div", has_text="Form added successfully").nth(2).click()

    async def delete_form(self, excel_name):
        await self.page.get_by_role(
            "link", name=f"[object Object] {excel_name}"
        ).click()

        await self.page.get_by_role("heading", name=excel_name).click()
        await self.page.get_by_role("button", name="Delete").click()

        await expect(
            self.page.get_by_role(
                "heading", name="Are you sure want to delete ?"
            )
        ).to_be_visible()

        await self.page.get_by_role("button", name="Yes").click()

        await expect(
            self.page.get_by_role(
                "alertdialog", name="Form removed successfully"
            )
        ).to_be_visible()

        await self.page.locator(
            "div", has_text="Form removed successfully"
        ).nth(2).click()
