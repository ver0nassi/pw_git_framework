import pytest
from framework.browser.browser_manager import BrowserManager
from playwright.sync_api import BrowserContext, Page
from framework.browser.config import BrowserConfig, ContextConfig, ViewportSize


@pytest.fixture(scope="session")
def browser_manager() -> BrowserManager:
    browser_config = BrowserConfig(
        browser_type="chromium",
        headless=False,
        timeout=3000,
        slow_mo=0,
        channel=None
    )

    with BrowserManager(browser_config=browser_config) as manager:
        yield manager

@pytest.fixture(scope="function")
def context(browser_manager: BrowserManager) -> BrowserContext:
    context_config = ContextConfig(
        viewport = ViewportSize(width=1280, height=720),
        base_url="https://github.com/"
    )
    context = browser_manager.new_context(context_config)

    try:
        yield context
    finally:
        context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()

    try:
        yield page
    finally:
        page.close()