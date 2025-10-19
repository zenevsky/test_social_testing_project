import allure
import pytest

from tests.api_tests.comment.create_a_comment.create_a_comment_test_data import POSITIVE_DATA
from endpoints.comment.models.comment_object import CreateCommentPayload


@allure.feature('Comment')
@allure.story('Create a Comment')
@pytest.mark.api
class TestCreateComment:
    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Create a Comment')
    def test_create_a_comment_positive(self, create_and_delete_post_fixture, create_comment_endpoint,
                                       delete_comment_endpoint, payload):
        post_id = create_and_delete_post_fixture.data.id
        payload.objectId = post_id
        create_comment_endpoint.create_comment(payload)
        create_comment_endpoint.check_that_status_is_200()
        delete_comment_endpoint.delete_comment(create_comment_endpoint.data.id)

    @pytest.mark.high
    @allure.title('Create a Comment without auth')
    def test_create_a_new_comment_without_auth(self, create_and_delete_post_fixture, create_comment_endpoint):
        post_id = create_and_delete_post_fixture.data.id
        payload = CreateCommentPayload(objectId=post_id)
        create_comment_endpoint.create_comment(payload, headers={'Content-type': 'application/json'})
        create_comment_endpoint.check_that_status_is_401()
