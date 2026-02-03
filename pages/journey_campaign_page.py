import re
from playwright.async_api import expect


class JourneyCampaignPage:
    def __init__(self, page):
        self.page = page

    async def create_journey_campaign(self, campaign_name: str):
        create_heading = self.page.get_by_role(
            "heading", name="Create Campaign"
        )

        await expect(create_heading).to_be_visible()

        # Scope Select link within Create Campaign section
        create_section = create_heading.locator("..")

        await create_section.get_by_role(
            "link", name="Select"
        ).click()
        await expect(
            self.page.get_by_role("button", name="Add Item")
        ).to_be_visible()

        await self.page.locator(
            'input[name="journeyCampaignName"]'
        ).fill(campaign_name)

        # Email step
        await self.page.get_by_role("button", name="Add Item").click()
        await self.page.get_by_role("button", name="email").click()
        await self.page.get_by_text("Merry_Christmas").click()
        await self.page.get_by_role("button", name="Submit").click()
        await self.page.get_by_role("button", name="Select Frequency").click()
        await self.page.get_by_role("button", name="Submit").click()

        # WhatsApp step
        await self.page.get_by_role("button", name="Add Item").click()
        await self.page.get_by_role("button", name="whatsapp").nth(1).click()
        await self.page.get_by_text("chat_initiate").click()
        await self.page.get_by_role("button", name="Submit").click()

        await self.page.get_by_role("button", name="Select Frequency").click()
        await self.page.get_by_role("dialog").get_by_role("textbox").fill("5")
        await self.page.get_by_role("button", name="Submit").click()

        await expect(
            self.page.get_by_role("button", name="Wait 9 minutes,")
        ).to_be_visible()

        await self.page.get_by_role("button", name="Save").click()

        #Toast handled safely (non-strict)
        await expect(
            self.page.locator("div.toast-message", has_text="Success")
        ).to_be_visible()

        await self.page.get_by_text("Success Success").click()

    async def delete_journey_campaign(self, campaign_name: str):
        # Find heading using regex (ignore suffix like Cronberry Automation)
        campaign_heading = self.page.get_by_role(
            "heading",
            name=re.compile(rf"^{re.escape(campaign_name)}\b")
        )

        await expect(campaign_heading).to_be_visible()

        # Move to campaign container/card
        campaign_card = campaign_heading.locator("..").locator("..")

        # Find delete button INSIDE this campaign card
        # (icon-only button → no accessible name)
        delete_button = campaign_card.locator(
            "button.btn-outline-danger"
        ).first

        await expect(delete_button).to_be_visible()
        await delete_button.click()

        # Confirm delete modal
        await expect(
            self.page.get_by_role("heading", name="Delete Campaign")
        ).to_be_visible()

        await self.page.get_by_role("button", name="Yes").click()

        # Success toast (safe non-strict)
        await expect(
            self.page.locator("div.toast-message", has_text="Success")
        ).to_be_visible()