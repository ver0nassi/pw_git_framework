from playwright.sync_api import Page, Locator, expect

class MainMenuComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

        self._container = page.get_by_role("dialog", name="Global navigation menu")
        self.close_menu_button = self._container.get_by_role("button", name="Close menu")

        self.home_link = self._container.get_by_role("link", name="Home")
        self.all_issues_link = self._container.get_by_role("link", name="All issues")
        self.all_pull_requests_link = self._container.get_by_role("link", name="All pull requests")
        self.all_repositories_link = self._container.get_by_role("link", name="All repositories")
        self.projects_link = self._container.get_by_role("link", name="Projects")
        self.discussions_link = self._container.get_by_role("link", name="Discussions")
        self.codespaces_link = self._container.get_by_role("link", name="Codespaces")
        self.copilot_link = self._container.get_by_role("link", name="Copilot")

        self.explore_link = self._container.get_by_role("link", name="Explore")
        self.marketplace_link = self._container.get_by_role("link", name="Marketplace")
        self.mcp_registry_link = self._container.get_by_role("link", name="MCP registry")

        self.top_repositories_heading = self._container.get_by_role("heading", name="Top repositories")
        self.search_for_repositories_button = self._container.get_by_role("button", name="Search for repositories")
        self.search_for_repositories_textbox = self._container.get_by_role("textbox", name="Search for repositories")

    def expect_opened(self) -> None:
        expect(self._container).to_be_visible()

    def close(self) -> None:
        self.close_menu_button.click()

    def expect_closed(self) -> None:
        expect(self._container).not_to_be_visible()

    def repo_link(self, name: str) -> Locator:
        """Return the repository link matching the provided repository name in username/reponame format."""
        return self._container.get_by_role("link", name=name)

    def search_repository(self, name: str) -> Locator:
        self.search_for_repositories_button.click()
        self.search_for_repositories_textbox.fill(name)
        return self.repo_link(name)
