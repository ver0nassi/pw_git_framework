from framework.pages.base_page import BasePage
from playwright.sync_api import Page, expect

from framework.components.footer.guest_login_footer import GuestLoginFooterComponent
from framework.pages.forgot_password_page import ForgotPasswordPage

class LoginPage(BasePage):
    PAGE_PATH: str = "/login"
    def __init__(self, page : Page):
        super().__init__(page)

        self.footer = GuestLoginFooterComponent(page)
        # --- Locators ---
        self.heading = page.get_by_role("heading", name="Sign in to GitHub")
        self.login_input = page.get_by_label("Username or email address")
        self.password_input = page.get_by_label("Password")
        self.forgot_password_link = page.get_by_role("link", name="Forgot password?")

        self.sign_in_button = page.get_by_role("button", name="Sign in")
        self.continue_with_google_button = page.get_by_role("button", name="Continue with Google")
        self.continue_with_apple_button = page.get_by_role("button", name="Continue with Apple")

        self.create_account_link = page.get_by_role("link", name="Create an account")
        self.sign_in_with_passkey_button = page.get_by_role("button", name="Sign in with a passkey")

    def assert_loaded(self):
        expect(self.heading).to_be_visible()
        expect(self.login_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.sign_in_button).to_be_visible()
        self.footer.assert_loaded()

    def enter_username(self, username: str) -> None:
        self.login_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_sign_in(self) -> None:
        self.sign_in_button.click()

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()

    def open_forgot_password(self) -> ForgotPasswordPage:
        """CLicks on Forgot Password link and returns forgot password page"""
        self.forgot_password_link.click()
        return ForgotPasswordPage(self.page)