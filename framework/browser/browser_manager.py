from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page

class PlaywrightBrowserManager:
    def __init__(self, headless: bool = False, slow_mo: int = 0):
        self.headless = headless
        self.slow_mo = slow_mo
        self._playwright: Playwright | None = None
        self._browser: Browser | None = None

    def __enter__(self):
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=self.headless, slow_mo=self.slow_mo)
        return self

    def new_context(self, js_enabled: bool = True) -> BrowserContext:
        if not self._browser:
            raise RuntimeError("Browser not started. Use inside 'with' block")
        return self._browser.new_context(java_script_enabled=js_enabled, viewport={"width":1536, "height": 720})

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
