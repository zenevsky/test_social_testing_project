import allure
import pytest

from tests.api_tests.comment.create_a_comment.create_a_comment_test_data import POSITIVE_DATA
from endpoints.comment.models.comment_object import UpdateCommentPayload


@pytest.mark.api
@allure.feature('Comment')
@allure.story('Update a Comment By ID')
class TestUpdateComment:

    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Update comment by ID successfully')
    def test_update_comment_positive(self, comment_steps, create_and_delete_comment_fixture, payload):
        comment_steps.update_comment_successful(payload, create_and_delete_comment_fixture.data.id)

    @pytest.mark.high
    @allure.title('Update comment by ID without auth')
    def test_update_comment_without_auth(self, comment_steps, create_and_delete_comment_fixture):
        payload = UpdateCommentPayload()
        comment_steps.update_comment_without_auth(payload, create_and_delete_comment_fixture.data.id)
