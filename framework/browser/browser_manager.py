from dataclasses import dataclass, asdict
from framework.browser.config import BrowserConfig, ContextConfig
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page

class BrowserManager:
    def __init__(self, browser_config: BrowserConfig | None = None):
        self.browser_config = browser_config or BrowserConfig()
        self._playwright: Playwright | None = None
        self._browser: Browser | None = None

    def __enter__(self) -> "BrowserManager":
        self._playwright = sync_playwright().start()

        browser_type = self.browser_config.browser_type.lower()
        if not hasattr(self._playwright, browser_type):
            raise ValueError(f"Unsupported browser: {browser_type}")

        browser = getattr(self._playwright, browser_type)

        raw_launch_options = asdict(self.browser_config)
        # 2. Convert dataclass to a dict & remove keys Playwright launch doesn't accept
        clean_launch_options = {
                                key : value for key, value in raw_launch_options.items()
                                if value is not None and key !="browser_type"
        }

        self._browser = browser.launch(**clean_launch_options)
        return self

    def new_context(self, context_config : ContextConfig | None = None) -> BrowserContext:
        if not self._browser:
            raise RuntimeError("Browser not started. Use inside 'with' block")

        # Fallback
        config = context_config or ContextConfig()
        context_options = asdict(config)

        clean_context_options = {}
        for key, value in context_options.items():
            if key == "viewport":
                clean_context_options[key] = value
            elif value is not None:
                clean_context_options[key] = value

        return self._browser.new_context(**clean_context_options)

    def new_page(self, context: BrowserContext | None = None) -> Page:
        # If the user explicitly provided a context, use it.
        # Otherwise, fall back to creating a quick, one-off context.
        target_context = context or self.new_context()
        return target_context.new_page()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
        # avoids accidental reuse
        self._browser = None
        self._playwright = None