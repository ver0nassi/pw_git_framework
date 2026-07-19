from framework.browser.browser_manager import BrowserManager
from framework.pages.loggedout_page import GuestHeaderLinks, GuestPage

with BrowserManager() as manager:
    page = manager.new_page()
    guest_page = GuestPage(page)

    guest_page.navigate()
    guest_page.verify_page_loaded()
    guest_page.open_header_button_menu(guest_page.platform_button)
    page.wait_for_timeout(5000)
    test_list = guest_page.get_all_menu_items_text(guest_page.platform_button)
    print(test_list)
