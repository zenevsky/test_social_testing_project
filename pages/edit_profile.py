from playwright.sync_api import expect
from pages.locators import edit_profile_locators as loc
from pages.base_page import BasePage


class EditProfilePage(BasePage):
    page_url = '/user/account/edit'

    def open_general_tab(self):
        self.page.click(loc.general_tab)
        expect(self.page.locator(loc.first_name_input)).to_be_visible()

    def open_communication_tab(self):
        self.page.click(loc.communication_tab)
        expect(self.page.locator(loc.phone_private_input)).to_be_visible()

    def open_social_tab(self):
        self.page.click(loc.social_tab)
        expect(self.page.locator(loc.website_input)).to_be_visible()

    def fill_first_name(self, value: str):
        self.page.fill(loc.first_name_input, value)
        expect(self.page.locator(loc.first_name_input)).to_have_value(value)

    def fill_last_name(self, value: str):
        self.page.fill(loc.last_name_input, value)
        expect(self.page.locator(loc.last_name_input)).to_have_value(value)

    def fill_title(self, value: str):
        self.page.fill(loc.title_input, value)
        expect(self.page.locator(loc.title_input)).to_have_value(value)

    def select_gender(self, value: str):
        self.page.select_option(loc.gender_select, value)
        expect(self.page.locator(loc.gender_select)).to_have_value(value)

    def fill_street(self, value: str):
        self.page.fill(loc.street_input, value)
        expect(self.page.locator(loc.street_input)).to_have_value(value)

    def fill_zip(self, value: str):
        self.page.fill(loc.zip_input, value)
        expect(self.page.locator(loc.zip_input)).to_have_value(value)

    def fill_city(self, value: str):
        self.page.fill(loc.city_input, value)
        expect(self.page.locator(loc.city_input)).to_have_value(value)

    def select_country(self, value: str):
        self.page.select_option(loc.country_select, value)
        expect(self.page.locator(loc.country_select)).to_have_value(value)

    def fill_state(self, value: str):
        self.page.fill(loc.state_input, value)
        expect(self.page.locator(loc.state_input)).to_have_value(value)

    def fill_birthday(self, value: str):
        self.page.fill(loc.birthday_input, value)
        expect(self.page.locator(loc.birthday_input)).to_have_value(value)

    def set_hide_year(self, checked: bool = True):
        checkbox = self.page.locator(loc.hide_year_checkbox)
        if checkbox.is_checked() != checked:
            checkbox.check() if checked else checkbox.uncheck()
        expect(checkbox).to_be_checked() if checked else expect(checkbox).not_to_be_checked()

    def fill_about(self, value: str):
        self.page.fill(loc.about_textarea, value)
        expect(self.page.locator(loc.about_textarea)).to_have_value(value)

    def fill_phone_private(self, value: str):
        self.page.fill(loc.phone_private_input, value)
        expect(self.page.locator(loc.phone_private_input)).to_have_value(value)

    def fill_phone_work(self, value: str):
        self.page.fill(loc.phone_work_input, value)
        expect(self.page.locator(loc.phone_work_input)).to_have_value(value)

    def fill_mobile(self, value: str):
        self.page.fill(loc.mobile_input, value)
        expect(self.page.locator(loc.mobile_input)).to_have_value(value)

    def fill_fax(self, value: str):
        self.page.fill(loc.fax_input, value)
        expect(self.page.locator(loc.fax_input)).to_have_value(value)

    def fill_xmpp(self, value: str):
        self.page.fill(loc.xmpp_input, value)
        expect(self.page.locator(loc.xmpp_input)).to_have_value(value)

    def fill_website(self, value: str):
        self.page.fill(loc.website_input, value)
        expect(self.page.locator(loc.website_input)).to_have_value(value)

    def fill_facebook(self, value: str):
        self.page.fill(loc.facebook_input, value)
        expect(self.page.locator(loc.facebook_input)).to_have_value(value)

    def fill_linkedin(self, value: str):
        self.page.fill(loc.linkedin_input, value)
        expect(self.page.locator(loc.linkedin_input)).to_have_value(value)

    def fill_instagram(self, value: str):
        self.page.fill(loc.instagram_input, value)
        expect(self.page.locator(loc.instagram_input)).to_have_value(value)

    def fill_xing(self, value: str):
        self.page.fill(loc.xing_input, value)
        expect(self.page.locator(loc.xing_input)).to_have_value(value)

    def fill_youtube(self, value: str):
        self.page.fill(loc.youtube_input, value)
        expect(self.page.locator(loc.youtube_input)).to_have_value(value)

    def fill_vimeo(self, value: str):
        self.page.fill(loc.vimeo_input, value)
        expect(self.page.locator(loc.vimeo_input)).to_have_value(value)

    def fill_tiktok(self, value: str):
        self.page.fill(loc.tiktok_input, value)
        expect(self.page.locator(loc.tiktok_input)).to_have_value(value)

    def fill_twitter(self, value: str):
        self.page.fill(loc.twitter_input, value)
        expect(self.page.locator(loc.twitter_input)).to_have_value(value)

    def fill_mastodon(self, value: str):
        self.page.fill(loc.mastodon_input, value)
        expect(self.page.locator(loc.mastodon_input)).to_have_value(value)

    def fill_general(
            self,
            first_name: str,
            last_name: str,
            title: str,
            gender: str,
            street: str,
            zip_code: str,
            city: str,
            country: str,
            state: str,
            birthday: str,
            hide_year: bool,
            about: str
    ):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_title(title)
        self.select_gender(gender)
        self.fill_street(street)
        self.fill_zip(zip_code)
        self.fill_city(city)
        self.select_country(country)
        self.fill_state(state)
        self.fill_birthday(birthday)
        self.set_hide_year(hide_year)
        self.fill_about(about)

    def fill_communication(
            self,
            phone_private: str,
            phone_work: str,
            mobile: str,
            fax: str,
            xmpp: str
    ):
        self.fill_phone_private(phone_private)
        self.fill_phone_work(phone_work)
        self.fill_mobile(mobile)
        self.fill_fax(fax)
        self.fill_xmpp(xmpp)

    def fill_social(
            self,
            website: str,
            facebook: str,
            linkedin: str,
            instagram: str,
            xing: str,
            youtube: str,
            vimeo: str,
            tiktok: str,
            twitter: str,
            mastodon: str
    ):
        self.fill_website(website)
        self.fill_facebook(facebook)
        self.fill_linkedin(linkedin)
        self.fill_instagram(instagram)
        self.fill_xing(xing)
        self.fill_youtube(youtube)
        self.fill_vimeo(vimeo)
        self.fill_tiktok(tiktok)
        self.fill_twitter(twitter)
        self.fill_mastodon(mastodon)

    def save_profile(self):
        self.page.click(loc.save_button)

    def should_see_success_message(self, text: str):
        expect(self.page.locator(loc.status_message_span)).to_have_text(text)

    def should_see_first_name_error(self, text: str):
        expect(self.page.locator(loc.first_name_error)).to_have_text(text)

    def should_see_last_name_error(self, text: str):
        expect(self.page.locator(loc.last_name_error)).to_have_text(text)
