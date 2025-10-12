import allure
import pytest

from tests.api_tests.post.creates_a_new_post.create_a_new_post_test_data import POSITIVE_DATA
from endpoints.post.models.post_object import PostPayload


@allure.feature('Post')
@allure.story('Updates a Post By ID')
@pytest.mark.api
class TestUpdatePost:
    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Update a Post By ID')
    def test_update_post_positive(self, update_post_endpoint, create_and_delete_post_fixture, payload):
        update_post_endpoint.update_post(payload, create_and_delete_post_fixture.data.id)
        update_post_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Update a Post By ID without auth')
    def test_update_post_without_auth(self, update_post_endpoint, create_and_delete_post_fixture):
        payload = PostPayload()
        update_post_endpoint.update_post(
            payload,
            create_and_delete_post_fixture.data.id,
            headers={'Content-type': 'application/json'})
        update_post_endpoint.check_that_status_is_401()
