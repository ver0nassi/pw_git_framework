from playwright.sync_api import Locator, Page, expect


class RepositorySidebarComponent:
    def __init__(self, page: Page):
        self.page = page

        self._container = page.get_by_role("complementary", name="Dashboard menu")
        self.heading = self._container.get_by_role("heading", name="Top repositories")
        self.new_link = self._container.get_by_role("link", name="New", exact=True)
        self.search_button = self._container.get_by_role("button", name="Search for repositories")
        self.search_textbox = self._container.get_by_role("textbox", name="Search for repositories")

    def get_repository(self, repo_name:str) -> Locator:
        return self._container.get_by_role("link", name=repo_name, exact=False)

    def get_all_repositories(self):
        return self._container.locator("a[data-component='NavList.Item'][data-testid='dynamic-side-panel-items-item']")

    def assert_loaded(self) -> None:
        expect(self.heading).to_be_visible()
        expect(self.search_textbox).to_be_visible()
