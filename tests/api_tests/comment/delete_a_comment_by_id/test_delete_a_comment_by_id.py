import allure
import pytest


@allure.feature('Comment')
@allure.story('Delete a Comment By ID')
@pytest.mark.api
class TestDeleteComment:
    @pytest.mark.high
    @allure.title('Delete A Comment By ID')
    def test_delete_a_comment_by_id(self, delete_comment_endpoint, create_comment_fixture):
        delete_comment_endpoint.delete_comment(create_comment_fixture.data.id)
        delete_comment_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Delete A Comment By ID without auth')
    def test_delete_a_comment_by_id_without_auth(self, delete_comment_endpoint, create_and_delete_comment_fixture):
        delete_comment_endpoint.delete_comment(
            create_and_delete_comment_fixture.data.id,
            headers={'Content-type': 'application/json'})
        delete_comment_endpoint.check_that_status_is_401()
