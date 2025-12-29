import time

import allure
import pytest


@allure.feature('Space Page')
@allure.story('Space UI and behavior')
@pytest.mark.ui
@pytest.mark.db
class TestSpacePage:

    @allure.title("All comments from DB are displayed on space page")
    def test_space_comments_match_db(self, space_page, dashboard_page, login_modal, comments_from_db, spaces_page,
                                     space_steps):
        dashboard_page.open_page()
        login_modal.login_as("yellowlatesummer@gmail.com", "20039915aAa")
        spaces_page.open_page()
        spaces_page.click_first_card_with_navigation()

        db_comments = comments_from_db()
        db_messages = [row["message"] for row in db_comments]

        space_page.check_that_space_page_is_opened()
        space_steps.check_comments_present(db_messages)
