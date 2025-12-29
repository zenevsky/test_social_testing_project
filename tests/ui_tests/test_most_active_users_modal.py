import allure
import pytest


@allure.feature("Most Active Users")
@allure.story("Most Active Users Modal")
@pytest.mark.ui
class TestMostActiveUsersModal:

    @pytest.mark.medium
    def test_modal_opens_and_has_users(self, dashboard_page, most_active_users_modal):
        dashboard_page.open_page()
        dashboard_page.click_get_most_active_users()
        most_active_users_modal.check_that_most_active_users_is_visible()
        most_active_users_modal.check_that_modal_contains_expected_users(5)
        most_active_users_modal.check_that_user_has_stats_entries(0, 3)
        most_active_users_modal.click_close()

    @pytest.mark.medium
    def test_click_user_opens_profile(self, dashboard_page, most_active_users_modal, profile_panel):
        dashboard_page.open_page()
        dashboard_page.click_get_most_active_users()
        most_active_users_modal.check_that_most_active_users_is_visible()
        username = most_active_users_modal.get_username_from_profile_url(0)
        most_active_users_modal.click_user(0)
        profile_panel.check_that_expected_profile_page_is_opened(username)
