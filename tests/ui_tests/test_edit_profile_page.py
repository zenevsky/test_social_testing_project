import time

import allure
import pytest
from pages.pages_data.profile_data import GeneralData, CommunicationData, SocialData


@allure.feature('Edit Profile Page')
@allure.story('Edit Profile Page')
@pytest.mark.ui
class TestEditProfilePage:

    @pytest.mark.medium
    def test_fill_general_tab(self, edit_profile_page, dashboard_page, login_modal, account_dropdown, profile_panel):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("yellowlatesummer@gmail.com")
        login_modal.when_fill_password("20039915aAa")
        login_modal.when_click_login_button()
        login_modal.should_be_logged_in()
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()
        profile_panel.click_edit_account()

        general_data = GeneralData()

        edit_profile_page.fill_general(
            first_name=general_data.first_name,
            last_name=general_data.last_name,
            title=general_data.title,
            gender=general_data.gender,
            street=general_data.street,
            zip_code=general_data.zip_code,
            city=general_data.city,
            state=general_data.state,
            country=general_data.country,
            birthday=general_data.birthday,
            hide_year=general_data.hide_year,
            about=general_data.about
        )
        edit_profile_page.save_profile()
        edit_profile_page.should_see_success_message("Saved")

    @pytest.mark.medium
    def test_fill_communication_tab(self, edit_profile_page, dashboard_page, login_modal, account_dropdown,
                                    profile_panel):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("yellowlatesummer@gmail.com")
        login_modal.when_fill_password("20039915aAa")
        login_modal.when_click_login_button()
        login_modal.should_be_logged_in()
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()
        profile_panel.click_edit_account()

        comm_data = CommunicationData()

        edit_profile_page.open_communication_tab()
        edit_profile_page.fill_communication(
            phone_private=comm_data.phone_private,
            phone_work=comm_data.phone_work,
            mobile=comm_data.mobile,
            fax=comm_data.fax,
            xmpp=comm_data.xmpp
        )
        edit_profile_page.save_profile()
        edit_profile_page.should_see_success_message("Saved")

    @pytest.mark.medium
    def test_fill_social_tab(self, edit_profile_page, dashboard_page, login_modal, account_dropdown, profile_panel):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("yellowlatesummer@gmail.com")
        login_modal.when_fill_password("20039915aAa")
        login_modal.when_click_login_button()
        login_modal.should_be_logged_in()
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()
        profile_panel.click_edit_account()

        social_data = SocialData()

        edit_profile_page.open_social_tab()
        edit_profile_page.fill_social(
            website=social_data.website,
            facebook=social_data.facebook,
            linkedin=social_data.linkedin,
            instagram=social_data.instagram,
            xing=social_data.xing,
            youtube=social_data.youtube,
            vimeo=social_data.vimeo,
            tiktok=social_data.tiktok,
            twitter=social_data.twitter,
            mastodon=social_data.mastodon
        )
        edit_profile_page.save_profile()
        edit_profile_page.should_see_success_message("Saved")

    @pytest.mark.medium
    def test_required_fields_validation(
            self,
            edit_profile_page,
            dashboard_page,
            login_modal,
            account_dropdown,
            profile_panel
    ):
        dashboard_page.open_page()
        login_modal.when_open_login_modal()
        login_modal.when_fill_username("yellowlatesummer@gmail.com")
        login_modal.when_fill_password("20039915aAa")
        login_modal.when_click_login_button()
        login_modal.should_be_logged_in()
        account_dropdown.open_dropdown()
        account_dropdown.click_profile()
        profile_panel.click_edit_account()

        edit_profile_page.fill_first_name("")
        edit_profile_page.fill_last_name("")

        edit_profile_page.save_profile()

        edit_profile_page.should_see_first_name_error("First name cannot be blank.")
        edit_profile_page.should_see_last_name_error("Last name cannot be blank.")
