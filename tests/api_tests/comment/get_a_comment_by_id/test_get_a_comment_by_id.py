import allure
import pytest


@allure.feature('Comment')
@allure.story('Get Comment By ID')
@pytest.mark.api
class TestGetComment:
    @pytest.mark.high
    @allure.title('Get Comment By ID')
    def test_get_comment_by_id(self, get_comment_by_id_endpoint, create_and_delete_comment_fixture):
        get_comment_by_id_endpoint.get_comment(create_and_delete_comment_fixture.data.id)
        get_comment_by_id_endpoint.check_that_status_is_200()
        get_comment_by_id_endpoint.check_that_id_is_correct(create_and_delete_comment_fixture.data.id)

    @pytest.mark.high
    @allure.title('Get Comment By ID without auth')
    def test_get_comment_by_id_without_auth(self, get_comment_by_id_endpoint, create_and_delete_comment_fixture):
        get_comment_by_id_endpoint.get_comment(
            create_and_delete_comment_fixture.data.id,
            headers={'Content-type': 'application/json'})
        get_comment_by_id_endpoint.check_that_status_is_401()

    @pytest.mark.high
    @allure.title('Get Not Existing Comment')
    def test_get_not_existing_comment(self, get_comment_by_id_endpoint):
        get_comment_by_id_endpoint.get_comment(999999999999999999999)
        get_comment_by_id_endpoint.check_that_status_is_404()
