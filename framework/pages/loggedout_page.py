from framework.pages.base_page import BasePage
from playwright.sync_api import Page

class GuestPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.global_header = page.locator("header.js-details-container")
        self.search_trigger_button = page.get_by_role("button", name="Search or jump to…")
        self.sign_in_link = page.get_by_role("link", name="Sign in", exact=True)
        self.sign_up_link = page.get_by_role("link", name="Sign up", exact=True)