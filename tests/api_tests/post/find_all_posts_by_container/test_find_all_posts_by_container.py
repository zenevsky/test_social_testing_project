import pytest
import allure


@pytest.mark.api
@allure.feature('Post')
@allure.story('Find All Posts By Container')
class TestFindAllPostsByContainer:

    @pytest.mark.high
    @allure.title('Find all posts by container successfully')
    def test_find_all_posts_by_container_successful(self, post_steps):
        post_steps.find_all_posts_by_container_successful(2)

    @pytest.mark.low
    @allure.title('404 received when requesting posts by non-existing container')
    def test_find_all_posts_by_container_non_existing(self, post_steps):
        post_steps.find_all_posts_by_container_non_existing(9999999999)

    @pytest.mark.high
    @allure.title('Fail to find all posts by container without authorization')
    def test_find_all_posts_by_container_without_auth(self, post_steps):
        post_steps.find_all_posts_by_container_without_auth(2)
