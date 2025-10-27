import allure
import pytest

from tests.api_tests.comment.create_a_comment.create_a_comment_test_data import POSITIVE_DATA
from endpoints.comment.models.comment_object import CreateCommentPayload


@pytest.mark.api
@allure.feature('Comment')
@allure.story('Create a Comment')
class TestCreateComment:

    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Create a Comment successfully')
    def test_create_comment_positive(self, comment_steps, create_and_delete_post_fixture, payload):
        payload.objectId = create_and_delete_post_fixture.data.id
        comment = comment_steps.create_comment_successful(payload)
        comment_steps.delete_comment_successful(comment.id)

    @pytest.mark.high
    @allure.title('Create a Comment without auth')
    def test_create_comment_without_auth(self, comment_steps, create_and_delete_post_fixture):
        payload = CreateCommentPayload(objectId=create_and_delete_post_fixture.data.id)
        comment_steps.create_comment_without_auth(payload)
