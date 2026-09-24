from playwright.sync_api import Page, expect

from framework.components.header.main_header_component import MainHeaderComponent
from framework.components.header.main_menu_component import MainMenuComponent
from framework.components.header.user_menu_component import UserMenuComponent
from framework.components.home.changelog_component import ChangelogComponent
from framework.components.home.feed_component import FeedItemComponent
from framework.components.home.repository_sidebar_component import (
    RepositorySidebarComponent,
)
from framework.pages.base_page import BasePage


class AuthenticatedMainPage(BasePage):
    PAGE_PATH: str = "/"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.header: MainHeaderComponent = MainHeaderComponent(page)
        self.main_menu: MainMenuComponent = MainMenuComponent(page)
        self.user_menu: UserMenuComponent = UserMenuComponent(page)
        self.feed: FeedItemComponent = FeedItemComponent(page)
        self.changelog: ChangelogComponent = ChangelogComponent(page)
        self.repository_sidebar: RepositorySidebarComponent = RepositorySidebarComponent(page)


