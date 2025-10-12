import allure
import pytest


@allure.feature('Post')
@allure.story('Find All Posts')
@pytest.mark.api
class TestFindAllPosts:

    @pytest.mark.high
    @allure.title('Find all posts with auth')
    def test_find_all_posts(self, get_all_posts_endpoint):
        get_all_posts_endpoint.find_all_posts()
        get_all_posts_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Find all posts without auth')
    def test_find_all_posts_without_auth(self, get_all_posts_endpoint):
        get_all_posts_endpoint.find_all_posts(headers={'Content-type': 'application/json'})
        get_all_posts_endpoint.check_that_status_is_401()
