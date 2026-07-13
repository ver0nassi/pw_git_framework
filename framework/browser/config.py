from dataclasses import dataclass

@dataclass
class BrowserConfig:
    """Configuration for Playwright browser instance"""

    browser_type: str = "chromium" # Options: "chromium", "firefox", "webkit"
    headless: bool = False
    timeout: int = 3000
    slow_mo: int = 0
    channel: str | None = None

@dataclass
class ContextConfig:
    """Configuration for Playwright Browser Context"""

    viewport: dict[str, int] | None = None
    java_script_enabled: bool = True
    base_url: str | None = None
    ignore_https_errors: bool = False
    locale: str | None = None
    timezone_id: str | None = None
    color_scheme: str | None = None # "light" | "dark" | "no-preference"
    user_agent: str | None = None
    storage_state: str | None = None
    accept_downloads: bool = True
