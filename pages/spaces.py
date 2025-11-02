# pages/spaces_page.py
import re
import allure
from typing import Optional
from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage
from pages.locators import spaces_locators as loc


class SpacesPage(BasePage):
    page_url = '/spaces'

    @allure.step("Get all space cards")
    def get_cards(self) -> Locator:
        return self.find(loc.card_item)

    @allure.step("Get first space card")
    def get_first_card(self) -> Locator:
        return self.get_cards().first

    @allure.step("Get first card title")
    def get_first_card_title(self) -> str:
        return self.get_first_card().locator(loc.card_title).inner_text().strip()

    @allure.step("Get first card description")
    def get_first_card_description(self) -> str:
        return self.get_first_card().locator(loc.card_details).inner_text().strip()

    @allure.step("Search for keyword: {keyword}")
    def when_search_for(self, keyword: str) -> None:
        self.page.get_by_placeholder(loc.search_input_placeholder).fill(keyword)
        self.find(loc.search_button).click()

    @allure.step("Reset filters")
    def when_reset_filters(self) -> None:
        self.find(loc.reset_filters_button).click()

    @allure.step("Click first card")
    def when_click_first_card(self) -> None:
        self.get_first_card().locator(loc.card_link).click()

    @allure.step("Click first card (with navigation)")
    def when_click_first_card_with_navigation(self) -> None:
        first_card = self.find(loc.card_item).first
        link = first_card.locator("a.card-space-link >> .card-title").first
        with self.page.expect_navigation():
            link.click()

    @allure.step("Sort by option: {sort_option}")
    def when_sort_by(self, sort_option: str) -> None:
        self.find(loc.sort_select).select_option(sort_option)

    @allure.step("Filter by status: {status_value}")
    def when_filter_by_status(self, status_value: str) -> None:
        self.find(loc.status_select).select_option(status_value)

    @allure.step("Check 'Spaces' tab is active")
    def should_have_active_spaces_tab(self) -> None:
        tab = self.find(loc.spaces_tab_header)
        expect(tab).to_have_class("active")

    @allure.step("Check at least one card exists")
    def should_have_at_least_one_card(self) -> None:
        self.page.wait_for_selector(loc.card_item)
        count = self.get_cards().count()
        assert count > 0, f'Expected at least one card, but found {count}.'

    @allure.step("Check sort and status dropdowns are visible")
    def should_show_sort_and_status_dropdowns_visible(self) -> None:
        expect(self.find(loc.sort_select)).to_be_visible()
        expect(self.find(loc.status_select)).to_be_visible()

    @allure.step("Search results should contain: {substring}")
    def should_return_search_results_containing(self, substring: str) -> None:
        self.page.wait_for_selector(loc.card_item)
        cards_count = self.get_cards().count()
        assert cards_count > 0, f'Search returned no cards when expecting at least one for "{substring}"'
        title = self.get_first_card_title()
        assert substring in title, f'Expected first result title to contain "{substring}", got "{title}"'

    @allure.step("Filters reset should restore list of cards")
    def should_reset_filters_restore_cards(self) -> None:
        self.page.wait_for_selector(loc.card_item)
        count = self.get_cards().count()
        assert count > 0, f'After reset filters expected some cards, but found {count}.'

    @allure.step("Should navigate to a space page")
    def should_navigate_to_space(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/s/.*"))

    @allure.step("Validate first card title and description")
    def should_have_first_card_title_and_description(
            self,
            expected_title: Optional[str] = None,
            expected_description_substring: Optional[str] = None
    ) -> None:

        self.should_have_at_least_one_card()

        if expected_title is not None:
            actual = self.get_first_card_title()
            assert actual == expected_title, f'Expected first card title "{expected_title}", got "{actual}"'

        if expected_description_substring is not None:
            actual_desc = self.get_first_card_description()
            assert expected_description_substring in actual_desc, (
                f'Expected description to contain "{expected_description_substring}", got "{actual_desc}"'
            )

    @allure.step("Validate cards are sorted by title (ascending={ascending})")
    def should_cards_ordered_by_title(self, ascending: bool = True) -> None:
        self.page.wait_for_selector(loc.card_item)
        titles = [
            self.get_cards().nth(i).locator(loc.card_title).inner_text().strip()
            for i in range(self.get_cards().count())
        ]
        sorted_titles = sorted(titles)
        if not ascending:
            sorted_titles = list(reversed(sorted_titles))

        assert titles == sorted_titles, f"Cards are not sorted by title: {titles}"

    @allure.step("Check that no cards are found")
    def should_no_cards_found(self) -> None:
        count = self.get_cards().count()
        assert count == 0, f'Expected no cards, but found {count}'
