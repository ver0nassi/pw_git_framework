from framework.pages.base_page import BasePage
from framework.components.header.guest_header import GuestHeaderComponent
from framework.components.footer.guest_footer import GuestFooterComponent
from playwright.sync_api import Page, expect


class GuestPage(BasePage):
    PAGE_PATH: str = "/"
    def __init__(self, page: Page):
        super().__init__(page)

        # --- Common Global Components ---
        self.header : GuestHeaderComponent = GuestHeaderComponent(page)
        self.footer : GuestFooterComponent = GuestFooterComponent(page)

        # --- Top banner items ---
        self.hero_heading = page.get_by_role("heading", name="The future of building happens together")
        self.hero_paragraph = page.locator("p[class*='Hero-description']")
        self.hero_email_input = page.locator("#hero_user_email")
        self.hero_sign_up_button = page.get_by_role("button", name="Sign up for GitHub")

    def assert_loaded(self) -> None:
        """Verifies that key above-the-fold landing page elements are visible."""
        # Check the primary heading
        expect(self.hero_heading).to_be_visible()
        # Check that your main conversion form is present
        expect(self.hero_email_input).to_be_visible()




