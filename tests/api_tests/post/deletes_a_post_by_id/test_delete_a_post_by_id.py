import pytest
import allure


@pytest.mark.api
@allure.feature('Post')
@allure.story('Delete A Post By ID')
class TestDeletePost:

    @pytest.mark.high
    @allure.title('Delete a post successfully')
    def test_delete_post_successful(self, post_steps, create_post_fixture):
        post_steps.delete_post_successful(create_post_fixture.data.id)

    @pytest.mark.high
    @allure.title('Unable to delete a post created by another user')
    def test_delete_post_by_another_user(self, post_steps):
        post_steps.delete_post_by_another_user(3)

    @pytest.mark.high
    @allure.title('404 error received when deleting not existing post')
    def test_delete_post_non_existing(self, post_steps):
        post_steps.delete_post_non_existing(9999999999999)

    @pytest.mark.high
    @allure.title('Fail to delete a post without authorization')
    def test_delete_post_without_auth(self, post_steps, create_and_delete_post_fixture):
        post_steps.delete_post_without_auth(create_and_delete_post_fixture.data.id)
