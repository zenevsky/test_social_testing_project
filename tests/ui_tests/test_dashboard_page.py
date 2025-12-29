import allure
import pytest


@allure.feature('Dashboard Page')
@allure.story('Dashboard Page')
@pytest.mark.ui
class TestDashboardPage:

    @pytest.mark.medium
    def test_spaces_page_is_opened_by_clicking_to_see_all_button(self, dashboard_page, spaces_page):
        dashboard_page.open_page()
        dashboard_page.check_dashboard_tab_header_is_active()
        dashboard_page.click_to_see_all_button()
        spaces_page.check_that_active_spaces_tab_is_visible()
