from framework.pages.base_page import BasePage
from framework.components.guest_login_footer import GuestLoginFooterComponent

from playwright.sync_api import Page

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

    def enter_email(self, email: str) -> None:
        self.email_input.fill(email)

    def click_send_password_reset(self) -> None:
        self.send_password_button.click()

    def request_password_reset(self, email: str) -> None:
        self.enter_email(email)
        self.click_send_password_reset()
