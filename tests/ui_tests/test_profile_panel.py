import allure
import pytest

from utils.file_helpers import get_test_file_path


@allure.feature("Profile Panel")
@allure.story("Profile Panel UI and actions")
@pytest.mark.ui
class TestProfilePanel:

    def _login_and_open_profile(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("yellowlatesummer@gmail.com")
        login_modal.when_fill_password("20039915aAa")
        login_modal.when_click_login_button()
        login_modal.should_be_logged_in()
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()
        profile_panel.should_see_profile_panel()

    @pytest.mark.medium
    def test_upload_profile_photo(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        self._login_and_open_profile(dashboard_page, login_modal, account_dropdown, profile_panel)

        test_file = get_test_file_path("test_image.jpg")
        profile_panel.upload_profile_photo(test_file)
        profile_panel.should_see_profile_photo_uploaded()

    @pytest.mark.medium
    def test_delete_profile_photo(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        self._login_and_open_profile(dashboard_page, login_modal, account_dropdown, profile_panel)

        test_file = get_test_file_path("test_image.jpg")
        profile_panel.upload_profile_photo(test_file)
        profile_panel.should_see_profile_photo_uploaded()
        profile_panel.hover_profile_photo()
        profile_panel.click_delete_photo()
        profile_panel.should_see_delete_modal()
        profile_panel.click_delete_modal_confirm()
        profile_panel.should_see_profile_photo_deleted()

    @pytest.mark.medium
    def test_upload_banner(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        self._login_and_open_profile(dashboard_page, login_modal, account_dropdown, profile_panel)

        test_file = get_test_file_path("test_image.jpg")
        profile_panel.upload_banner(test_file)
        profile_panel.should_see_banner_uploaded()

    @pytest.mark.medium
    def test_delete_banner(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        self._login_and_open_profile(dashboard_page, login_modal, account_dropdown, profile_panel)

        test_file = get_test_file_path("test_image.jpg")
        profile_panel.upload_banner(test_file)
        profile_panel.should_see_banner_uploaded()
        profile_panel.hover_banner()
        profile_panel.click_delete_banner()
        profile_panel.should_see_delete_modal()
        profile_panel.click_delete_modal_confirm()
        profile_panel.should_see_banner_deleted()

    @pytest.mark.low
    def test_click_username_navigates_to_profile(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        self._login_and_open_profile(dashboard_page, login_modal, account_dropdown, profile_panel)

        username = profile_panel.get_username()
        profile_panel.click_username()
        profile_panel.should_be_on_profile_page(username)
