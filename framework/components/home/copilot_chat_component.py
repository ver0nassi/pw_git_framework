from playwright.sync_api import Locator, Page, expect
from framework.components.common.base_component import BaseComponent
from framework.components.common.action_menu_component import (
    ActionMenuComponent,
    MenuItemRole
)
from framework.components.home.repository_picker_component import RepositoryPickerComponent


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
        self.select_repository_dialog = self.page.get_by_role("dialog", name="Select a repository", exact=True)
        self.add_files_and_spaces_button = self._container.get_by_role("button", name="Add files, and spaces")
        self.model_button = self._container.get_by_role("button", name="Model:", exact=False)
        self.optimized_for_button = self._container.get_by_role("button", name="Optimized for:", exact=False)
        self.view_token_usage_button = self._container.get_by_role("button", name="View token usage")
        self.send_now_button = self._container.get_by_role("button", name="Send now", exact=False)

    def assert_loaded(self) -> None:
        expect(self.textbox).to_be_visible()
        expect(self.ask_button).to_be_visible()
        expect(self.send_now_button).to_be_visible()

    def open_ask_menu(self) -> ActionMenuComponent:
        return self.open_menu(self.ask_button, MenuItemRole.RADIO)

    def open_all_repositories_menu(self) -> RepositoryPickerComponent:
        self.select_repository_button.click()
        picker = RepositoryPickerComponent(self.select_repository_dialog)
        picker.assert_loaded()

        return picker