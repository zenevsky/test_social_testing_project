import re
import allure
from pages.base_page import BasePage
from pages.locators import profile_panel_locators as loc
from playwright.sync_api import expect


class ProfilePanel(BasePage):

    @allure.step("Profile panel should be visible")
    def should_see_profile_panel(self) -> None:
        expect(self.find(loc.panel_container)).to_be_visible()

    @allure.step("Profile photo should be uploaded")
    def should_see_profile_photo_uploaded(self) -> None:
        img = self.find(loc.profile_photo_img)
        expect(img).to_be_visible()
        expect(img).not_to_have_attribute("src", loc.default_avatar_src)

    @allure.step("Profile photo should be deleted")
    def should_see_profile_photo_deleted(self) -> None:
        img = self.find(loc.profile_photo_img)
        expect(img).to_have_attribute("src", loc.default_avatar_src)

    @allure.step("Banner should be uploaded")
    def should_see_banner_uploaded(self) -> None:
        img = self.find(loc.banner_image)
        expect(img).to_be_visible()
        expect(img).not_to_have_attribute("src", loc.default_banner_src)

    @allure.step("Banner should be deleted")
    def should_see_banner_deleted(self) -> None:
        img = self.find(loc.banner_image)
        expect(img).to_have_attribute("src", loc.default_banner_src)

    @allure.step("Should be on profile page of '{username}'")
    def should_be_on_profile_page(self, username: str) -> None:
        pattern = re.compile(rf"/u/{re.escape(username.lower())}/?$", re.IGNORECASE)
        expect(self.page).to_have_url(pattern)

    @allure.step("Delete confirmation modal should be visible")
    def should_see_delete_modal(self) -> None:
        expect(self.find(loc.delete_modal)).to_be_visible()

    @allure.step("Delete confirmation modal should NOT be visible")
    def should_not_see_delete_modal(self) -> None:
        expect(self.find(loc.delete_modal)).not_to_be_visible()

    @allure.step("Click username on profile panel")
    def click_username(self) -> None:
        self.find(loc.username_link).click()

    @allure.step("Click crop banner button")
    def click_crop_banner(self) -> None:
        self.find(loc.banner_crop_button).click()

    @allure.step("Hover profile photo")
    def hover_profile_photo(self) -> None:
        self.find(loc.profile_photo_container).hover()

    @allure.step("Upload profile photo: {file_path}")
    def upload_profile_photo(self, file_path: str) -> None:
        self.find(loc.photo_upload_input).set_input_files(file_path)

    @allure.step("Click crop profile photo button")
    def click_crop_photo(self) -> None:
        self.find(loc.photo_crop_button).click()

    @allure.step("Click delete profile photo")
    def click_delete_photo(self) -> None:
        self.hover_profile_photo()
        delete_btn = self.find(loc.photo_delete_button)
        expect(delete_btn).to_be_visible()
        delete_btn.click()

    @allure.step("Hover banner")
    def hover_banner(self) -> None:
        self.find(loc.banner_container).hover()

    @allure.step("Upload banner: {file_path}")
    def upload_banner(self, file_path: str) -> None:
        self.find(loc.banner_upload_input).set_input_files(file_path)

    @allure.step("Click delete banner")
    def click_delete_banner(self) -> None:
        self.find(loc.banner_delete_button).click()

    @allure.step("Click Edit Account button")
    def click_edit_account(self) -> None:
        self.find(loc.edit_account_button).click()

    @allure.step("Close delete confirmation modal")
    def click_delete_modal_close(self) -> None:
        self.find(loc.delete_modal_close_button).click()

    @allure.step("Cancel deletion in confirmation modal")
    def click_delete_modal_cancel(self) -> None:
        self.find(loc.delete_modal_cancel_button).click()

    @allure.step("Confirm deletion in confirmation modal")
    def click_delete_modal_confirm(self) -> None:
        self.find(loc.delete_modal_confirm_button).click()

    def get_username(self) -> str:
        href = self.find(loc.username_link).get_attribute("href")
        return href.strip("/").split("/")[-1]

    def get_friends_count(self) -> int:
        return int(self.find(loc.friends_count).inner_text())

    def get_followers_count(self) -> int:
        return int(self.find(loc.followers_count).inner_text())

    def get_following_count(self) -> int:
        return int(self.find(loc.following_count).inner_text())

    def get_spaces_count(self) -> int:
        return int(self.find(loc.spaces_count).inner_text())
