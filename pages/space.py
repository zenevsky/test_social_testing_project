import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import space_locators as loc
from utils.text_normalizer import strip_mentions_and_whitespace


class SpacePage(BasePage):

    @allure.step("Check space page is opened")
    def check_that_space_page_is_opened(self) -> None:
        expect(self.find(loc.SPACE_TITLE)).to_be_visible()
        expect(self.find(loc.STREAM_CONTAINER)).to_be_visible()

    @allure.step("Check space title is '{expected_title}'")
    def check_that_space_title_is(self, expected_title: str) -> None:
        expect(self.find(loc.SPACE_TITLE)).to_have_text(expected_title)

    @allure.step("Check space description is visible")
    def check_that_space_description_is_visible(self) -> None:
        expect(self.find(loc.SPACE_DESCRIPTION)).to_be_visible()

    @allure.step("Check posts count is greater than zero")
    def check_that_posts_count_is_not_zero(self) -> None:
        expect(self.find(loc.POSTS_COUNT)).not_to_have_text("0")

    @allure.step("Check members count is '{expected_count}'")
    def check_that_members_count_is(self, expected_count: str) -> None:
        expect(self.find(loc.MEMBERS_COUNT)).to_have_text(expected_count)

    @allure.step("Click invite button")
    def open_invite_members_modal(self) -> None:
        self.find(loc.INVITE_BUTTON).click()

    @allure.step("Open space settings dropdown")
    def open_space_settings(self) -> None:
        self.find(loc.SPACE_SETTINGS_DROPDOWN).click()

    @allure.step("Create post with text '{text}'")
    def create_post(self, text: str) -> None:
        self.find(loc.POST_TAB).click()
        expect(self.find(loc.POST_EDITOR)).to_be_visible()

        self.find(loc.POST_TEXTAREA).fill(text)
        self.find(loc.POST_SUBMIT_BUTTON).click()

    @allure.step("Check that post is created")
    def check_that_post_is_created(self) -> None:
        expect(self.find(loc.POST_ITEM).first).to_be_visible()

    @allure.step("Check stream is not empty")
    def check_that_stream_is_not_empty(self) -> None:
        expect(self.find(loc.STREAM_EMPTY_PLACEHOLDER)).not_to_be_visible()

    @allure.step("Open stream filter")
    def open_stream_filter(self) -> None:
        self.find(loc.FILTER_BUTTON).click()
        expect(self.find(loc.FILTER_PANEL)).to_be_visible()

    @allure.step("Check members panel is visible")
    def check_that_members_panel_is_visible(self) -> None:
        expect(self.find(loc.MEMBERS_PANEL)).to_be_visible()

    @allure.step("Get all comment messages from UI")
    def get_messages(self) -> list[str]:
        return [
            el.inner_text().strip()
            for el in self.find_all(".comment-message")
        ]
