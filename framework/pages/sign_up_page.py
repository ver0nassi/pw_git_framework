from playwright.sync_api import Page, expect

from framework.pages.base_page import BasePage


class SignUpPage(BasePage):
    PAGE_PATH = "/signup"
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_your_free_account_heading = page.get_by_role("heading", name="Create your free account")
        self.sign_up_for_github_heading = page.get_by_role("heading", name="Sign up for GitHub")

        self.continue_with_google_button = page.get_by_role("button", name="Continue with Google")
        self.continue_with_apple_button = page.get_by_role("button", name="Continue with Apple")

        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.username_input = page.get_by_role("textbox", name="Username")

        self.country_region_dropdown = page.get_by_role("button", name="Your Country/Region")
        self.country_region_list = page.get_by_role("listbox", name="Select Country/Region options")
        self.country_region_list_search_box = page.get_by_role("searchbox", name="Filter")
        self.country_region_list_close_button = page.get_by_role("button", name="Close")

        self.create_account_button = page.get_by_role("button", name="Create account")

    def assert_loaded(self) -> None:
        expect(self.create_your_free_account_heading).to_be_visible()
        expect(self.sign_up_for_github_heading).to_be_visible()
        expect(self.create_account_button).to_be_visible()

    def sign_up_with_email(self, email: str, password: str, username: str, country: str | None = None) -> None:
        if not all([email, password, username]):
            raise ValueError("Email, password, and username cannot be empty")

        self.email_input.fill(email)
        self.password_input.fill(password)
        self.username_input.fill(username)
        self.country_region_dropdown.click()

