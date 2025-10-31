import pytest
import allure


@allure.feature("Login Page")
@allure.story("Login modal UI and behavior")
@pytest.mark.ui
class TestLogin:

    @pytest.mark.low
    @allure.title("Login modal becomes visible when opened")
    def test_login_modal_visible(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.should_see_login_modal()

    @pytest.mark.low
    @allure.title("Login fields are visible in modal")
    def test_login_fields_visible(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.should_see_login_fields()

    @pytest.mark.medium
    @allure.title("Password recovery flow works correctly")
    def test_password_recovery_flow(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_click_password_recovery()
        login_modal.should_see_password_recovery_modal()
        login_modal.when_click_back_from_recovery()
        login_modal.should_see_login_modal()

    @pytest.mark.medium
    @allure.title("Login with invalid credentials shows error")
    def test_login_invalid_credentials(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("wrong_user")
        login_modal.when_fill_password("wrong_pass")
        login_modal.when_click_login_button()
        login_modal.should_see_error_message()

    @pytest.mark.high
    @allure.title("User can login successfully with valid credentials")
    def test_login_successful(self, dashboard_page, login_modal, account_dropdown):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("yellowlatesummer@gmail.com")
        login_modal.when_fill_password("20039915aAa")
        login_modal.when_click_login_button()
        login_modal.should_be_logged_in()
        account_dropdown.open_dropdown()
        account_dropdown.should_have_profile_item()
        account_dropdown.should_have_logout_item()
