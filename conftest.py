import pytest

from playwright.sync_api import BrowserContext

from endpoints.post.find_all_posts import FindAllPosts

from pages.dashboard import DashboardPage


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
def find_all_posts_endpoint():
    return FindAllPosts()
