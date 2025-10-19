import allure
import pytest


@allure.feature('Comment')
@allure.story('Find Comments By Object')
@pytest.mark.api
class TestFindCommentsByObject:

    @pytest.mark.high
    @allure.title('Find comments by object')
    def test_find_comments_by_object(self, create_and_delete_comment_fixture, get_comments_by_object_endpoint):
        get_comments_by_object_endpoint.find_comments_by_object(
            params={
                'objectId': create_and_delete_comment_fixture.data.objectId,
                'objectModel': 'humhub\modules\post\models\Post'
            }
        )
        get_comments_by_object_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Find comments by content without auth')
    def test_find_comments_by_object_without_auth(self, create_and_delete_comment_fixture,
                                                  get_comments_by_object_endpoint):
        get_comments_by_object_endpoint.find_comments_by_object(
            params={
                'objectId': create_and_delete_comment_fixture.data.objectId,
                'objectModel': 'humhub\modules\post\models\Post'
            },
            headers={'Content-type': 'application/json'}
        )

        get_comments_by_object_endpoint.check_that_status_is_401()
