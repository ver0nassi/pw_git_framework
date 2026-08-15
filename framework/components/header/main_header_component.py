from playwright.sync_api import Page

from framework.components.header.main_menu_component import MainMenuComponent
from framework.components.header.user_menu_component import UserMenuComponent

class MainHeaderComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

        self._container = page.get_by_role("banner", name="Global navigation menu")
        self.open_menu_button = self._container.get_by_role("button", name="Open menu")
        self.dashboard_button = self._container.get_by_role("link", name="Dashboard")
        self.search_button = self._container.get_by_role("button", name="Open quick search dialog, type / to search")
        self.copilot_link = self._container.get_by_role("link", name="Chat with Copilot")
        self.open_copilot_button = self._container.get_by_role("button", name="Open Copilot...")
        self.create_new_button = self._container.get_by_role("button", name="Create new...")
        self.all_issues_link = self._container.get_by_role("link", name="All issues ( g then i )")
        self.all_pull_requests_link = self._container.get_by_role("link", name="All pull requests ( g then p )")
        self.all_repositories_link = self._container.get_by_role("link", name="All repositories")
        self.notifications_link = self._container.get_by_role("link", name="You have no unread notifications")
        self.open_user_menu_button = self._container.get_by_role("button", name="Open user navigation menu")

    def open_user_menu(self) -> UserMenuComponent:
        self.open_user_menu_button.click()
        menu = UserMenuComponent(self.page)
        menu.expect_opened()
        return menu

    def open_main_menu(self) -> MainMenuComponent:
        self.open_menu_button.click()
        menu = MainMenuComponent(self.page)
        menu.expect_opened()
        return menu


