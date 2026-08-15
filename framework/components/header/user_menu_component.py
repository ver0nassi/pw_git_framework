from playwright.sync_api import Page, expect

class UserMenuComponent:
    def __init__(self, page: Page):
        self.page = page

        self._container = page.get_by_role("dialog", name="User navigation")

        self.user_image = self._container.get_by_role("img", name="User avatar")
        self.account_switch_button = self._container.get_by_role("button", name="Account switcher")
        self.set_status_button = self._container.get_by_role("button", name="Set status")

        self.profile_link = self._container.get_by_role("link", name="Profile")
        self.repositories_link = self._container.get_by_role("link", name="Repositories")
        self.stars_link = self._container.get_by_role("link", name="Stars")
        self.gists_link = self._container.get_by_role("link", name="Gists")
        self.organizations_link = self._container.get_by_role("link", name="Organizations")
        self.enterprises_link = self._container.get_by_role("link", name="Enterprises")
        self.sponsors_link = self._container.get_by_role("link", name="Sponsors")

        self.settings_link = self._container.get_by_role("link", name="Settings")
        self.copilot_settings_link = self._container.get_by_role("link", name="Copilot Settings")
        self.feature_preview_button = self._container.get_by_role("button", name="Feature preview")
        self.appearance_link = self._container.get_by_role("link", name="Appearance")
        self.accessibility_link = self._container.get_by_role("link", name="Accessibility")
        self.try_enterprise_link = self._container.get_by_role("link", name="Try Enterprise")

        self.sign_out_link = self._container.get_by_role("link", name="Sign out")

    def expect_opened(self) -> None:
        expect(self._container).to_be_visible()

    def expect_username(self, username: str) -> None:
        expect(self._container.get_by_role("heading", name=username)).to_be_visible()