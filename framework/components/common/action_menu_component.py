from playwright.sync_api import Locator, expect


class ActionMenuComponent:
    def __init__(self, locator: Locator) -> None:
        self._container = locator
        self.all_items = self._container.get_by_role("menuitem")

    def get_item(self, item_name: str) -> Locator:
        """Locates a menu item by its accessible name."""
        return self._container.get_by_role("menuitem", name=item_name)

    def all_item_names(self) -> list[str]:
        return self.all_items.all_inner_texts()

    def assert_loaded(self) -> None:
        expect(self._container).to_be_visible()
        expect(self.all_items.first).to_be_visible()
