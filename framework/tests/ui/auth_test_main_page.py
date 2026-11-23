import pytest
from playwright.sync_api import expect

from framework.tests.conftest import authenticated_main_page

# ------ Smoke tests ------
@pytest.mark.smoke
def test_saved_session_is_authenticated(authenticated_main_page):
    expect(authenticated_main_page.header.open_user_menu_button).to_be_visible()

@pytest.mark.smoke
def test_auth_main_page_contains_all_header_elements(authenticated_main_page):
    elements_to_verify_visibility = authenticated_main_page.header.get_all_header_elements()
    for element in elements_to_verify_visibility:
        expect(element).to_be_visible()

@pytest.mark.smoke
def test_auth_main_page_main_menu_is_opened(authenticated_main_page):
    main_menu = authenticated_main_page.header.open_main_menu()
    main_menu.expect_opened()
    expect(main_menu.home_link).to_be_visible()
    expect(main_menu.all_repositories_link).to_be_visible()

@pytest.mark.smoke
def test_auth_main_page_main_menu_is_closed(authenticated_main_page):
    main_menu = authenticated_main_page.header.open_main_menu()
    main_menu.expect_opened()
    expect(main_menu.home_link).to_be_visible()
    expect(main_menu.close_menu_button).to_be_visible()

    main_menu.close_menu_button.click()
    main_menu.expect_closed()

@pytest.mark.smoke
def test_auth_main_page_repo_sidebar_is_visible(authenticated_main_page):
    authenticated_main_page.repository_sidebar.assert_loaded()

@pytest.mark.smoke
def test_auth_main_page_copilot_chat_is_visible(authenticated_main_page):
    authenticated_main_page.dashboard.copilot_chat.assert_loaded()

@pytest.mark.smoke
def test_auth_main_page_dashboard_buttons_are_visible(authenticated_main_page):
    authenticated_main_page.dashboard.assert_loaded()





# -- -- -- Main Menu tests
@pytest.mark.regression
def test_main_menu_contains_all_elements_visible(authenticated_main_page):
    main_menu = authenticated_main_page.header.open_main_menu()
    main_menu.expect_opened()

    for element in main_menu.get_all_elements():
        expect(element).to_be_visible()

@pytest.mark.regression
def test_main_menu_repositories_are_visible(authenticated_main_page):
    pass

@pytest.mark.regression
def test_main_menu_search_repositories_textbox_is_visible(authenticated_main_page):
    main_menu = authenticated_main_page.header.open_main_menu()
    main_menu.expect_opened()

    main_menu.search_for_repositories_button.click()
    expect(main_menu.search_for_repositories_textbox).to_be_visible()

@pytest.mark.regression
def test_main_menu_searched_repository_name_is_found(authenticated_main_page):
    main_menu = authenticated_main_page.header.open_main_menu()
    main_menu.expect_opened()

    main_menu.search_repository("Sicily")
    expect(main_menu.repository_link("Mashynka/Sicily")).to_be_visible()




# - - - - - Side Bar tests
@pytest.mark.regression
def test_repository_sidebar_contains_specific_repository_name(authenticated_main_page):
    authenticated_main_page.repository_sidebar.assert_loaded()
    searched_repository = authenticated_main_page.repository_sidebar.get_repository("Mashynka/Sicily")
    expect(searched_repository).to_be_visible()

@pytest.mark.regression
def test_repository_sidebar_searched_repository_name_is_found(authenticated_main_page):
    repository_sidebar = authenticated_main_page.repository_sidebar

    repository_sidebar.search_button.click()
    repository_sidebar.search_textbox.fill("Sicily")
    expect(repository_sidebar.get_all_repositories()).to_have_count(1)
    expect(repository_sidebar.get_repository("Sicily")).to_be_visible()

@pytest.mark.regression
def test_repository_sidebar_searched_not_existing_repository_name_is_not_found(authenticated_main_page):
    repository_sidebar = authenticated_main_page.repository_sidebar

    repository_sidebar.search_button.click()
    repository_sidebar.search_textbox.fill("Borland")
    expect(repository_sidebar.get_all_repositories()).to_have_count(0)
    expect(repository_sidebar.get_repository("Sicily")).not_to_be_visible()

@pytest.mark.xfail(reason="TO DO")
@pytest.mark.regression
def test_repository_sidebar_new_button_redirects_to_new_repository_creation_page(authenticated_main_page):
    pass

# - - - - - Dashboard

@pytest.mark.regression
def test_copilot_chat_ask_button_shows_menu_items_upon_click(authenticated_main_page):
    dashboard = authenticated_main_page.dashboard
    dashboard.assert_loaded()

    ask_button_menu = dashboard.open_menu(dashboard.copilot_chat.ask_button)
    ask_button_menu_items = ask_button_menu.get_all_items()
    for menu in ask_button_menu_items:
        expect(ask_button_menu.get_item(menu)).to_be_visible()





