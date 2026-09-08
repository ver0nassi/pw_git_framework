import pytest
from playwright.sync_api import expect

from framework.components.common.flash_alert_component import FlashAlertComponent
from framework.pages.forgot_password_page import ForgotPasswordPage


def test_forgot_password_page_is_loaded(page):
    forgot_password_page = ForgotPasswordPage(page)
    forgot_password_page.navigate()

    forgot_password_page.assert_loaded()


def test_forgot_password_page_footer_is_displayed(page):
    forgot_password_page = ForgotPasswordPage(page)
    forgot_password_page.navigate()

    forgot_password_page.footer.assert_loaded()


@pytest.mark.security
def test_forgot_password_page_uses_https_only(page):
    forgot_password_page = ForgotPasswordPage(page)
    forgot_password_page.navigate("http://github.com/password_reset")

    expect(page).to_have_url("https://github.com/password_reset")


@pytest.mark.parametrize(
    "test_email",
    [
        "",
        "        ",
        "bobby.com",
        "bobby@com",
        " @.com",
        "bobby@."
    ]
)
def test_forgot_password_page_shows_error_for_invalid_email(page, test_email):
    forgot_password_page = ForgotPasswordPage(page)
    forgot_password_page.navigate()

    expected_message = (
        "That address is either invalid, not a verified primary email or is not associated "
        "with a personal user account. Organization billing emails are only for notifications"
    )

    forgot_password_page.email_input.fill(test_email)
    forgot_password_page.send_password_button.click()
    alert = FlashAlertComponent(page)
    alert.assert_message(expected_message)
    alert.dismiss_button.click()


def test_invalid_email_error_message_contains_expected_help_links(page):
    forgot_password_page = ForgotPasswordPage(page)
    forgot_password_page.navigate()

    expected_verified_primary_email_url = ("https://docs.github.com/account-and-profile/setting-up-and-managing-your-personal-"
                              "account-on-github/managing-email-preferences/changing-your-primary-email-address")
    expected_personal_user_account_url = "https://docs.github.com/get-started/learning-about-github/types-of-github-accounts"
    expected_billing_emails_url = ("https://docs.github.com/billing/managing-your-github-billing-settings/setting-your-billing-"
                           "email")

    forgot_password_page.email_input.fill("bobby.mac")
    forgot_password_page.send_password_button.click()
    alert = FlashAlertComponent(page)

    verified_primary_email_link = alert.get_link_by_text("verified primary email")
    personal_user_account_link = alert.get_link_by_text("personal user account")
    billing_emails_link = alert.get_link_by_text("billing emails")

    expect(verified_primary_email_link).to_have_attribute('href', expected_verified_primary_email_url)
    expect(personal_user_account_link).to_have_attribute('href', expected_personal_user_account_url)
    expect(billing_emails_link).to_have_attribute('href', expected_billing_emails_url)



