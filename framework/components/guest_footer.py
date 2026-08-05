from enum import Enum
from typing import TypeAlias
from playwright.sync_api import Page, Locator, expect

# Enums namespace
class GuestFooterLinks:
    """Namespace grouping for the GitHub guest footer menus."""
    class Newsletter(str, Enum):
        NEWSLETTER_HEADING = "The developer newsletter"
        NEWSLETTER_PARAGRAPH = "Get tips, technical guides, and best practices. Twice a month. Right in your inbox."
        NEWSLETTER_SUBSCRIBE_BUTTON = "Subscribe"

    class MarketingFooterHeading(str, Enum):
        PLATFORM = "PLATFORM"
        ECOSYSTEM = "ECOSYSTEM"
        SUPPORT = "SUPPORT"
        COMPANY = "COMPANY"

    class Platform(str, Enum):
        FEATURES = "Features"
        ENTERPRISE = "Enterprise"
        COPILOT = "Copilot"
        AI = "AI"
        SECURITY = "Security"
        PRICING = "Pricing"
        TEAM = "Team"
        RESOURCES = "Resources"
        ROADMAP = "Roadmap"
        COMPARE_GITHUB = "Compare GitHub"

    class Ecosystem(str, Enum):
        DEVELOPER_API = "Developer API"
        PARTNERS = "Partners"
        EDUCATION = "Education"
        GITHUB_CLI = "GitHub CLI"
        GITHUB_DESKTOP = "GitHub Desktop"
        GITHUB_MARKETPLACE = "GitHub Marketplace"
        MCP_REGISTRY = "MCP Registry"

    class Support(str, Enum):
        DOCS = "Docs"
        COMMUNITY_FORUM = "Community Forum"
        PROFESSIONAL_SERVICES = "Professional Services"
        PREMIUM_SUPPORT = "Premium Support"
        SKILLS = "Skills"
        STATUS = "Status"
        CONTACT_GITHUB = "Contact GitHub"
        WHAT_IS_GIT = "What is Git?"
        SITEMAP = "Sitemap"

    class Company(str, Enum):
        ABOUT = "About"
        WHY_GITHUB = "Why GitHub"
        CUSTOMER_STORIES = "Customer Stories"
        BLOG = "Blog"
        THE_README_PROJECT = "The ReadME Project"
        CAREERS = "Careers"
        NEWSROOM = "Newsroom"
        INCLUSION = "Inclusion"
        SOCIAL_IMPACT = "Social Impact"
        SHOP = "Shop"

    class Legal(str, Enum):
        TERMS = "Terms"
        PRIVACY = "Privacy"

    class LegalButton(str, Enum):
        MANAGE_COOKIES = "Manage cookies"
        DO_NOT_SHARE_MY_PERSONAL_INFORMATION = "Do not share my personal information"

    class Social(str, Enum):
        LINKEDIN = "Github on LinkedIn"
        INSTAGRAM = "Github on Instagram"
        YOUTUBE = "Github on YouTube"
        X = "Github on X"
        TIKTOK = "Github on TikTok"
        TWITCH = "Github on Twitch"
        GITHUB = "GitHub's organization on GitHub"

# Type aliases
MarketingFooterLink: TypeAlias = (
    GuestFooterLinks.Platform
    | GuestFooterLinks.Ecosystem
    | GuestFooterLinks.Support
    | GuestFooterLinks.Company
)
LegalFooterLink: TypeAlias = GuestFooterLinks.Legal
LegalFooterButton: TypeAlias = GuestFooterLinks.LegalButton
SocialFooterLink: TypeAlias = GuestFooterLinks.Social

class GuestFooterComponent:
    def __init__(self, page: Page):
        self.page = page
        # --- Footer ---
        self._footer= page.locator("footer")
        # --- Marketing Footer ---
        self._marketing_footer = self._footer.locator(".MarketingFooter-module")
        self._newsletter_container = self._marketing_footer.locator(".Newsletter-module")
        # --- Sub Footer ---
        self._sub_footer_container = self._footer.locator(".SubFooter-module")
        self._legal_container = self._footer.get_by_role("navigation", name="Legal and Resource Links")
        self._social_container = self._footer.get_by_role("navigation", name="GitHub's Social Media Links")
        # unique elements
        self.newsletter_heading = self._footer.get_by_role("heading", name=GuestFooterLinks.Newsletter.NEWSLETTER_HEADING)
        self.newsletter_description = self._newsletter_container.locator("p")
        self.subscribe_button = self._footer.get_by_role("link", name=GuestFooterLinks.Newsletter.NEWSLETTER_SUBSCRIBE_BUTTON)
        self.language_button = self._footer.get_by_role("button", name="English - Select language")


    def get_marketing_link(self, link: MarketingFooterLink) -> Locator:
        """Returns Marketing Footer item link locator"""
        return self._marketing_footer.get_by_role("link", name=link.value)

    def get_legal_link(self, link: LegalFooterLink) -> Locator:
        """Returns Legal Footer item link locator"""
        return self._legal_container.get_by_role("link", name=link.value)

    def get_legal_button(self, button: LegalFooterButton) -> Locator:
        """Returns Legal Footer button locator"""
        return self._legal_container.get_by_role("button", name=button.value)

    def get_social_link(self, link: SocialFooterLink) -> Locator:
        """Returns Social Footer item link locator"""
        return self._social_container.get_by_role("link", name=link.value)

    def click_marketing_link(self, link: MarketingFooterLink) -> None:
        """Gets and clicks Marketing Footer item link"""
        self.get_marketing_link(link).click()

    def click_legal_link(self, link: LegalFooterLink) -> None:
        """Gets and clicks Legal Footer item link"""
        self.get_legal_link(link).click()

    def click_legal_button(self, button: LegalFooterButton) -> None:
        """Gets and clicks Legal Footer Button"""
        self.get_legal_link(button).click()

    def click_social_link(self, link: SocialFooterLink) -> None:
        """Gets and clicks Social Footer link"""
        self.get_social_link(link).click()

    def click_subscribe(self) -> None:
        self.subscribe_button.click()

    def click_language_selector(self) -> None:
        self.language_button.click()

    # @classmethod
    # def get_marketing_links(cls) -> list[MarketingFooterLink]:
    #     return [
    #         *cls.Platform,
    #         *cls.Ecosystem,
    #         *cls.Support,
    #         *cls.Company,
    #     ]

    def expect_newsletter_section(self) -> None:
        """Checks for Newsletter related items visibility"""
        expect(self.newsletter_heading).to_have_text(GuestFooterLinks.Newsletter.NEWSLETTER_HEADING.value)
        expect(self.newsletter_description).to_have_text(GuestFooterLinks.Newsletter.NEWSLETTER_PARAGRAPH.value)
        expect(self.subscribe_button).to_have_text(GuestFooterLinks.Newsletter.NEWSLETTER_SUBSCRIBE_BUTTON.value)

    def expect_marketing_links_present(self) -> None:
        """Iterates over Marketing Footer links (GuestFooterLinks namespace) and asserts visibility of each menu item"""
        for enum_cls in (
                GuestFooterLinks.Platform,
                GuestFooterLinks.Ecosystem,
                GuestFooterLinks.Support,
                GuestFooterLinks.Company,
        ):
            for link in enum_cls:
                expect(self.get_marketing_link(link)).to_be_visible()

    def expect_legal_links_present(self) -> None:
        """Iterates over Legal Footer Section links and buttons and asserts visibility of each item"""
        for link in GuestFooterLinks.Legal:
            expect(self.get_legal_link(link)).to_be_visible()

        for button in GuestFooterLinks.LegalButton:
            expect(self.get_legal_button(button)).to_be_visible()

    def expect_social_links_present(self) -> None:
        """Iterates over Social Footer Section links asserts visibility of each item"""
        for link in GuestFooterLinks.Social:
            expect(self.get_social_link(link)).to_be_visible()

    def expect_loaded(self):
        """ Combines all expect methods in Footer"""    
        self.expect_newsletter_section()
        self.expect_marketing_links_present()
        self.expect_legal_links_present()
        self.expect_social_links_present()



