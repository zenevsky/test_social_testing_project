import pytest
import allure


@allure.feature("Login Page")
@allure.story("Login modal UI and behavior")
@pytest.mark.ui
class TestLogin:

    @pytest.mark.low
    @allure.title("Login modal becomes visible and fields are visible")
    def test_login_modal_visible_and_fields(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.open_modal()

    @pytest.mark.medium
    @allure.title("Password recovery flow works correctly")
    def test_password_recovery_flow(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.open_modal()
        login_modal.open_password_recovery()
        login_modal.back_from_recovery()

    @pytest.mark.medium
    @allure.title("Login with invalid credentials shows error")
    def test_login_invalid_credentials(self, dashboard_page, login_modal):
        dashboard_page.open_page()
        login_modal.login_with_invalid_credentials("wrong_user", "wrong_pass")

    @pytest.mark.high
    @allure.title("User can login successfully with valid credentials")
    def test_login_successful(self, dashboard_page, login_modal, account_dropdown):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.go_to_profile()
