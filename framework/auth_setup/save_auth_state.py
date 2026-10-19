import re

from playwright.sync_api import sync_playwright

from framework.auth_setup.paths import AUTH_DIR, GITHUB_STATE


def main() -> None:
    AUTH_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        try:
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://github.com/login")
            print("Log in manually. Waiting for redirect to github.com...")
            page.wait_for_url(re.compile(r"^https://github\.com/?$"), timeout=0)

            context.storage_state(path=str(GITHUB_STATE))
            print(f"Auth state saved: {GITHUB_STATE}")

        finally:
            browser.close()


if __name__ == "__main__":
    main()