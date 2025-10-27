import pytest
import allure


@pytest.mark.api
@allure.feature('Post')
@allure.story('Find All Posts')
class TestFindAllPosts:

    @pytest.mark.high
    @allure.title('Find all posts successfully')
    def test_find_all_posts_successful(self, post_steps):
        post_steps.find_all_posts_successful()

    @pytest.mark.high
    @allure.title('Fail to find all posts without authorization')
    def test_find_all_posts_without_auth(self, post_steps):
        post_steps.find_all_posts_without_auth()
