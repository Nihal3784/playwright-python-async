import re
from playwright.async_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page

    async def wait_for_overlay_to_clear(self):
        overlay = self.page.locator("div.overlay-container")

        # Wait until overlay either disappears OR stops blocking clicks
        if await overlay.is_visible():
            await self.page.wait_for_function(
                """() => {
                    const overlay = document.querySelector('div.overlay-container');
                    if (!overlay) return true;
                    return getComputedStyle(overlay).pointerEvents === 'none';
                }"""
            )

    async def neutralize_toast_pointer_events(self):
        await self.page.add_style_tag(
            content="""
            .ngx-toastr,
            .overlay-container {
                pointer-events: none !important;
            }
            """
        )

    async def sign_out(self):
        # neutralize toast interference (test-only)
        await self.neutralize_toast_pointer_events()

        # open user dropdown
        await self.page.get_by_role(
            "link", name=re.compile(r"^[A-Z]{1,2}$")
        ).click()

        # wait for menu
        await expect(
            self.page.get_by_role("menuitem", name="Edit Account")
        ).to_be_visible()

        # sign out
        await self.page.get_by_text("Sign Out").click()

    async def open_email_campaign(self):
        await self.page.get_by_role("link", name="Email Campaign").click()
        await expect(
            self.page.get_by_role("heading", name="Email Campaign")
        ).to_be_visible()

    async def open_whatsapp_campaign(self):
        await self.page.get_by_role(
            "link", name="Whatsapp Campaign"
        ).click()

        await expect(
            self.page.get_by_role("heading", name="Whatsapp Campaign")
        ).to_be_visible()

    async def navigate_to_lead_status(self):
        await self.page.locator("a").filter(has_text="Leads").click()
        await self.page.get_by_role("link", name="Audience").click()

        await self.page.locator("#manageLeadsButton").nth(1).click()
        await self.page.get_by_role(
            "link", name="Update Lead Status"
        ).click()

    async def open_user_management(self):
        await self.page.get_by_role("link", name="User Management").click()

    async def go_to_campaign_template(self):
        await self.page.locator("a").filter(has_text=re.compile(r"^Campaign$")).click()
        await self.page.get_by_role("link", name="Campaign Template").click()

    async def open_campaign_manager(self):
        await self.page.locator(
            "//aside[contains(@class,'sidebar')]//a[.//span[normalize-space()='Campaign']]"
        ).click()
        await self.page.get_by_role("link", name="Campaign Manager").click()

    async def navigate_to_excel_upload(self):
        await self.page.locator("a", has_text="Project Integration").click()
        await self.page.locator("a", has_text="Bulk").click()
        await self.page.get_by_role("link", name="Excel Upload").click()

    async def wait_for_toast_to_disappear(self):
        pass

    async def go_to_product_page(self):
        await self.page.locator(
            "a", has_text="Invoice & Quotations"
        ).click()

        await self.page.get_by_role(
            "link", name="Product"
        ).click()

