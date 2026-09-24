from playwright.sync_api import Locator, Page, expect


class ChangelogComponent:
    def __init__(self, page: Page) -> None:
        self._container = page.get_by_role("complementary", name="Explore")

        self.heading = self._container.get_by_role("heading", name="Latest from our changelog")
        self.changelog_items = self._container.locator("li").get_by_role("link")
        self.view_changelog_link = self._container.get_by_role("link", name="View changelog →")

    def get_item_titles(self) -> list[str]:
        """Returns the visible titles of all changelog items, in order."""
        return self.changelog_items.all_inner_texts()

    def get_item_by_index(self, index: int) -> Locator:
        return self.changelog_items.nth(index)

    def assert_loaded(self) -> None:
        expect(self.heading).to_be_visible()
        expect(self.changelog_items).to_be_visible()
        expect(self.view_changelog_link).to_be_visible()