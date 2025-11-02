import allure
import pytest
from pages.pages_data.profile_data import GeneralData, CommunicationData, SocialData


@allure.feature('Edit Profile Page')
@allure.story('Edit Profile Page')
@pytest.mark.ui
class TestEditProfilePage:

    @pytest.mark.medium
    def test_fill_general_tab(self, dashboard_page, login_modal, account_dropdown, profile_panel, edit_profile_page):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.go_to_profile()
        profile_panel.click_edit_account()
        edit_profile_page.fill_general_tab(GeneralData())

    @pytest.mark.medium
    def test_fill_communication_tab(self, dashboard_page, login_modal, account_dropdown, profile_panel,
                                    edit_profile_page):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.go_to_profile()
        profile_panel.click_edit_account()
        edit_profile_page.fill_communication_tab(CommunicationData())

    @pytest.mark.medium
    def test_fill_social_tab(self, dashboard_page, login_modal, account_dropdown, profile_panel, edit_profile_page):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.go_to_profile()
        profile_panel.click_edit_account()
        edit_profile_page.fill_social_tab(SocialData())

    @pytest.mark.medium
    def test_required_fields_validation(self, dashboard_page, login_modal, account_dropdown, profile_panel,
                                        edit_profile_page):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        account_dropdown.go_to_profile()
        profile_panel.click_edit_account()
        edit_profile_page.validate_required_fields()
