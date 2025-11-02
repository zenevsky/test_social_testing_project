import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import account_dropdown_locators as loc


class AccountDropdown(BasePage):

    @allure.step("Open account dropdown menu")
    def open_dropdown(self) -> None:
        trigger = self.find("#account-dropdown-link")
        expect(trigger).to_be_visible()
        trigger.click()
        expect(self.find(loc.menu_container)).to_be_visible()

    @allure.step("Account dropdown menu should be visible")
    def should_be_visible(self) -> None:
        expect(self.page.locator(loc.menu_container)).to_be_visible()

    @allure.step("Click 'Profile' in dropdown")
    def click_profile(self) -> None:
        self.page.click(loc.profile_link)

    @allure.step("Click 'Settings' in dropdown")
    def click_settings(self) -> None:
        self.page.click(loc.settings_link)

    @allure.step("Click 'Logout' in dropdown")
    def click_logout(self) -> None:
        self.page.click(loc.logout_link)

    @allure.step("Go to profile page via dropdown")
    def go_to_profile(self):
        self.open_dropdown()
        self.click_profile()

    @allure.step("Dropdown should contain 'Profile' item")
    def should_have_profile_item(self) -> None:
        expect(self.page.locator(loc.profile_link)).to_be_visible()

    @allure.step("Dropdown should contain 'Settings' item")
    def should_have_settings_item(self) -> None:
        expect(self.page.locator(loc.settings_link)).to_be_visible()

    @allure.step("Dropdown should contain 'Logout' item")
    def should_have_logout_item(self) -> None:
        expect(self.page.locator(loc.logout_link)).to_be_visible()
