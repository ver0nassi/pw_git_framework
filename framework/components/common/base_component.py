from playwright.sync_api import Locator, Page

from framework.components.common.action_menu_component import ActionMenuComponent, MenuItemRole


class BaseComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_menu(self, trigger_button: Locator, item_role: MenuItemRole = MenuItemRole.ITEM) -> ActionMenuComponent:
        """Shared method. Clicks the specified trigger button and returns the associated ActionMenuComponent."""
        trigger_button.click()
        menu_locator = self.page.locator('[role="menu"]:visible').last
        menu = ActionMenuComponent(menu_locator, item_role)
        menu.assert_loaded()

        return menu

    # shared helper temp for dialog openings
    # def open_dialog(self, trigger_button: Locator, dialog: Locator) -> Locator:
        trigger_button.click()
        expect(dialog).to_be_visible()
        return dialog