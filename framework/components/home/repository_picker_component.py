from playwright.sync_api import Locator, expect
"""This component can eventually accommodate more repository-picker functionality:
- Selecting and deselecting repositories.
- Checking selected repository state.
- Searching repositories.
- Verifying multi-selection.
- Verifying empty search results."""


class RepositoryPickerComponent:
    def __init__(self, locator: Locator) -> None:
        self._container = locator

        self.options = self._container.get_by_role("option")
        self.search_combobox = self._container.get_by_role("combobox", name="Search")

    def get_option(self, option_name: str) -> Locator:
        """Return a repository option matching its accessible name."""
        return self._container.get_by_role("option", name=option_name, exact=True)

    def get_all_option_names(self) -> list[str]:
        return self.options.all_inner_texts()

    def assert_loaded(self) -> None:
        expect(self._container).to_be_visible()
        expect(self.options.first).to_be_visible()