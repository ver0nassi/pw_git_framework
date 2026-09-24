from playwright.sync_api import Locator, Page, expect

from framework.components.common.base_component import BaseComponent


class CopilotChatComponent(BaseComponent):
    def __init__(self, page: Page, container: Locator) -> None:
        super().__init__(page)
        self._container = container

        self.textbox = self._container.get_by_role(
            "textbox", name="Ask anything or type @ to add context with Copilot"
        )
        self.ask_button = self._container.get_by_role("button", name="Ask")
        self.select_repository_button = self._container.get_by_role(
            "button", name="Select repositories to attach to conversation"
        )
        self.add_files_and_spaces_button = self._container.get_by_role("button", name="Add files, and spaces")
        self.model_button = self._container.get_by_role("button", name="Model:", exact=False)
        self.optimized_for_button = self._container.get_by_role("button", name="Optimized for:", exact=False)
        self.view_token_usage_button = self._container.get_by_role("button", name="View token usage")
        self.send_now_button = self._container.get_by_role("button", name="Send now ( enter )")

    def assert_loaded(self) -> None:
        expect(self.textbox).to_be_visible()
        expect(self.ask_button).to_be_visible()
        expect(self.send_now_button).to_be_visible()