import pytest

from endpoints.post.models.post_object import PostPayload
from endpoints.comment.models.comment_object import CreateCommentPayload
from db.helpers import fetch_all
from db.queries.comment import GET_ALL_COMMENTS


@pytest.fixture()
def create_and_delete_post(create_post_endpoint, delete_post_endpoint):
    payload = PostPayload()
    create_post_endpoint.create_post(payload, 2)
    yield create_post_endpoint
    delete_post_endpoint.delete_post(create_post_endpoint.data.id)


@pytest.fixture()
def create_new_post(create_post_endpoint):
    payload = PostPayload()
    create_post_endpoint.create_post(payload, 2)
    return create_post_endpoint


@pytest.fixture()
def create_and_delete_comment(create_post_endpoint, delete_post_endpoint, create_comment_endpoint,
                              delete_comment_endpoint):
    post_payload = PostPayload()
    create_post_endpoint.create_post(post_payload, 2)
    comment_payload = CreateCommentPayload(objectId=create_post_endpoint.data.id)
    create_comment_endpoint.create_comment(comment_payload)
    yield create_comment_endpoint
    delete_comment_endpoint.delete_comment(create_comment_endpoint.data.id)
    delete_post_endpoint.delete_post(create_post_endpoint.data.id)


@pytest.fixture()
def create_new_comment(create_post_endpoint, create_comment_endpoint):
    post_payload = PostPayload()
    create_post_endpoint.create_post(post_payload, 2)
    comment_payload = CreateCommentPayload(objectId=create_post_endpoint.data.id)
    create_comment_endpoint.create_comment(comment_payload)
    return create_comment_endpoint


@pytest.fixture
def comments_from_db(mysql_connection):
    def _get_comments():
        return fetch_all(mysql_connection, GET_ALL_COMMENTS)

    return _get_comments
