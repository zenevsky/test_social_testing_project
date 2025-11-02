from typing import List

import allure
from playwright.sync_api import Page, Locator


class BasePage:
    base_url = 'http://facetest.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open page")
    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def find_all(self, locator) -> List[Locator]:
        return self.page.locator(locator).all()
