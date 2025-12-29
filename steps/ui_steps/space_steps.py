import allure
from playwright.sync_api import expect

from pages.space import SpacePage
from utils.text_normalizer import strip_mentions_and_whitespace
from pages.locators import space_locators as loc

class SpaceSteps:

    def __init__(self, space_page: SpacePage):
        self.space_page = space_page

    @allure.step("Check comments from DB are displayed in UI")
    def check_comments_present(self, db_messages: list[str], timeout: int = 10000) -> None:
        comments = self.space_page.find(loc.COMMENT_MESSAGE)
        expect(comments.first).to_be_visible(timeout=timeout)

        ui_messages_raw = [el.inner_text() for el in comments.element_handles()]

        ui_messages = [strip_mentions_and_whitespace(m) for m in ui_messages_raw]
        db_messages_norm = [strip_mentions_and_whitespace(m) for m in db_messages]

        missing = []

        for db_msg in db_messages_norm:
            if not any(db_msg in ui_msg for ui_msg in ui_messages):
                missing.append(db_msg)

        assert not missing, f"Comments missing in UI: {missing}"