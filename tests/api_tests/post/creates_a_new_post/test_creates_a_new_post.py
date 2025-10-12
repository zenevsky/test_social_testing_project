import allure
import pytest

from tests.api_tests.post.creates_a_new_post.create_a_new_post_test_data import POSITIVE_DATA
from endpoints.post.models.post_object import PostPayload


@allure.feature('Post')
@allure.story('Create A New Post')
@pytest.mark.api
class TestCreatePost:
    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Create A New Post')
    def test_create_a_new_post_positive(self, create_post_endpoint, delete_post_endpoint, payload):
        create_post_endpoint.create_post(payload, 2)
        create_post_endpoint.check_that_status_is_200()
        delete_post_endpoint.delete_post(create_post_endpoint.data.id)

    @pytest.mark.high
    @allure.title('Create A New Post without auth')
    def test_create_a_new_post_without_auth(self, create_post_endpoint):
        payload = PostPayload()
        create_post_endpoint.create_post(payload, 2, headers={'Content-type': 'application/json'})
        create_post_endpoint.check_that_status_is_401()
