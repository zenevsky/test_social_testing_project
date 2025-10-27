import allure
import pytest

from tests.api_tests.post.creates_a_new_post.create_a_new_post_test_data import POSITIVE_DATA, NEGATIVE_DATA
from endpoints.post.models.post_object import PostPayload


@pytest.mark.api
@allure.feature('Post')
@allure.story('Create A New Post')
class TestCreatePost:

    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Create a new post successfully')
    def test_create_post_positive(self, post_steps, payload):
        post = post_steps.create_post_successful(payload)
        post_steps.delete_post_successful(post.id)

    @pytest.mark.parametrize('payload', NEGATIVE_DATA)
    @pytest.mark.high
    @allure.title('Fail to create a new post with invalid payload')
    def test_create_post_negative(self, post_steps, payload):
        post_steps.create_post_invalid_payload(payload)

    @pytest.mark.high
    @allure.title('Fail to create a new post without authorization')
    def test_create_post_without_auth(self, post_steps):
        payload = PostPayload()
        post_steps.create_post_without_auth(payload)

