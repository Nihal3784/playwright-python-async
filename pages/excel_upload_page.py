from playwright.async_api import expect


class ExcelUploadPage:

    def __init__(self, page):
        self.page = page

    async def open_cloud_form(self):
        await self.page.get_by_role(
            "link", name="[object Object] Cloud"
        ).click()

        await expect(
            self.page.get_by_role("heading", name="Cloud")
        ).to_be_visible()

    async def upload_excel_file(self, file_path: str):
        await self.page.get_by_text("Upload", exact=True).click()

        await expect(
            self.page.get_by_role("heading", name="Bulk Upload")
        ).to_be_visible()

        await self.page.get_by_role(
            "button", name="Choose File"
        ).set_input_files(file_path)

        await self.page.get_by_role(
            "button", name="Save"
        ).click()

    async def verify_upload_success(self):
        await expect(
            self.page.get_by_role(
                "alertdialog",
                name="File Uploaded Successfully"
            )
        ).to_be_visible()

        await self.page.locator(
            "div", has_text="File Uploaded Successfully"
        ).nth(2).click()
