from playwright.sync_api import Locator, expect


class FeedItemComponent:
    def __init__(self, locator: Locator) -> None:
        self._container = locator

        self.profile_image = self._container.get_by_role("img", name="profile", exact=False)
        self.repo_name = self._container.locator("[data-hovercard-type='repository']")

        self.star_repository_button = self._container.get_by_role("button", name="Star this repository")
        self.add_repository_to_list_button = self._container.get_by_role(
            "button", name="Add this repository to a list"
        )

        self.section_details = self._container.get_by_role("region", name="Repo Details", exact=False)
        self.language = self.section_details.locator('span[itemprop="programmingLanguage"]')
        self.stars_link = self.section_details.get_by_role("link", name="stargazers", exact=False)

        self.repo_description = self._container.locator("div").filter(has=self.repo_name)

    def assert_loaded(self) -> None:
        expect(self.repo_name).to_be_visible()
        expect(self.repo_description).to_be_visible()
        expect(self.section_details).to_be_visible()