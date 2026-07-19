from framework.browser.config import BrowserConfig, ContextConfig
from playwright.sync_api import BrowserContext, Page
from framework.browser.browser_manager import BrowserManager

class BasePage:
    BASE_URL: str = "https://github.com/"
    PAGE_PATH: str = "/"
    def __init__(self, page : Page):
        self.page = page

        self.global_search_input = page.locator(".QueryBuilder-InputWrapper").get_by_role("combobox")
        # or alternatively find the combobox that is actively visible on the screen
        # self.global_search_input = page.get_by_role("combobox").locator("visible=true")
        self.global_footer = page.get_by_role("contentinfo")
        self.flash_alert_container = page.locator("#js-flash-container")

    def navigate(self, url : str | None = None) -> None:
        """
        Navigates to a URL.
        If no URL is provided, it falls back to the page's default PAGE_PATH.
        """
        target_url = url or f"{self.BASE_URL}{self.PAGE_PATH}"
        self.page.goto(target_url, wait_until="networkidle")

    def reload(self):
        self.page.reload(wait_until="networkidle")

    def url(self) -> str:
        return self.page.url

    def title(self) -> str:
        return self.page.title()

    def wait_loaded(self):
        #TODO
        pass

    def locator(self):
        #TODO
        pass

    def take_screenshot(self):
        #TODO
        pass

    def get_context(self) -> BrowserContext:
        return self.page.context

    def assert_no_system_errors(self):
        """A global safety check to ensure GitHub didn't throw an unexpected alert banner."""
        if self.flash_alert_container.is_visible():
            error_msg = self.flash_alert_container.inner_text().strip()
            raise AssertionError(f"System error detected on page: {error_msg}")

    # TODO methods
    # click(locator)
    #
    # fill(locator, text)
    #
    # hover(locator)
    #
    # wait_visible(locator)
    #
    # wait_hidden(locator)
    #
    # is_visible(locator)
    #
    # scroll_into_view(locator)
