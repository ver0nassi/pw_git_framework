from playwright.sync_api import Locator, Page, expect


class SearchDialogComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

        self._container = page.get_by_role("dialog", name="Quick search")

        self.search_input = self._container.get_by_role("combobox", name="Search or jump to")
        self._search_suggestions = self._container.get_by_role("listbox", name="Search suggestions")
        self.clear_search_button = self._container.get_by_role("button", name="Clear search")

        self.search_syntax_tip_link = self._container.get_by_role("link", name="Search syntax tips")

    def assert_loaded(self) -> None:
        expect(self.search_input).to_be_visible()
        expect(self._search_suggestions).to_be_visible()

    def get_option(self, option_name: str) -> Locator:
        return self._search_suggestions.get_by_role("option", name=option_name, exact=True)