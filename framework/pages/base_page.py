from playwright.sync_api import BrowserContext, Page, Locator
from framework.components.flash_alert_component import FlashAlertComponent


class BasePage:
    BASE_URL: str = "https://github.com/"
    PAGE_PATH: str = "/"

    def __init__(self, page : Page):
        self.page = page
        self.flash_alert = FlashAlertComponent(page)

    def navigate(self, url : str | None = None) -> None:
        """Navigates to a URL. If no URL is provided, it falls back to the page's default PAGE_PATH."""
        target_url = url or f"{self.BASE_URL}{self.PAGE_PATH}"
        self.page.goto(target_url, wait_until="domcontentloaded")
        self.wait_loaded()

    def reload(self):
        self.page.reload(wait_until="load")

    def url(self) -> str:
        return self.page.url

    def title(self) -> str:
        return self.page.title()

    def wait_visible(self, locator: Locator) -> None:
        locator.wait_for(state="visible")

    def wait_loaded(self) -> None:
        #TODO
        pass

    def locator(self):
        #TODO
        pass

    def take_screenshot(self, path: str) -> bytes:
        return self.page.screenshot(path=path, full_page=True)

    def get_context(self) -> BrowserContext:
        return self.page.context

    # TODO methods
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
