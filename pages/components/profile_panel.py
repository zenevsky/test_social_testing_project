import re

from pages.base_page import BasePage
from pages.locators import profile_panel_locators as loc
from playwright.sync_api import expect


class ProfilePanel(BasePage):

    def should_see_profile_panel(self) -> None:
        expect(self.find(loc.panel_container)).to_be_visible()

    def get_username(self) -> str:
        href = self.find(loc.username_link).get_attribute("href")
        return href.strip("/").split("/")[-1]

    def click_username(self) -> None:
        self.find(loc.username_link).click()

    def click_crop_banner(self) -> None:
        self.find(loc.banner_crop_button).click()

    def hover_profile_photo(self) -> None:
        self.find(loc.profile_photo_container).hover()

    def upload_profile_photo(self, file_path: str) -> None:
        self.find(loc.photo_upload_input).set_input_files(file_path)

    def should_see_profile_photo_uploaded(self) -> None:
        img = self.find(loc.profile_photo_img)
        expect(img).to_be_visible()
        expect(img).not_to_have_attribute("src", loc.default_avatar_src)

    def click_crop_photo(self) -> None:
        self.find(loc.photo_crop_button).click()

    def click_delete_photo(self) -> None:
        self.hover_profile_photo()
        delete_btn = self.find(loc.photo_delete_button)
        expect(delete_btn).to_be_visible()
        delete_btn.click()

    def should_see_profile_photo_deleted(self) -> None:
        img = self.find(loc.profile_photo_img)
        expect(img).to_be_visible()
        expect(img).to_have_attribute("src", loc.default_avatar_src)

    def hover_banner(self) -> None:
        self.find(loc.banner_container).hover()

    def upload_banner(self, file_path: str) -> None:
        self.find(loc.banner_upload_input).set_input_files(file_path)

    def should_see_banner_uploaded(self) -> None:
        img = self.find(loc.banner_image)
        expect(img).to_be_visible()
        expect(img).not_to_have_attribute("src", loc.default_banner_src)

    def click_delete_banner(self) -> None:
        self.find(loc.banner_delete_button).click()

    def should_see_banner_deleted(self) -> None:
        img = self.find(loc.banner_image)
        expect(img).to_be_visible()
        expect(img).to_have_attribute("src", loc.default_banner_src)

    def get_friends_count(self) -> int:
        return int(self.find(loc.friends_count).inner_text())

    def get_followers_count(self) -> int:
        return int(self.find(loc.followers_count).inner_text())

    def get_following_count(self) -> int:
        return int(self.find(loc.following_count).inner_text())

    def get_spaces_count(self) -> int:
        return int(self.find(loc.spaces_count).inner_text())

    def click_edit_account(self) -> None:
        self.find(loc.edit_account_button).click()

    def should_be_on_profile_page(self, username: str) -> None:
        expect(self.page).to_have_url(re.compile(rf"/u/{re.escape(username.lower())}/?$", re.IGNORECASE))

    def should_see_delete_modal(self) -> None:
        expect(self.find(loc.delete_modal)).to_be_visible()

    def click_delete_modal_close(self) -> None:
        self.find(loc.delete_modal_close_button).click()

    def click_delete_modal_cancel(self) -> None:
        self.find(loc.delete_modal_cancel_button).click()

    def click_delete_modal_confirm(self) -> None:
        self.find(loc.delete_modal_confirm_button).click()

    def should_not_see_delete_modal(self) -> None:
        expect(self.find(loc.delete_modal)).not_to_be_visible()
