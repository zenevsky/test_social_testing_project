import allure
import pytest


@pytest.mark.api
@allure.feature('Comment')
@allure.story('Get Comment By ID')
class TestGetComment:

    @pytest.mark.high
    @allure.title('Get comment by ID successfully')
    def test_get_comment_by_id_positive(self, comment_steps, create_and_delete_comment):
        comment_steps.get_comment_successful(create_and_delete_comment.data.id)

    @pytest.mark.high
    @allure.title('Get comment by ID without auth')
    def test_get_comment_by_id_without_auth(self, comment_steps, create_and_delete_comment):
        comment_steps.get_comment_without_auth(create_and_delete_comment.data.id)

    @pytest.mark.high
    @allure.title('Get not existing comment')
    def test_get_not_existing_comment(self, comment_steps):
        comment_steps.get_not_existing_comment()
