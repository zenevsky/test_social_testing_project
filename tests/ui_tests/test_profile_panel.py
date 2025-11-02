import allure
import pytest

from utils.file_helpers import get_test_file_path


@allure.feature("Profile Panel")
@allure.story("Profile Panel UI and actions")
@pytest.mark.ui
class TestProfilePanel:

    @pytest.mark.medium
    def test_upload_profile_photo(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()

        test_file = get_test_file_path("test_image.jpg")
        profile_panel.upload_profile_photo(test_file)
        profile_panel.should_see_profile_photo_uploaded()

    @pytest.mark.medium
    def test_delete_profile_photo(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()

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
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()

        test_file = get_test_file_path("test_image.jpg")
        profile_panel.upload_banner(test_file)
        profile_panel.should_see_banner_uploaded()

    @pytest.mark.medium
    def test_delete_banner(self, dashboard_page, login_modal, account_dropdown, profile_panel):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()

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
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()

        username = profile_panel.get_username()
        profile_panel.click_username()
        profile_panel.should_be_on_profile_page(username)
