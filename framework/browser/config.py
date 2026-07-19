from pydantic.dataclasses import dataclass as pydantic_dataclass
from pydantic import Field
from typing import Literal

@pydantic_dataclass
class ViewportSize:
    width: int = Field(gt=0, le=7680)
    height: int = Field(gt=0, le=4320)

@pydantic_dataclass
class BrowserConfig:
    """Configuration for Playwright browser instance"""

    browser_type: Literal["chromium", "firefox", "webkit"] = "chromium"
    headless: bool = False
    timeout: int = Field(default=3000, ge=0)
    slow_mo: int = Field(default=0, ge=0)
    channel: str | None = None

@pydantic_dataclass
class ContextConfig:
    """Configuration for Playwright Browser Context"""

    viewport: ViewportSize | None = None
    java_script_enabled: bool = True
    base_url: str | None = None
    ignore_https_errors: bool = False
    locale: str | None = None
    timezone_id: str | None = None
    color_scheme: Literal["light", "dark", "no-preference"] | None = None
    user_agent: str | None = None
    storage_state: str | None = None
    accept_downloads: bool = True
