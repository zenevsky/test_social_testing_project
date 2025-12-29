import allure
import pytest


@pytest.mark.api
@allure.feature('Comment')
@allure.story('Delete a Comment')
class TestDeleteComment:

    @pytest.mark.high
    @allure.title('Delete a Comment successfully')
    def test_delete_comment_positive(self, comment_steps, create_new_comment):
        comment_steps.delete_comment_successful(create_new_comment.data.id)

    @pytest.mark.high
    @allure.title('Delete a Comment without auth')
    def test_delete_comment_without_auth(self, comment_steps, create_and_delete_comment):
        comment_steps.delete_comment_without_auth(create_and_delete_comment.data.id)
