import re
from playwright.async_api import expect


class ProductPage:

    def __init__(self, page):
        self.page = page

    async def open_add_product_dialog(self):
        await self.page.get_by_role("button", name="Add").click()
        await expect(
            self.page.get_by_role("heading", name="Add Item")
        ).to_be_visible()

    async def add_product(self, name, description, rate, hsn):
        product_block = self.page.locator(
            "div", has_text=re.compile(r"^Product NameProduct Description$")
        )

        await product_block.get_by_role("textbox").first.fill(name)
        await product_block.get_by_role("textbox").nth(1).fill(description)

        rate_block = self.page.locator(
            "div", has_text=re.compile(r"^RateHSN$")
        )

        await rate_block.get_by_role("textbox").first.fill(rate)
        await rate_block.get_by_role("textbox").nth(1).fill(hsn)

        await self.page.get_by_role("dialog").get_by_role(
            "combobox"
        ).select_option("2")

        await self.page.get_by_role("button", name="Submit").click()

        # Toast handling
        await self.page.locator(
            "div", has_text="Product Added"
        ).nth(2).click()

    async def delete_product(self, product_name):
        await self.page.get_by_role(
            "cell", name=product_name
        ).click()

        await self.page.get_by_title(
            "Delete Record"
        ).first.click()

        await expect(
            self.page.get_by_role(
                "heading", name="Are you sure want to remove"
            )
        ).to_be_visible()

        await self.page.get_by_role("button", name="Yes").click()

        await self.page.locator(
            "div", has_text="Item removed"
        ).nth(2).click()
