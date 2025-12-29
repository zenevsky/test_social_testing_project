import pytest
import allure


@pytest.mark.api
@allure.feature('Post')
@allure.story('Get Post By ID')
class TestGetPost:

    @pytest.mark.high
    @allure.title('Get post by ID successfully')
    def test_get_post_successful(self, post_steps, create_and_delete_post):
        post_steps.get_post_successful(create_and_delete_post.data.id)

    @pytest.mark.high
    @allure.title('Fail to get post by ID without authorization')
    def test_get_post_without_auth(self, post_steps, create_and_delete_post):
        post_steps.get_post_without_auth(create_and_delete_post.data.id)

    @pytest.mark.low
    @allure.title('Get non-existing post returns 404')
    def test_get_post_non_existing(self, post_steps):
        post_steps.get_post_non_existing(999999999999999999999)
