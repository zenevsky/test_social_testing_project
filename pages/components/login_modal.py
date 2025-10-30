from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import login_modal_locators as loc


class LoginModal(BasePage):
    #
    # ---------- WHEN (actions) ----------
    #

    def when_open_login_modal(self) -> None:
        """Open the login modal."""
        self.find(loc.login_open_button).click()
        self.page.wait_for_selector(loc.modal_container, state="visible")

    def when_fill_username(self, username: str) -> None:
        """Fill in the username or email."""
        expect(self.find(loc.username_input)).to_be_visible()
        self.find(loc.username_input).fill(username)

    def when_fill_password(self, password: str) -> None:
        """Fill in the password."""
        expect(self.find(loc.password_input)).to_be_visible()
        self.find(loc.password_input).fill(password)

    def when_toggle_remember_me(self) -> None:
        """Toggle the Remember Me checkbox."""
        expect(self.find(loc.remember_me_checkbox)).to_be_visible()
        self.find(loc.remember_me_checkbox).click()

    def when_click_login_button(self) -> None:
        """Click the Sign In button."""
        self.page.wait_for_selector(loc.modal_container, state="visible")
        expect(self.find(loc.login_button)).to_be_visible()
        expect(self.find(loc.login_button)).to_be_enabled()
        self.find(loc.login_button).click()

    def when_click_password_recovery(self) -> None:
        """Click the Forgot password link."""
        expect(self.find(loc.password_recovery_link)).to_be_visible()
        self.find(loc.password_recovery_link).click()
        self.page.wait_for_selector(loc.password_recovery_modal, state="visible")

    def when_click_back_from_recovery(self) -> None:
        """Go back to the login modal from the password recovery form."""
        expect(self.find(loc.password_recovery_back_button)).to_be_visible()
        self.find(loc.password_recovery_back_button).click()
        self.page.wait_for_selector(loc.modal_container, state="visible")

    #
    # ---------- SHOULD (assertions) ----------
    #

    def should_see_login_modal(self) -> None:
        """Verify that the login modal is visible."""
        expect(self.find(loc.modal_container)).to_be_visible()

    def should_see_password_recovery_modal(self) -> None:
        """Verify that the password recovery modal is visible."""
        expect(self.find(loc.password_recovery_modal)).to_be_visible()

    def should_see_login_fields(self) -> None:
        """Verify that all mandatory login fields and buttons are visible."""
        expect(self.find(loc.username_input)).to_be_visible()
        expect(self.find(loc.password_input)).to_be_visible()
        expect(self.find(loc.remember_me_checkbox)).to_be_visible()
        expect(self.find(loc.login_button)).to_be_visible()
        expect(self.find(loc.password_recovery_link)).to_be_visible()

    def should_see_error_message(self, expected_text: str = "User or Password incorrect.") -> None:
        """Verify the error message text on failed login."""
        expect(self.find(loc.error_message)).to_have_text(expected_text)

    def should_be_logged_in(self) -> None:
        """Verify that the user is successfully logged in."""
        self.page.wait_for_selector(loc.modal_container, state="hidden")
        expect(self.find(loc.profile_menu_icon)).to_be_visible()
