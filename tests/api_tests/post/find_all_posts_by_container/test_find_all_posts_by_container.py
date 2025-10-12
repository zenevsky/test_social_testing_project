import allure
import pytest


@allure.feature('Post')
@allure.story('Find All Posts By Container')
@pytest.mark.api
class TestFindAllPostsByContainer:

    @pytest.mark.high
    @allure.title('Find all posts by container')
    def test_find_all_posts_by_container(self, get_all_posts_by_container_endpoint):
        get_all_posts_by_container_endpoint.find_all_posts_by_container(2)
        get_all_posts_by_container_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Find all posts by container without auth')
    def test_find_all_posts_by_container_without_auth(self, get_all_posts_by_container_endpoint):
        get_all_posts_by_container_endpoint.find_all_posts_by_container(2, headers={'Content-type': 'application/json'})
        get_all_posts_by_container_endpoint.check_that_status_is_401()
