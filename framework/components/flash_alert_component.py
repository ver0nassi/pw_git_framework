from playwright.sync_api import Page, Locator, expect

class FlashAlertComponent:
    """Universal alert component to use in multiple pages"""
    def __init__(self, page: Page):
        self._container = page.locator("#js-flash-container")
        self._alert = self._container.get_by_role("alert")
        self.dismiss_button = self._container.get_by_role("button",name="Dismiss this message")

    @property
    def alert(self) -> Locator:
        return self._alert

    def assert_message(self, message: str) -> None:
        """Assert that the flash alert contains the expected message."""
        expect(self._alert).to_contain_text(message)