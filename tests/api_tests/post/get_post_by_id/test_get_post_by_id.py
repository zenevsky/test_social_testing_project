import allure
import pytest


@allure.feature('Post')
@allure.story('Get Post By ID')
@pytest.mark.api
class TestGetPost:
    @pytest.mark.high
    @allure.title('Get Post By ID')
    def test_get_post_by_id(self, get_post_by_id_endpoint, create_and_delete_post_fixture):
        get_post_by_id_endpoint.get_post(create_and_delete_post_fixture.data.id)
        get_post_by_id_endpoint.check_that_status_is_200()
        get_post_by_id_endpoint.check_that_id_is_correct(create_and_delete_post_fixture.data.id)

    @pytest.mark.high
    @allure.title('Get Post By ID without auth')
    def test_get_post_by_id_without_auth(self, get_post_by_id_endpoint, create_and_delete_post_fixture):
        get_post_by_id_endpoint.get_post(
            create_and_delete_post_fixture.data.id,
            headers={'Content-type': 'application/json'})
        get_post_by_id_endpoint.check_that_status_is_401()

    @pytest.mark.high
    @allure.title('Get Not Existing Post')
    def test_get_not_existing_post(self, get_post_by_id_endpoint):
        get_post_by_id_endpoint.get_post(999999999999999999999)
        get_post_by_id_endpoint.check_that_status_is_404()
