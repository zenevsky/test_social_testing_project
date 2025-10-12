import allure
import pytest


@allure.feature('Post')
@allure.story('Delete A Post By ID')
@pytest.mark.api
class TestDeletePost:
    @pytest.mark.high
    @allure.title('Delete A Post By ID')
    def test_delete_a_post_by_id(self, delete_post_endpoint, create_post_fixture):
        delete_post_endpoint.delete_post(create_post_fixture.data.id)
        delete_post_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Delete A Post By ID without auth')
    def test_delete_a_post_by_id_without_auth(self, delete_post_endpoint, create_and_delete_post_fixture):
        delete_post_endpoint.delete_post(
            create_and_delete_post_fixture.data.id,
            headers={'Content-type': 'application/json'})
        delete_post_endpoint.check_that_status_is_401()

    @pytest.mark.high
    @allure.title('Check state value after deletion')
    def test_check_state_value_after_deletion(self, delete_post_endpoint, get_post_by_id_endpoint, create_post_fixture):
        delete_post_endpoint.delete_post(create_post_fixture.data.id)
        get_post_by_id_endpoint.get_post(create_post_fixture.data.id)
        get_post_by_id_endpoint.check_state_value_is(100)
