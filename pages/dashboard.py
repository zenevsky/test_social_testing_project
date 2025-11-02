import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import dashboard_locators as loc


class DashboardPage(BasePage):
    page_url = '/dashboard'

    @allure.step("Check that Dashboard tab header is active")
    def check_dashboard_tab_header_is_active(self):
        dashboard_tab_header = self.find(loc.dashboard_tab_header)
        expect(dashboard_tab_header).to_have_class('active')

    @allure.step("Click 'See all' button on Dashboard page")
    def click_to_see_all_button(self):
        self.page.get_by_text(loc.see_all_button).click()

    @allure.step("Click 'Get a list' in Most Active Users block")
    def click_get_most_active_users(self) -> None:
        self.find(loc.most_active_users_get_list_button).click()
