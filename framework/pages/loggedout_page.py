from framework.pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

from enum import Enum

class GuestHeaderLinks:
    """Namespace grouping for the GitHub guest header dropdown menus."""
    # --- Platform Dropdown Items ---
    class Platform(str,Enum):
        # --- AI CODE CREATION ---
        COPILOT = "GitHub Copilot"
        COPILOT_APP = "GitHub Copilot app"
        MCP_REGISTRY = "MCP Registry"

        # --- DEVELOPER WORKFLOWS ---
        ACTIONS = "Actions"
        CODESPACES = "Codespaces"
        ISSUES = "Issues"
        CODE_REVIEW = "Code Review"

        # --- APPLICATION SECURITY ---
        ADVANCED_SECURITY = "GitHub Advanced Security"
        CODE_SECURITY = "Code security"
        SECRET_PROTECTION = "Secret protection"

        # --- EXPLORE ---
        WHY_GITHUB = "Why GitHub"
        DOCUMENTATION = "Documentation"
        BLOG = "Blog"
        CHANGELOG = "Changelog"
        MARKETPLACE = "Marketplace"

        # --- GLOBAL FOOTER LINK ---
        VIEW_ALL_FEATURES = "View all features"

    # --- Solutions Dropdown Items ---
    class Solutions(str,Enum):
        # --- BY COMPANY SIZE ---
        ENTERPRISES = "Enterprises"
        SMALL_AND_MEDIUM_TEAMS = "Small and medium teams"
        STARTUPS = "Startups"
        NONPROFITS = "Nonprofits"

        # --- BY USE CASE ---
        APP_MODERNIZATION = "App Modernization"
        DEVSECOPS = "DevSecOps"
        DEVOPS = "DevOps"
        CI_CD = "CI/CD"
        VIEW_ALL_USE_CASES = "View all use cases"

        # --- BY INDUSTRY ---
        HEALTHCARE = "Healthcare"
        FINANCIAL_SERVICES = "Financial services"
        MANUFACTURING = "Manufacturing"
        GOVERNMENT = "Government"
        VIEW_ALL_INDUSTRIES = "View all industries"

        # --- GLOBAL FOOTER LINK ---
        VIEW_ALL_SOLUTIONS = "View all solutions"

    # --- Resources Dropdown Items ---
    class Resources(str,Enum):
        # --- EXPLORE BY TOPIC ---
        AI = "AI"
        SOFTWARE_DEVELOPMENT = "Software Development"
        DEVOPS = "DevOps"
        SECURITY = "Security"
        VIEW_ALL_TOPICS = "View all topics"

        # --- EXPLORE BY TYPE ---
        CUSTOMER_STORIES = "Customer stories"
        EVENTS_AND_WEBINARS = "Events & webinars"
        EBOOKS_AND_REPORTS = "Ebooks & reports"
        BUSINESS_INSIGHTS = "Business insights"
        GITHUB_SKILLS = "GitHub Skills"

        # --- SUPPORT & SERVICES ---
        DOCUMENTATION = "Documentation"
        CUSTOMER_SUPPORT = "Customer support"
        COMMUNITY_FORUM = "Community forum"
        TRUST_CENTER = "Trust center"
        PARTNERS = "Partners"

        # --- GLOBAL FOOTER LINK ---
        VIEW_ALL_RESOURCES = "View all resources"

    # --- OpenSource Dropdown Items ---
    class OpenSource(str,Enum):
        # --- COMMUNITY ---
        SPONSORS = "GitHub Sponsors"

        # --- PROGRAMS ---
        SECURITY_LAB = "Security Lab"
        MAINTAINER_COMMUNITY = "Maintainer Community"
        ACCELERATOR = "Accelerator"
        GITHUB_STARS = "GitHub Stars"
        ARCHIVE_PROGRAM = "Archive Program"

        # --- REPOSITORIES ---
        TOPICS = "Topics"
        TRENDING = "Trending"
        COLLECTIONS = "Collections"

    # --- OpenSource Dropdown Items ---
    class Enterprise(str,Enum):
        # --- ENTERPRISE SOLUTIONS ---
        ENTERPRISE_PLATFORM = "Enterprise platform"

        # --- AVAILABLE ADD-ONS ---
        ADVANCED_SECURITY = "GitHub Advanced Security"
        COPILOT_FOR_BUSINESS = "Copilot for Business"
        PREMIUM_SUPPORT = "Premium Support"

class GuestPage(BasePage):
    PAGE_PATH: str = "/"
    def __init__(self, page: Page):
        super().__init__(page)

        self.global_header = page.locator("header.js-details-container")
        # --- Header buttons ---
        self.platform_button = page.get_by_role("button", name="Platform")
        self.solutions_button = page.get_by_role("button", name="Solutions")
        self.resources_button = page.get_by_role("button", name="Resources")
        self.open_source_button = page.get_by_role("button", name="Open Source")
        self.enterprise_button = page.get_by_role("button", name="Enterprise")
        self.pricing_button = page.get_by_role("button", name="Pricing")
        self.nav_dropdown = page.locator("div[class*='__dropdown']")
        self.nav_dropdown_item = page.locator("span[class*='__title']")
        # --- Header Search, Sing in, Sign up elements
        self.search_trigger_button = page.get_by_role("button", name="Search or jump to…")
        self.sign_in_link = page.get_by_role("link", name="Sign in", exact=True)
        self.sign_up_link = page.get_by_role("link", name="Sign up", exact=True)
        # --- Top banner items ---
        self.hero_heading = page.get_by_role("heading", name="The future of building happens together")
        self.hero_paragraph = page.locator("p[class*='Hero-description']")
        self.hero_email_input = page.locator("#hero_user_email")
        self.hero_sign_up_button = page.get_by_role("button", name="Sign up for GitHub")

    def open_header_button_menu(self, menu_button: Locator) -> None:
        """Hovers over header buttons to trigger drop-down menu"""
        menu_button.hover()
        specific_dropdown = menu_button.locator("xpath=..").locator(self.nav_dropdown)
        specific_dropdown.wait_for(state="visible")

    def click_link_in_header_dropdown(self, menu_button: Locator, link_item_name: str) -> None:
        """Hovers over header buttons to trigger drop-down menu and clicks on specific link from it with exact name"""
        self.open_header_button_menu(menu_button)
        self.nav_dropdown.get_by_role("link", name=link_item_name, exact=True).click()

    def verify_page_loaded(self) -> None:
        """Verifies that key above-the-fold landing page elements are visible."""
        # Check the primary heading
        expect(self.hero_heading).to_be_visible()
        # Check that your main conversion form is present
        expect(self.hero_email_input).to_be_visible()

    def get_all_menu_items_text(self, menu_button: Locator) -> list[str]:
        """Parses all drop-down menu items names into list"""
        active_dropdown = menu_button.locator("xpath=..").locator(self.nav_dropdown)
        span_titles = active_dropdown.locator(self.nav_dropdown_item)
        raw_titles = span_titles.all_text_contents()
        return [title.replace("New", "").strip() for title in raw_titles if title.strip()]




