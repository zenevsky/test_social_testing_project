import allure
from playwright.sync_api import expect
from pages.locators import edit_profile_locators as loc
from pages.base_page import BasePage


class EditProfilePage(BasePage):
    page_url = '/user/account/edit'

    @allure.step("Open General tab")
    def open_general_tab(self):
        self.page.click(loc.general_tab)
        expect(self.page.locator(loc.first_name_input)).to_be_visible()

    @allure.step("Open Communication tab")
    def open_communication_tab(self):
        self.page.click(loc.communication_tab)
        expect(self.page.locator(loc.phone_private_input)).to_be_visible()

    @allure.step("Open Social tab")
    def open_social_tab(self):
        self.page.click(loc.social_tab)
        expect(self.page.locator(loc.website_input)).to_be_visible()

    @allure.step("Fill first name: {value}")
    def fill_first_name(self, value: str):
        self.page.fill(loc.first_name_input, value)
        expect(self.page.locator(loc.first_name_input)).to_have_value(value)

    @allure.step("Fill last name: {value}")
    def fill_last_name(self, value: str):
        self.page.fill(loc.last_name_input, value)
        expect(self.page.locator(loc.last_name_input)).to_have_value(value)

    @allure.step("Fill title: {value}")
    def fill_title(self, value: str):
        self.page.fill(loc.title_input, value)
        expect(self.page.locator(loc.title_input)).to_have_value(value)

    @allure.step("Select gender: {value}")
    def select_gender(self, value: str):
        self.page.select_option(loc.gender_select, value)
        expect(self.page.locator(loc.gender_select)).to_have_value(value)

    @allure.step("Fill street: {value}")
    def fill_street(self, value: str):
        self.page.fill(loc.street_input, value)
        expect(self.page.locator(loc.street_input)).to_have_value(value)

    @allure.step("Fill ZIP code: {value}")
    def fill_zip(self, value: str):
        self.page.fill(loc.zip_input, value)
        expect(self.page.locator(loc.zip_input)).to_have_value(value)

    @allure.step("Fill city: {value}")
    def fill_city(self, value: str):
        self.page.fill(loc.city_input, value)
        expect(self.page.locator(loc.city_input)).to_have_value(value)

    @allure.step("Select country: {value}")
    def select_country(self, value: str):
        self.page.select_option(loc.country_select, value)
        expect(self.page.locator(loc.country_select)).to_have_value(value)

    @allure.step("Fill state: {value}")
    def fill_state(self, value: str):
        self.page.fill(loc.state_input, value)
        expect(self.page.locator(loc.state_input)).to_have_value(value)

    @allure.step("Fill birthday: {value}")
    def fill_birthday(self, value: str):
        self.page.fill(loc.birthday_input, value)
        expect(self.page.locator(loc.birthday_input)).to_have_value(value)

    @allure.step("Set 'Hide year' checkbox to {checked}")
    def set_hide_year(self, checked: bool = True):
        checkbox = self.page.locator(loc.hide_year_checkbox)
        if checkbox.is_checked() != checked:
            checkbox.check() if checked else checkbox.uncheck()
        expect(checkbox).to_be_checked() if checked else expect(checkbox).not_to_be_checked()

    @allure.step("Fill 'About' field")
    def fill_about(self, value: str):
        self.page.fill(loc.about_textarea, value)
        expect(self.page.locator(loc.about_textarea)).to_have_value(value)

    @allure.step("Fill private phone: {value}")
    def fill_phone_private(self, value: str):
        self.page.fill(loc.phone_private_input, value)
        expect(self.page.locator(loc.phone_private_input)).to_have_value(value)

    @allure.step("Fill work phone: {value}")
    def fill_phone_work(self, value: str):
        self.page.fill(loc.phone_work_input, value)
        expect(self.page.locator(loc.phone_work_input)).to_have_value(value)

    @allure.step("Fill mobile: {value}")
    def fill_mobile(self, value: str):
        self.page.fill(loc.mobile_input, value)
        expect(self.page.locator(loc.mobile_input)).to_have_value(value)

    @allure.step("Fill fax: {value}")
    def fill_fax(self, value: str):
        self.page.fill(loc.fax_input, value)
        expect(self.page.locator(loc.fax_input)).to_have_value(value)

    @allure.step("Fill XMPP: {value}")
    def fill_xmpp(self, value: str):
        self.page.fill(loc.xmpp_input, value)
        expect(self.page.locator(loc.xmpp_input)).to_have_value(value)

    @allure.step("Fill website: {value}")
    def fill_website(self, value: str):
        self.page.fill(loc.website_input, value)
        expect(self.page.locator(loc.website_input)).to_have_value(value)

    @allure.step("Fill Facebook: {value}")
    def fill_facebook(self, value: str):
        self.page.fill(loc.facebook_input, value)
        expect(self.page.locator(loc.facebook_input)).to_have_value(value)

    @allure.step("Fill LinkedIn: {value}")
    def fill_linkedin(self, value: str):
        self.page.fill(loc.linkedin_input, value)
        expect(self.page.locator(loc.linkedin_input)).to_have_value(value)

    @allure.step("Fill Instagram: {value}")
    def fill_instagram(self, value: str):
        self.page.fill(loc.instagram_input, value)
        expect(self.page.locator(loc.instagram_input)).to_have_value(value)

    @allure.step("Fill Xing: {value}")
    def fill_xing(self, value: str):
        self.page.fill(loc.xing_input, value)
        expect(self.page.locator(loc.xing_input)).to_have_value(value)

    @allure.step("Fill YouTube: {value}")
    def fill_youtube(self, value: str):
        self.page.fill(loc.youtube_input, value)
        expect(self.page.locator(loc.youtube_input)).to_have_value(value)

    @allure.step("Fill Vimeo: {value}")
    def fill_vimeo(self, value: str):
        self.page.fill(loc.vimeo_input, value)
        expect(self.page.locator(loc.vimeo_input)).to_have_value(value)

    @allure.step("Fill TikTok: {value}")
    def fill_tiktok(self, value: str):
        self.page.fill(loc.tiktok_input, value)
        expect(self.page.locator(loc.tiktok_input)).to_have_value(value)

    @allure.step("Fill Twitter: {value}")
    def fill_twitter(self, value: str):
        self.page.fill(loc.twitter_input, value)
        expect(self.page.locator(loc.twitter_input)).to_have_value(value)

    @allure.step("Fill Mastodon: {value}")
    def fill_mastodon(self, value: str):
        self.page.fill(loc.mastodon_input, value)
        expect(self.page.locator(loc.mastodon_input)).to_have_value(value)

    @allure.step("Fill General tab")
    def fill_general(self, **kwargs):
        for field, value in kwargs.items():
            method = getattr(self, f"fill_{field}", None)
            if method:
                method(value)

    @allure.step("Fill Communication tab")
    def fill_communication(self, **kwargs):
        for field, value in kwargs.items():
            method = getattr(self, f"fill_{field}", None)
            if method:
                method(value)

    @allure.step("Fill Social tab")
    def fill_social(self, **kwargs):
        for field, value in kwargs.items():
            method = getattr(self, f"fill_{field}", None)
            if method:
                method(value)

    @allure.step("Save profile")
    def save_profile(self):
        self.page.click(loc.save_button)

    @allure.step("Success message should be visible")
    def should_see_success_message(self, text: str):
        expect(self.page.locator(loc.status_message_span)).to_have_text(text)

    @allure.step("First name error should be visible")
    def should_see_first_name_error(self, text: str):
        expect(self.page.locator(loc.first_name_error)).to_have_text(text)

    @allure.step("Last name error should be visible")
    def should_see_last_name_error(self, text: str):
        expect(self.page.locator(loc.last_name_error)).to_have_text(text)

    @allure.step("Fill General tab and save profile")
    def fill_general_tab(self, general_data):
        self.fill_general(**general_data.__dict__)
        self.save_profile()
        self.should_see_success_message("Saved")

    @allure.step("Fill Communication tab and save profile")
    def fill_communication_tab(self, comm_data):
        self.open_communication_tab()
        self.fill_communication(**comm_data.__dict__)
        self.save_profile()
        self.should_see_success_message("Saved")

    @allure.step("Fill Social tab and save profile")
    def fill_social_tab(self, social_data):
        self.open_social_tab()
        self.fill_social(**social_data.__dict__)
        self.save_profile()
        self.should_see_success_message("Saved")

    @allure.step("Validate required fields on General tab")
    def validate_required_fields(self):
        self.fill_first_name("")
        self.fill_last_name("")
        self.save_profile()
        self.should_see_first_name_error("First name cannot be blank.")
        self.should_see_last_name_error("Last name cannot be blank.")
