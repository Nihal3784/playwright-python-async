import re
from playwright.async_api import expect


class RolePage:
    def __init__(self, page):
        self.page = page

    def _row_by_name(self, name):
        return self.page.get_by_role("row", name=re.compile(fr"^{name}\b"))

    async def create_role(self, role_name):
        await self.page.get_by_role("button", name="Add").click()
        await expect(
            self.page.get_by_role("heading", name="Add Role")
        ).to_be_visible()

        await self.page.get_by_role("dialog").get_by_role("textbox").fill(role_name)

        await self.page.locator(
            "div", has_text=re.compile(r"^TypeSelect")
        ).get_by_role("combobox").select_option("1")

        await self.page.locator(
            "div", has_text=re.compile(r"^Select Role$")
        ).nth(1).click()

        await self.page.get_by_role("option", name="Admin").click()
        await self.page.get_by_role("button", name="Save").click()

    async def verify_created(self, role_name):
        await expect(
            self.page.get_by_role("cell", name=role_name)
        ).to_be_visible()
        await expect(
            self.page.get_by_role("alertdialog", name="Success", exact=True)
        ).to_be_visible()

    async def delete_role(self, role_name: str):
        # 1️⃣ Find role name cell
        name_cell = self.page.get_by_role("cell", name=role_name)
        await expect(name_cell).to_be_visible()

        # 2️⃣ Select row (Cronberry requirement)
        await name_cell.click()

        # 3️⃣ Go to the row
        row = name_cell.locator("..")

        # 4️⃣ Click Delete action
        delete_btn = (
            row
            .get_by_role("cell")
            .locator("a")
            .nth(1)
        )

        await delete_btn.click()

        # 5️⃣ Confirm
        await self.page.get_by_role("button", name="Yes").click()

    async def verify_deleted(self):
        await expect(
            self.page.get_by_role("alertdialog", name="Success", exact=True)
        ).to_be_visible()
        await self.page.get_by_text("Success Success").click()
