import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import login_modal_locators as loc


class LoginModal(BasePage):

    @allure.step("Open login modal")
    def open_login_modal(self) -> None:
        self.find(loc.login_open_button).click()
        self.page.wait_for_selector(loc.modal_container, state="visible")

    @allure.step("Fill username: {username}")
    def fill_username(self, username: str) -> None:
        expect(self.find(loc.username_input)).to_be_visible()
        self.find(loc.username_input).fill(username)

    @allure.step("Fill password")
    def fill_password(self, password: str) -> None:
        expect(self.find(loc.password_input)).to_be_visible()
        self.find(loc.password_input).fill(password)

    @allure.step("Toggle 'Remember me'")
    def toggle_remember_me(self) -> None:
        expect(self.find(loc.remember_me_checkbox)).to_be_visible()
        self.find(loc.remember_me_checkbox).click()

    @allure.step("Click Login button")
    def click_login_button(self) -> None:
        self.page.wait_for_selector(loc.modal_container, state="visible")
        expect(self.find(loc.login_button)).to_be_visible()
        expect(self.find(loc.login_button)).to_be_enabled()
        self.find(loc.login_button).click()

    @allure.step("Click Password Recovery")
    def click_password_recovery(self) -> None:
        expect(self.find(loc.password_recovery_link)).to_be_visible()
        self.find(loc.password_recovery_link).click()
        self.page.wait_for_selector(loc.password_recovery_modal, state="visible")

    @allure.step("Click Back from Password Recovery")
    def click_back_from_recovery(self) -> None:
        expect(self.find(loc.password_recovery_back_button)).to_be_visible()
        self.find(loc.password_recovery_back_button).click()
        self.page.wait_for_selector(loc.modal_container, state="visible")

    @allure.step("Login modal should be visible")
    def check_that_login_modal_is_visible(self) -> None:
        expect(self.find(loc.modal_container)).to_be_visible()

    @allure.step("Password recovery modal should be visible")
    def check_that_password_recovery_modal_is_visible(self) -> None:
        expect(self.find(loc.password_recovery_modal)).to_be_visible()

    @allure.step("Login fields should be visible")
    def check_that_login_fields_is_visible(self) -> None:
        expect(self.find(loc.username_input)).to_be_visible()
        expect(self.find(loc.password_input)).to_be_visible()
        expect(self.find(loc.remember_me_checkbox)).to_be_visible()
        expect(self.find(loc.login_button)).to_be_visible()
        expect(self.find(loc.password_recovery_link)).to_be_visible()

    @allure.step("Should see error message: '{expected_text}'")
    def check_that_error_message_is_visible(self, expected_text: str = "User or Password incorrect.") -> None:
        expect(self.find(loc.error_message)).to_have_text(expected_text)

    @allure.step("User should be logged in")
    def check_that_user_is_logged_in(self) -> None:
        self.page.wait_for_selector(loc.modal_container, state="hidden")
        expect(self.find(loc.profile_user_name)).to_be_visible()
        expect(self.find(loc.profile_avatar)).to_be_visible()

    @allure.step("Open login modal and verify login UI")
    def open_modal(self):
        self.open_login_modal()
        self.check_that_login_modal_is_visible()
        self.check_that_login_fields_is_visible()

    @allure.step("Open password recovery modal")
    def open_password_recovery(self):
        self.click_password_recovery()
        self.check_that_password_recovery_modal_is_visible()

    @allure.step("Return from password recovery to login modal")
    def back_from_recovery(self):
        self.click_back_from_recovery()
        self.check_that_login_modal_is_visible()

    @allure.step("Login as '{username}'")
    def login_as(self, username: str, password: str):
        self.open_login_modal()
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
        self.check_that_user_is_logged_in()

    @allure.step("Login with invalid credentials '{username}/{password}'")
    def login_with_invalid_credentials(self, username: str, password: str):
        self.open_login_modal()
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
        self.check_that_error_message_is_visible()
