import allure
import pytest


@allure.feature('Dashboard Page')
@allure.story('Dashboard Page')
@pytest.mark.ui
class TestDashboardPage:

    @pytest.mark.low
    def test_dashboard_tab_header_is_active(self, dashboard_page):
        dashboard_page.open_page()
        dashboard_page.check_dashboard_tab_header_is_active()
