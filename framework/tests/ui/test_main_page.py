import re

import pytest
from playwright.sync_api import expect

from framework.pages.guest_page import GuestPage
from framework.pages.login_page import LoginPage


def test_guest_main_page_is_loaded(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.assert_loaded()

def test_guest_user_redirected_to_login_when_clicking_try_git_hub_copilot_button(page):
    """Verify clicking 'Try GitHub Copilot' redirects unauthenticated user to login"""
    guest_page = GuestPage(page)
    guest_page.navigate()

    expect(guest_page.try_git_hub_copilot_link).to_be_visible()
    guest_page.try_git_hub_copilot_link.click()
    login_page = LoginPage(page)

    login_page.assert_loaded()
    expect(page).to_have_url(
        re.compile(r"https://github\.com/login\?.*return_to=.*github-copilot.*signup")
    )

def test_guest_main_page_contains_sign_in_link(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    expect(guest_page.header.sign_in_link).to_be_visible()

def test_guest_main_page_contains_sign_up_button(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    expect(guest_page.header.sign_up_link).to_be_visible()
    expect(guest_page.header.sign_up_link).to_be_enabled()

def test_guest_user_can_navigate_to_login(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.header.sign_in_link.click()
    login_page = LoginPage(page)
    login_page.assert_loaded()

def test_guest_homepage_rejects_invalid_email_format(page):
    guest_page = GuestPage(page)
    guest_page.navigate()
    expected_message = "Please include an '@' in the email address. 'ab.com' is missing an '@'."

    # missing @ symbol validation
    guest_page.hero_email_input.fill('ab.com')

    with page.expect_event("dialog") as event_info:
        guest_page.hero_sign_up_button.click()

    dialog = event_info.value
    assert expected_message in dialog.message
    assert dialog.type == "alert"

def test_guest_main_page_contains_guest_footer(page):
    guest_page = GuestPage(page)
    guest_page.navigate()

    guest_page.footer.expect_loaded()

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




