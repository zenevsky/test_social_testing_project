from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import account_dropdown_locators as loc


class AccountDropdown(BasePage):

    def open_dropdown(self) -> None:
        trigger = self.find("#account-dropdown-link")
        expect(trigger).to_be_visible()
        trigger.click()
        expect(self.find(loc.menu_container)).to_be_visible()

    def should_be_visible(self) -> None:
        expect(self.page.locator(loc.menu_container)).to_be_visible()

    def click_profile(self) -> None:
        self.page.click(loc.profile_link)

    def click_settings(self) -> None:
        self.page.click(loc.settings_link)

    def click_logout(self) -> None:
        self.page.click(loc.logout_link)

    def should_have_profile_item(self) -> None:
        expect(self.page.locator(loc.profile_link)).to_be_visible()

    def should_have_settings_item(self) -> None:
        expect(self.page.locator(loc.settings_link)).to_be_visible()

    def should_have_logout_item(self) -> None:
        expect(self.page.locator(loc.logout_link)).to_be_visible()
