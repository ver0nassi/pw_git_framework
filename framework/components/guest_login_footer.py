from playwright.sync_api import Page, expect

class GuestLoginFooterComponent:
    def __init__(self, page: Page):
        # --- Footer ---
        self._footer = page.get_by_role("contentinfo")
        # --- Links ---
        self.terms_link = self._footer.get_by_role("link", name="Terms")
        self.privacy_link = self._footer.get_by_role("link", name="Privacy")
        self.docs_link = self._footer.get_by_role("link", name="Docs")
        self.support_link = self._footer.get_by_role("link", name="Contact GitHub Support")
        # --- Buttons ---
        self.manage_cookies_button = self._footer.get_by_role("button", name="Manage cookies")
        self.dont_share_personal_info_button = self._footer.get_by_role("button", name="Do not share my personal information")

    def assert_loaded(self) -> None:
        expect(self._footer).to_be_visible()