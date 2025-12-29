import pytest

from steps.api_steps.post_steps import PostSteps
from steps.api_steps.comment_steps import CommentSteps

from steps.ui_steps.edit_profile_steps import EditProfileSteps
from steps.ui_steps.space_steps import SpaceSteps


@pytest.fixture
def post_steps(
        create_post_endpoint,
        delete_post_endpoint,
        update_post_endpoint,
        get_post_by_id_endpoint,
        get_all_posts_endpoint,
        get_all_posts_by_container_endpoint,
        upload_files_to_post_endpoint
):
    return PostSteps(
        create_post_endpoint=create_post_endpoint,
        delete_post_endpoint=delete_post_endpoint,
        update_post_endpoint=update_post_endpoint,
        get_post_endpoint=get_post_by_id_endpoint,
        find_all_posts_endpoint=get_all_posts_endpoint,
        find_all_by_container_endpoint=get_all_posts_by_container_endpoint,
        upload_files_endpoint=upload_files_to_post_endpoint
    )


@pytest.fixture
def comment_steps(
        create_comment_endpoint,
        delete_comment_endpoint,
        update_comment_endpoint,
        get_comment_by_id_endpoint,
        get_comments_by_content_endpoint,
        get_comments_by_object_endpoint
):
    return CommentSteps(
        create_comment_endpoint=create_comment_endpoint,
        delete_comment_endpoint=delete_comment_endpoint,
        update_comment_endpoint=update_comment_endpoint,
        get_comment_endpoint=get_comment_by_id_endpoint,
        find_by_content_endpoint=get_comments_by_content_endpoint,
        find_by_object_endpoint=get_comments_by_object_endpoint
    )


@pytest.fixture()
def edit_profile_steps(edit_profile_page):
    return EditProfileSteps(edit_profile_page=edit_profile_page)


@pytest.fixture()
def space_steps(space_page):
    return SpaceSteps(space_page=space_page)
