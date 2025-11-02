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
        most_active_users_modal.should_be_visible()
        most_active_users_modal.should_have_users_count(5)
        most_active_users_modal.should_user_have_stats_entries(0, 3)
        most_active_users_modal.click_close()

    @pytest.mark.medium
    def test_click_user_opens_profile(self, dashboard_page, most_active_users_modal, profile_panel):
        dashboard_page.open_page()
        dashboard_page.click_get_most_active_users()
        most_active_users_modal.should_be_visible()
        username = most_active_users_modal.get_username(0)
        most_active_users_modal.click_user(0)
        profile_panel.should_be_on_profile_page(username)
