from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import login_modal_locators as loc


class LoginModal(BasePage):
    def when_open_login_modal(self) -> None:
        self.find(loc.login_open_button).click()
        self.page.wait_for_selector(loc.modal_container, state="visible")

    def when_fill_username(self, username: str) -> None:
        expect(self.find(loc.username_input)).to_be_visible()
        self.find(loc.username_input).fill(username)

    def when_fill_password(self, password: str) -> None:
        expect(self.find(loc.password_input)).to_be_visible()
        self.find(loc.password_input).fill(password)

    def when_toggle_remember_me(self) -> None:
        expect(self.find(loc.remember_me_checkbox)).to_be_visible()
        self.find(loc.remember_me_checkbox).click()

    def when_click_login_button(self) -> None:
        self.page.wait_for_selector(loc.modal_container, state="visible")
        expect(self.find(loc.login_button)).to_be_visible()
        expect(self.find(loc.login_button)).to_be_enabled()
        self.find(loc.login_button).click()

    def when_click_password_recovery(self) -> None:
        expect(self.find(loc.password_recovery_link)).to_be_visible()
        self.find(loc.password_recovery_link).click()
        self.page.wait_for_selector(loc.password_recovery_modal, state="visible")

    def when_click_back_from_recovery(self) -> None:
        expect(self.find(loc.password_recovery_back_button)).to_be_visible()
        self.find(loc.password_recovery_back_button).click()
        self.page.wait_for_selector(loc.modal_container, state="visible")

    def should_see_login_modal(self) -> None:
        expect(self.find(loc.modal_container)).to_be_visible()

    def should_see_password_recovery_modal(self) -> None:
        expect(self.find(loc.password_recovery_modal)).to_be_visible()

    def should_see_login_fields(self) -> None:
        expect(self.find(loc.username_input)).to_be_visible()
        expect(self.find(loc.password_input)).to_be_visible()
        expect(self.find(loc.remember_me_checkbox)).to_be_visible()
        expect(self.find(loc.login_button)).to_be_visible()
        expect(self.find(loc.password_recovery_link)).to_be_visible()

    def should_see_error_message(self, expected_text: str = "User or Password incorrect.") -> None:
        """Verify the error message text on failed login."""
        expect(self.find(loc.error_message)).to_have_text(expected_text)

    def should_be_logged_in(self) -> None:
        self.page.wait_for_selector(loc.modal_container, state="hidden")
        expect(self.find(loc.profile_user_name)).to_be_visible()
        expect(self.find(loc.profile_avatar)).to_be_visible()
