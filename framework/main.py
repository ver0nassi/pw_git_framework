from framework.browser.browser_manager import BrowserManager
from framework.pages.guest_page import GuestPage

with BrowserManager() as manager:
    page = manager.new_page()
    guest_page = GuestPage(page)

    guest_page.navigate()
    guest_page.verify_page_loaded()

    guest_page.header.open_menu(guest_page.header.platform_button)
    page.wait_for_timeout(5000)
    test_list = guest_page.header.get_dropdown_items_text(guest_page.header.platform_button)
    print(test_list)
