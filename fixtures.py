import pytest

from endpoints.post.models.post_object import PostPayload


@pytest.fixture()
def create_and_delete_post_fixture(create_post_endpoint, delete_post_endpoint):
    payload = PostPayload()
    create_post_endpoint.create_post(payload, 2)
    yield create_post_endpoint
    delete_post_endpoint.delete_post(create_post_endpoint.data.id)


@pytest.fixture()
def create_post_fixture(create_post_endpoint):
    payload = PostPayload()
    create_post_endpoint.create_post(payload, 2)
    return create_post_endpoint
