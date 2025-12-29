import allure
from playwright.sync_api import expect, Locator
from pages.base_page import BasePage
from pages.locators import most_active_users_modal_locators as loc


class MostActiveUsersModal(BasePage):

    def get_modal(self) -> Locator:
        return self.page.locator(loc.modal_container)

    def get_close_button(self) -> Locator:
        return self.page.locator(loc.close_button)

    def get_users(self) -> Locator:
        return self.page.locator(loc.users_items)

    def get_user_item(self, index: int) -> Locator:
        return self.get_users().nth(index)

    def get_user_name(self, index: int) -> Locator:
        return self.get_user_item(index).locator(loc.user_name)

    def get_user_link(self, index: int) -> Locator:
        return self.get_user_item(index).locator(loc.user_link)

    def get_user_avatar(self, index: int) -> Locator:
        return self.get_user_item(index).locator(loc.user_avatar)

    def get_user_stats(self, index: int) -> Locator:
        return self.get_user_item(index).locator(loc.user_stats_entry)

    @allure.step("Click user #{index} in Most Active Users modal")
    def click_user(self, index: int) -> None:
        self.get_user_link(index).click()

    @allure.step("Close Most Active Users modal")
    def click_close(self) -> None:
        self.get_close_button().click()
        self.check_that_most_active_users_is_not_visible()

    @allure.step("Most Active Users modal should be visible")
    def check_that_most_active_users_is_visible(self) -> None:
        expect(self.get_modal()).to_be_visible()

    @allure.step("Most Active Users modal should not be visible")
    def check_that_most_active_users_is_not_visible(self) -> None:
        expect(self.get_modal()).not_to_be_visible()

    @allure.step("Modal should contain {expected} users")
    def check_that_modal_contains_expected_users(self, expected: int) -> None:
        expect(self.get_users()).to_have_count(expected)

    @allure.step("User #{index} should have name '{name}'")
    def check_that_user_has_name(self, index: int, name: str) -> None:
        expect(self.get_user_name(index)).to_have_text(name)

    @allure.step("User #{index} should have {expected} stats entries")
    def check_that_user_has_stats_entries(self, index: int, expected: int) -> None:
        expect(self.get_user_stats(index)).to_have_count(expected)

    @allure.step("Get profile URL for user #{index}")
    def get_user_profile_url(self, index: int) -> str:
        return self.get_user_link(index).get_attribute("href")

    @allure.step("Extract username from profile URL for user #{index}")
    def get_username_from_profile_url(self, index: int) -> str:
        return self.get_user_profile_url(index).split("/")[-2]
