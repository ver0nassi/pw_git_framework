from playwright.sync_api import Locator, Page, expect

from framework.components.home.feed_item_component import FeedItemComponent


class FeedComponent:
    def __init__(self, page: Page) -> None:

        self.heading = page.get_by_role("heading", name="Feed")
        self.filter_button = page.get_by_role("button", name="Filter")
        self.feed_items = page.get_by_role("region", name="repository body", exact=False)

        self.feed_items_header = self.feed_items.locator("header", has_text="Trending repositories")
        self.see_more_link = self.feed_items_header.get_by_role("link", name="See more")

    def assert_loaded(self) -> None:
        expect(self.heading).to_be_visible()
        expect(self.filter_button).to_be_visible()
        expect(self.feed_items).not_to_have_count(0)

    def get_item_by_index(self, index: int) -> FeedItemComponent:
        """Returns the repository feed item at a specific zero-based index first from top."""
        return FeedItemComponent(self.feed_items.nth(index))

