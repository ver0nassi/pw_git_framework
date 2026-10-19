from playwright.sync_api import Locator, Page, expect

from framework.components.common.base_component import BaseComponent
from framework.components.home.copilot_chat_component import CopilotChatComponent


class DashboardComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._container = page.locator('div[class*="copilotPreview"]')

        self.heading = self._container.get_by_role("heading", name="Home")
        self.copilot_chat = CopilotChatComponent(page, self._container)

        self.debug_button = self._container.get_by_role("button", name="Debug")
        self.agent_button = self._container.get_by_role("button", name="Agent")
        self.create_issue_button = self._container.get_by_role("button", name="Create issue")
        self.write_code_button = self._container.get_by_role("button", name="Write code")
        self.git_button = self._container.get_by_role("button", name="Git")
        self.pull_requests_button = self._container.get_by_role("button", name="Pull requests")

    def assert_loaded(self) -> None:
        expect(self.debug_button).to_be_visible()
        expect(self.agent_button).to_be_visible()
        expect(self.create_issue_button).to_be_visible()
        expect(self.write_code_button).to_be_visible()
        expect(self.git_button).to_be_visible()
        expect(self.pull_requests_button).to_be_visible()

