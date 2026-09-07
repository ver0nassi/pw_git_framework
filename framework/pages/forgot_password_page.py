from playwright.sync_api import Page, expect

from framework.components.footer.guest_login_footer import GuestLoginFooterComponent
from framework.pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    PAGE_PATH : str = "/password_reset"
    def __init__(self, page: Page):
        super().__init__(page)
        self.footer = GuestLoginFooterComponent(page)

        self._main = page.get_by_role("main")

        self.heading = self._main.get_by_role("heading", name="Reset your password")
        self.paragraph = self._main.get_by_role("paragraph")
        self.email_input = self._main.get_by_role("textbox", name="Email")
        self.send_password_button = self._main.get_by_role("button", name="Send password reset email")

    def assert_loaded(self) -> None:
        expect(self.heading).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.send_password_button).to_be_visible()


    def enter_email(self, email: str) -> None:
        self.email_input.fill(email)

    def click_send_password_reset(self) -> None:
        self.send_password_button.click()

    def request_password_reset(self, email: str) -> None:
        self.enter_email(email)
        self.click_send_password_reset()
