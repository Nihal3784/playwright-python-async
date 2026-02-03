from playwright.async_api import expect


class WhatsappCampaignPage:
    def __init__(self, page):
        self.page = page

    async def create_campaign(self, campaign_name):
        await self.page.locator(
            "input[name='campaignName']"
        ).fill(campaign_name)

        await self.page.get_by_role(
            "button", name="Select Segments"
        ).click()

        await expect(
            self.page.get_by_role(
                "row", name="Nihals Info Audience SEG-5412"
            )
        ).to_be_visible()

        await self.page.get_by_role(
            "row", name="Nihals Info Audience SEG-5412"
        ).locator("span").click()

        await self.page.get_by_role(
            "button", name="Calculate Audience"
        ).click()

        await expect(
            self.page.get_by_role(
                "alertdialog", name="User(s) Found"
            )
        ).to_be_visible()

        await self.page.get_by_role(
            "button", name="Proceed"
        ).click()

        await self.page.locator("select").select_option("4928")

        await self.page.get_by_role(
            "button", name="Send", exact=True
        ).click()

    async def verify_campaign_created_toast(self):
        await self.page.locator("div").filter(
            has_text="Campaign Created"
        ).nth(2).click()

    async def assert_campaign_name(self, campaign_name):
        await expect(
            self.page.get_by_role("cell", name=campaign_name)
        ).to_be_visible()
