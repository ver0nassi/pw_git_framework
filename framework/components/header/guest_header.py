from enum import Enum
from playwright.sync_api import Page, Locator, expect

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

class GuestHeaderComponent:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._container = page.locator("header")
        # --- Header menu wrapper ---
        self._global_nav = page.locator(".HeaderMenu-wrapper")

        # --- Header Buttons ---
        self.platform_button = self._global_nav.get_by_role("button", name="Platform")
        self.solutions_button = self._global_nav.get_by_role("button", name="Solutions")
        self.resources_button = self._global_nav.get_by_role("button", name="Resources")
        self.open_source_button = self._global_nav.get_by_role("button", name="Open Source")
        self.enterprise_button = self._global_nav.get_by_role("button", name="Enterprise")
        self.pricing_button = self._global_nav.get_by_role("button", name="Pricing")

        # --- Actions ---
        self.search_trigger_button = page.get_by_role("button", name="Search or jump to…")
        self.sign_in_link = page.get_by_role("link", name="Sign in", exact=True)
        self.sign_up_link = page.get_by_role("link", name="Sign up", exact=True)

    def _get_active_dropdown(self, menu_button: Locator) -> Locator:
        """Helper to return the container element relative to the hovered button."""
        menu_button.hover()
        controls_id = menu_button.get_attribute("aria-controls")
        if not controls_id:
            raise ValueError(
                f"Button '{menu_button}' does not have an 'aria-controls' attribute to locate its dropdown.")
        return self.page.locator(f"#{controls_id}")

    def open_menu(self, menu_button: Locator) -> Locator:
        """Hovers over a header button and verifies the dropdown opened."""
        dropdown_container = self._get_active_dropdown(menu_button)
        expect(menu_button).to_have_attribute("aria-expanded", "true")
        expect(dropdown_container).to_be_visible()
        return dropdown_container

    def click_dropdown_link(self, menu_button: Locator, link_item_name: str | Enum) -> None:
        """Opens a dropdown menu and clicks a target link."""
        dropdown_container = self._get_active_dropdown(menu_button)
        dropdown_container.get_by_role("link", name=link_item_name, exact=True).click()

    def get_dropdown_items_text(self, menu_button: Locator) -> list[str]:
        """Parses all drop-down menu items names into a list."""
        dropdown_container = self._get_active_dropdown(menu_button)
        raw_titles = dropdown_container.get_by_role("link").all_text_contents()
        return [title.replace("New", "").strip() for title in raw_titles if title.strip()]
