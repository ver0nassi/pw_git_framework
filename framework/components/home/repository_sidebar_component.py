from playwright.sync_api import Locator, Page, expect


class RepositorySidebarComponent:
    def __init__(self, page: Page):
        self.page = page

        self._container = page.get_by_role("complementary", name="Dashboard menu")
        self.heading = self._container.get_by_role("heading", name="Top repositories")
        self.new_link = self._container.get_by_role("link", name="New")
        self.search_textbox = self._container.get_by_role("textbox", name="Find a repository…")

    def get_repository(self, repo_name:str) -> Locator:
        return self._container.get_by_role("link", name=repo_name, exact=False)

    def assert_loaded(self) -> None:
        expect(self.heading).to_be_visible()
        expect(self.new_link).to_be_visible()
        expect(self.search_textbox).to_be_visible()
