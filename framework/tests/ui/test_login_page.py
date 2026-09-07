import pytest
from playwright.sync_api import expect

from framework.pages.forgot_password_page import ForgotPasswordPage
from framework.pages.login_page import LoginPage


def test_guest_user_can_navigate_to_forgot_password_page_from_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.forgot_password_link.click()

    forgot_password_page = ForgotPasswordPage(page)
    forgot_password_page.assert_loaded()

def test_passkey_authentication_prompt_is_displayed(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.passkey_button.click()
    expect(login_page.passkey_waiting_message).to_be_visible()

def test_user_name_is_required_for_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

    expect(page.locator("#login_field:invalid")).to_be_visible()

    login_page.login_input.fill("test-user")

    expect(page.locator("#login_field:invalid")).not_to_be_visible()
    expect(page.locator("#login_field:valid")).to_be_visible()

def test_password_is_required_for_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

    expect(page.locator("#password:invalid")).to_be_visible()

    login_page.password_input.fill("test-password")

    expect(page.locator("#password:invalid")).not_to_be_visible()
    expect(page.locator("#password:valid")).to_be_visible()

def test_incorrect_username_or_password_error_is_displayed(page):
    login_page = LoginPage(page)
    login_page.navigate()
    expected_error_message = "Incorrect username or password."

    login_page.login("test-user", "test-password")
    login_page.flash_alert.assert_message(expected_error_message)

def test_password_input_is_masked(page):
    login_page = LoginPage(page)
    login_page.navigate()

    expect(login_page.password_input).to_have_attribute("type", "password")

def test_login_with_google_account_redirects_to_google(page):
    login_page = LoginPage(page)
    login_page.navigate()

    expect(login_page.continue_with_google_button).to_be_visible()
    login_page.continue_with_google_button.click()
    page.wait_for_url("**/accounts.google.com/**", timeout=10000)
    current_url = page.url

    assert "v3/signin" in current_url

def test_login_with_apple_account_redirects_to_apple(page):
    login_page = LoginPage(page)
    login_page.navigate()

    expect(login_page.continue_with_apple_button).to_be_visible()
    login_page.continue_with_apple_button.click()
    page.wait_for_url("**/appleid.apple.com/**", timeout=10000)
    current_url = page.url
    assert "/auth/authorize" in current_url

@pytest.mark.security
def test_login_page_uses_https_only(page):
    login_page = LoginPage(page)
    login_page.navigate("http://github.com/login")

    expect(page).to_have_url("https://github.com/login")

@pytest.mark.security
def test_login_page_contains_required_security_headers(page):
    login_page = LoginPage(page)
    login_page.navigate()

    response = page.reload()
    headers = response.headers
    assert "strict-transport-security" in headers
    assert "content-security-policy" in headers
    assert "x-frame-options" in headers


