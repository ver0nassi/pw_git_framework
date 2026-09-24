from playwright.sync_api import Locator, Page

from framework.components.common.action_menu_component import ActionMenuComponent


class BaseComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_menu(self, trigger_button: Locator) -> ActionMenuComponent:
        """Shared method. Clicks the specified trigger button and returns the associated ActionMenuComponent."""
        trigger_button.click()
        menu_locator = self.page.locator('[role="menu"]:visible').last
        menu = ActionMenuComponent(menu_locator)
        menu.assert_loaded()

        return menu
