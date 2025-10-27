import allure
import pytest


@pytest.mark.api
@allure.feature('Comment')
@allure.story('Find Comments By Object')
class TestFindCommentsByObject:

    @pytest.mark.high
    @allure.title('Find comments by object successfully')
    def test_find_comments_by_object_positive(self, comment_steps, create_and_delete_comment_fixture):
        params = {
            'objectId': create_and_delete_comment_fixture.data.objectId,
            'objectModel': 'humhub\modules\post\models\Post'
        }
        comment_steps.find_comments_by_object_successful(params)

    @pytest.mark.high
    @allure.title('Find comments by object without auth')
    def test_find_comments_by_object_without_auth(self, comment_steps, create_and_delete_comment_fixture):
        params = {
            'objectId': create_and_delete_comment_fixture.data.objectId,
            'objectModel': 'humhub\modules\post\models\Post'
        }
        comment_steps.find_comments_by_object_without_auth(params)
