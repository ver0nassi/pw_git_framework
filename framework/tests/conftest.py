from collections.abc import Iterator

import pytest
from playwright.sync_api import BrowserContext, Page

from framework.auth_setup.paths import GITHUB_STATE
from framework.browser.browser_manager import BrowserManager
from framework.browser.config import BrowserConfig, ContextConfig, ViewportSize


@pytest.fixture(scope="session")
def auth_state_path() -> str:
    """Resolve and validate the saved session. Fails fast if missing."""
    if not GITHUB_STATE.is_file():
        pytest.fail(
            f"Auth state not found at {GITHUB_STATE}.\n"
            f"Run: python -m framework.scripts.save_auth_state",
            pytrace=False
        )
    return str(GITHUB_STATE)


@pytest.fixture(scope="session")
def browser_manager() -> Iterator[BrowserManager]:
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
def context(browser_manager: BrowserManager) -> Iterator[BrowserContext]:
    context_config = ContextConfig(
        viewport = ViewportSize(width=1280, height=720)
    )
    context = browser_manager.new_context(context_config)

    try:
        yield context
    finally:
        context.close()
#--------------- auth_setup --------------
@pytest.fixture(scope="function")
def authenticated_context(
    auth_state_path: str,
    browser_manager: BrowserManager
) -> Iterator[BrowserContext]:
    """Context pre-loaded with the saved session."""
    context = browser_manager.new_context(
        ContextConfig(
            viewport=ViewportSize(width=1440, height=900),
            storage_state=auth_state_path,
        )
    )
    try:
        yield context
    finally:
        context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Iterator[Page]:
    page = context.new_page()

    try:
        yield page
    finally:
        page.close()

#------------------  auth_setup ---------------------
@pytest.fixture(scope="function")
def authenticated_page(authenticated_context: BrowserContext) -> Iterator[Page]:
    page = authenticated_context.new_page()
    try:
        yield page
    finally:
        page.close()