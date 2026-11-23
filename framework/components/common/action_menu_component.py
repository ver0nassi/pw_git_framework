from enum import Enum

from playwright.sync_api import Locator, expect


class MenuItemRole(Enum):
    ITEM = "menuitem"
    RADIO = "menuitemradio"


class ActionMenuComponent:
    def __init__(self, locator: Locator, item_role: MenuItemRole = MenuItemRole.ITEM) -> None:
        self._container = locator
        self._item_role = item_role
        self.all_items = self._container.get_by_role(self.item_role.value)

    def get_item(self, item_name: str) -> Locator:
        """Locates a menu item by its accessible name."""
        return self._container.get_by_role(self._item_role.value, name=item_name, exact=True)

    def all_item_names(self) -> list[str]:
        """Return accessible text of all menu items."""
        return self.all_items.all_inner_texts()

    def assert_loaded(self) -> None:
        """Verify that the menu and at least one menu item are visible."""
        expect(self._container).to_be_visible()
        expect(self.all_items.first).to_be_visible()
