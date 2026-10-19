import pytest
from playwright.sync_api import expect

from framework.pages.authenticated_main_page import AuthenticatedMainPage


def test_saved_session_is_authenticated(authenticated_page):
    auth_page = AuthenticatedMainPage(authenticated_page)
    auth_page.navigate()

    expect(auth_page.header.open_user_menu_button).to_be_visible()

def test_auth_main_page_contains_all_header_elements(authenticated_page):
    auth_page = AuthenticatedMainPage(authenticated_page)
    auth_page.navigate()

    elements_to_verify_visibility = auth_page.header.get_all_header_elements()
    for element in elements_to_verify_visibility:
        expect(element).to_be_visible()

def test_auth_main_page_main_menu_is_opened(authenticated_page):
    auth_page = AuthenticatedMainPage(authenticated_page)
    auth_page.navigate()

    main_menu = auth_page.header.open_main_menu()
    expect(main_menu.home_link).to_be_visible()

def test_auth_main_page_repo_sidebar_is_visible(authenticated_page):
    auth_page = AuthenticatedMainPage(authenticated_page)
    auth_page.navigate()

    auth_page.repository_sidebar.assert_loaded()

def test_auth_main_page_copilot_chat_is_visible(authenticated_page):
    auth_page = AuthenticatedMainPage(authenticated_page)
    auth_page.navigate()

    auth_page.dashboard.copilot_chat.assert_loaded()

def test_auth_main_page_dashboard_buttons_are_visible(authenticated_page):
    auth_page = AuthenticatedMainPage(authenticated_page)
    auth_page.navigate()

    auth_page.dashboard.assert_loaded()

