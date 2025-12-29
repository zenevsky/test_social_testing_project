import pytest
import allure

from endpoints.post.models.post_object import PostPayload
from tests.api_tests.post.updates_a_post_by_id.updates_a_post_by_id_test_data import POSITIVE_DATA, NEGATIVE_DATA


@pytest.mark.api
@allure.feature('Post')
@allure.story('Updates a Post By ID')
class TestUpdatePost:

    @pytest.mark.parametrize('payload', POSITIVE_DATA)
    @pytest.mark.high
    @allure.title('Update a post successfully')
    def test_update_post_positive(self, post_steps, create_and_delete_post, payload):
        post_steps.update_post_successful(create_and_delete_post.data.id, payload)

    @pytest.mark.parametrize('payload', NEGATIVE_DATA)
    @pytest.mark.high
    @allure.title('Fail to update a post with invalid payload')
    def test_update_post_negative(self, post_steps, create_and_delete_post, payload):
        post_steps.update_post_invalid_payload(create_and_delete_post.data.id, payload)

    @pytest.mark.high
    @allure.title('Unable to update a post created by another user')
    def test_update_post_by_another_user(self, post_steps):
        payload = PostPayload()
        post_steps.update_post_by_another_user(3, payload)

    @pytest.mark.low
    @allure.title('404 received when updating non-existing post')
    def test_update_post_non_existing(self, post_steps):
        payload = PostPayload()
        post_steps.update_post_non_existing(99999999999, payload)

    @pytest.mark.high
    @allure.title('Fail to update a post without authorization')
    def test_update_post_without_auth(self, post_steps, create_and_delete_post):
        payload = PostPayload()
        post_steps.update_post_without_auth(create_and_delete_post.data.id, payload)
