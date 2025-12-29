import allure

from constants import SUCCESS_MESSAGE, BLANK_FIRST_NAME_ERROR, BLANK_LAST_NAME_ERROR
from pages.edit_profile import EditProfilePage


class EditProfileSteps:

    def __init__(self, edit_profile_page: EditProfilePage):
        self.edit_profile_page = edit_profile_page

    @allure.step("Fill General tab and save profile")
    def fill_general_tab(self, general_data):
        self.edit_profile_page.fill_general(**general_data.__dict__)
        self.edit_profile_page.save_profile()
        self.edit_profile_page.check_that_success_message_is_visible(SUCCESS_MESSAGE)

    @allure.step("Fill Communication tab and save profile")
    def fill_communication_tab(self, comm_data):
        self.edit_profile_page.open_communication_tab()
        self.edit_profile_page.fill_communication(**comm_data.__dict__)
        self.edit_profile_page.save_profile()
        self.edit_profile_page.check_that_success_message_is_visible(SUCCESS_MESSAGE)

    @allure.step("Fill Social tab and save profile")
    def fill_social_tab(self, social_data):
        self.edit_profile_page.open_social_tab()
        self.edit_profile_page.fill_social(**social_data.__dict__)
        self.edit_profile_page.save_profile()
        self.edit_profile_page.check_that_success_message_is_visible(SUCCESS_MESSAGE)

    @allure.step("Validate required fields on General tab")
    def validate_required_fields(self):
        self.edit_profile_page.fill_first_name("")
        self.edit_profile_page.fill_last_name("")
        self.edit_profile_page.save_profile()
        self.edit_profile_page.check_that_first_name_error_is_visible(
            BLANK_FIRST_NAME_ERROR
        )
        self.edit_profile_page.check_that_last_name_error_is_visible(
            BLANK_LAST_NAME_ERROR
        )
