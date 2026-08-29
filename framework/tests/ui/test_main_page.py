import re

import pytest
from playwright.sync_api import expect

from framework.pages.guest_page import GuestPage
from framework.pages.login_page import LoginPage
from framework.pages.sign_up_page import SignUpPage


def test_guest_main_page_is_loaded(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.assert_loaded()

def test_guest_main_page_contains_sign_in_link(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    expect(guest_page.header.sign_in_link).to_be_visible()

def test_guest_main_page_contains_sign_up_link(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    expect(guest_page.header.sign_up_link).to_be_visible()

def test_guest_main_page_footer_is_loaded(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.footer.expect_loaded()

def test_guest_user_can_open_search_dialog(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.header.open_search()
    guest_page.search_dialog.assert_loaded()

def test_guest_user_is_redirected_to_login_from_try_github_copilot(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    expect(guest_page.try_git_hub_copilot_link).to_be_visible()
    guest_page.try_git_hub_copilot_link.click()
    login_page = LoginPage(page)

    login_page.assert_loaded()
    expect(page).to_have_url(
        re.compile(r"https://github\.com/login\?.*github-copilot.*signup")
    )

@pytest.mark.skip(reason="GitHub bot protection blocks automated signup flow")
def test_guest_user_can_navigate_to_signup_from_header(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.header.sign_up_link.click()
    sign_up_page = SignUpPage(page)
    sign_up_page.assert_loaded()

def test_guest_user_can_navigate_to_login(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.header.sign_in_link.click()
    login_page = LoginPage(page)
    login_page.assert_loaded()

def test_guest_homepage_rejects_invalid_email_format(page):
    guest_page = GuestPage(page)
    guest_page.navigate()
    invalid_email = "ab.com"
    expected_message = "Please include an '@' in the email address. 'ab.com' is missing an '@'."

    # missing @ symbol validation
    guest_page.hero_email_input.fill(invalid_email)

    with page.expect_event("dialog") as event_info:
        guest_page.hero_sign_up_button.click()

    dialog = event_info.value
    assert dialog.message == expected_message
    assert dialog.type == "alert"

@pytest.mark.parametrize(
    "menu_name",
    [
        "Platform",
        "Solutions",
        "Resources",
        "Open Source",
        "Enterprise"
    ],
)
def test_guest_user_can_open_header_menu(page, menu_name):
    guest_page = GuestPage(page)
    guest_page.navigate()

    menu_locator = guest_page.header.get_menu_locator(menu_name)

    print(f"\nTesting menu: {menu_name}")
    print(f"Locator count: {menu_locator.count()}")
    print(f"Visible: {menu_locator.is_visible()}")

    guest_page.header.open_menu(menu_locator)




