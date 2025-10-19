import allure
import pytest

from tests.api_tests.comment.create_a_comment.create_a_comment_test_data import POSITIVE_DATA
from endpoints.comment.models.comment_object import UpdateCommentPayload


@allure.feature('Comment')
@allure.story('Update a Comment By ID')
@pytest.mark.api
class TestUpdateComment:
    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Update a Comment By ID')
    def test_update_a_comment_positive(self, create_and_delete_comment_fixture, update_comment_endpoint, payload):
        update_comment_endpoint.update_comment(payload, create_and_delete_comment_fixture.data.id)
        update_comment_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Update a Comment without auth')
    def test_update_comment_without_auth(self, create_and_delete_comment_fixture, update_comment_endpoint):
        payload = UpdateCommentPayload()
        update_comment_endpoint.update_comment(payload, create_and_delete_comment_fixture.data.id, headers={'Content-type': 'application/json'})
        update_comment_endpoint.check_that_status_is_401()
