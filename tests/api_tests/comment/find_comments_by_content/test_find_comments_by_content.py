import allure
import pytest
from endpoints.comment.models.comment_object import CreateCommentPayload


@pytest.mark.api
@allure.feature('Comment')
@allure.story('Find Comments By Content')
class TestFindCommentsByContent:

    @pytest.mark.high
    @allure.title('Find comments by content successfully')
    def test_find_comments_by_content_positive(self, comment_steps, create_and_delete_post_fixture):
        payload = CreateCommentPayload(objectId=create_and_delete_post_fixture.data.id)
        comment_steps.create_comment_successful(payload)
        comment_steps.find_comments_by_content_successful(create_and_delete_post_fixture.data.content.id)

    @pytest.mark.high
    @allure.title('Find comments by content without auth')
    def test_find_comments_by_content_without_auth(self, comment_steps, create_and_delete_post_fixture):
        payload = CreateCommentPayload(objectId=create_and_delete_post_fixture.data.id)
        comment_steps.create_comment_successful(payload)
        comment_steps.find_comments_by_content_without_auth(create_and_delete_post_fixture.data.content.id)
