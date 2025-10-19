import allure
import pytest

from endpoints.comment.models.comment_object import CreateCommentPayload


@allure.feature('Comment')
@allure.story('Find Comments By Content')
@pytest.mark.api
class TestFindCommentsByContent:

    @pytest.mark.high
    @allure.title('Find comments by content')
    def test_find_comments_by_content(self, create_and_delete_post_fixture, create_comment_endpoint,
                                      get_comments_by_content_endpoint):
        comment_payload = CreateCommentPayload(objectId=create_and_delete_post_fixture.data.id)
        create_comment_endpoint.create_comment(comment_payload)
        get_comments_by_content_endpoint.find_comments_by_content(create_and_delete_post_fixture.data.content.id)
        get_comments_by_content_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Find comments by content without auth')
    def test_find_comments_by_content_without_auth(self, create_and_delete_post_fixture, create_comment_endpoint,
                                                      get_comments_by_content_endpoint):
        comment_payload = CreateCommentPayload(objectId=create_and_delete_post_fixture.data.id)
        create_comment_endpoint.create_comment(comment_payload)
        get_comments_by_content_endpoint.find_comments_by_content(create_and_delete_post_fixture.data.content.id,
                                                                  headers={'Content-type': 'application/json'})
        get_comments_by_content_endpoint.check_that_status_is_401()
