import re
from playwright.async_api import expect


class LeadStatusPage:
    def __init__(self, page):
        self.page = page

    # ------------------------------------------------------------------
    # COMMON LOCATORS
    # ------------------------------------------------------------------

    def _name_input(self):
        return (
            self.page.locator("div")
            .filter(has_text=re.compile(r"^Name$"))
            .get_by_role("textbox")
        )

    def _row_by_name(self, name):
        """
        Returns the table row that contains the given lead status name
        """
        return self.page.get_by_role("cell", name=name).locator("..")

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------

    async def add_lead_status(self, name: str):
        await self.page.get_by_role("button", name="Add").click()

        await self._name_input().fill(name)

        await (
            self.page.locator("div")
            .filter(has_text=re.compile(r"^OrderSelect"))
            .get_by_role("combobox")
            .select_option("8")
        )

        await (
            self.page.locator("div")
            .filter(has_text=re.compile(r"^Color CodeSelect"))
            .get_by_role("combobox")
            .select_option("#008080")
        )

        await self.page.get_by_role("radio", name="Default").check()
        await self.page.get_by_role("button", name="Save").click()

        await expect(
            self.page.get_by_role(
                "heading", name="Are you sure want to update ?"
            )
        ).to_be_visible()

        await self.page.get_by_role("button", name="Yes").click()

    async def verify_created(self, name: str):
        await expect(
            self.page.get_by_role("cell", name=name)
        ).to_be_visible()

        await expect(
            self.page.get_by_role(
                "alertdialog",
                name="Success",
                exact=True
            )
        ).to_be_visible(timeout=600)

    # ------------------------------------------------------------------
    # UPDATE (BASED ON CREATED NAME)
    # ------------------------------------------------------------------

    async def open_edit(self, name: str):
        # Anchor on name cell (stable)
        name_cell = self.page.get_by_role("cell", name=name)
        await expect(name_cell).to_be_visible()

        # Select row (Cronberry requirement)
        await name_cell.click()

        # Move to row
        row = name_cell.locator("..")

        # Click Edit safely
        edit_btn = (
            row
            .get_by_role("cell")
            .locator("a")
            .first
        )

        await expect(edit_btn).to_be_enabled()
        await edit_btn.click()

    async def update_lead_status(self, old_name: str, new_name: str):
        await self.open_edit(old_name)

        name_input = self._name_input()
        await name_input.fill("")
        await name_input.fill(new_name)

        await self.page.get_by_role("radio", name="Yes").check()
        await self.page.get_by_role("button", name="Update").click()

        await expect(
            self.page.get_by_role(
                "heading", name="Are you sure want to update ?"
            )
        ).to_be_visible()

        await self.page.get_by_role("button", name="Yes").click()

    async def verify_updated(self, name: str):
        row = self._row_by_name(name)
        await expect(row).to_be_visible()

        await expect(
            self.page.get_by_role("alertdialog").filter(has_text="Success")

        ).to_be_visible()

    # ------------------------------------------------------------------
    # DELETE (BASED ON UPDATED NAME)
    # ------------------------------------------------------------------

    async def delete_lead_status(self, name: str):
        # Anchor on name cell (stable)
        name_cell = self.page.get_by_role("cell", name=name)
        await expect(name_cell).to_be_visible()

        # Select row
        await name_cell.click()

        # Move to row
        row = name_cell.locator("..")

        # Click Delete safely
        delete_btn = (
            row
            .get_by_role("cell")
            .locator("a")
            .nth(1)
        )

        await expect(delete_btn).to_be_enabled()
        await delete_btn.click()

        # 5️⃣ Confirm delete
        await self.page.get_by_role("button", name="Yes").click()

    async def verify_deleted(self):
        await expect(
            self.page.get_by_role(
                "alertdialog",
                name="Success",
                exact=True
            )
        ).to_be_visible(timeout=500)
