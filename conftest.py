import pytest

from playwright.sync_api import BrowserContext

from endpoints.post.find_all_posts import FindAllPosts
from endpoints.post.find_all_posts_by_container import FindAllPostsByContainer
from endpoints.post.get_post_by_id import GetPost
from endpoints.post.creates_a_new_post import CreatePost
from endpoints.post.updates_a_post_by_id import UpdatePost
from endpoints.post.upload_files_to_post_by_id import UploadFilesToPost
from endpoints.post.deletes_a_post_by_id import DeletePost

from pages.dashboard import DashboardPage

from fixtures import create_and_delete_post_fixture  # NOQA F401
from fixtures import create_post_fixture  # NOQA F401


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture()
def get_all_posts_endpoint():
    return FindAllPosts()


@pytest.fixture()
def get_all_posts_by_container_endpoint():
    return FindAllPostsByContainer()


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def get_post_by_id_endpoint():
    return GetPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def upload_files_to_post_endpoint():
    return UploadFilesToPost()
