import allure
import pytest


@allure.feature('Spaces Page')
@allure.story('Spaces UI and behavior')
@pytest.mark.ui
class TestSpacesPage:

    @pytest.mark.medium
    @allure.title("Page shows at least one space card")
    def test_page_shows_at_least_one_space_card(self, spaces_page):
        spaces_page.open_page()
        spaces_page.should_have_active_spaces_tab()
        spaces_page.should_have_at_least_one_card()

    @pytest.mark.medium
    @allure.title("Search filters spaces by a keyword")
    def test_search_filters_spaces_by_keyword(self, spaces_page):
        spaces_page.open_page()
        spaces_page.when_search_for("Добро")
        spaces_page.should_return_search_results_containing("Добро")

    @pytest.mark.low
    @allure.title("Sort and status dropdowns are visible")
    def test_sort_and_status_dropdowns_are_visible(self, spaces_page):
        spaces_page.open_page()
        spaces_page.should_show_sort_and_status_dropdowns_visible()

    @pytest.mark.medium
    @allure.title("Clicking first card opens the space page")
    def test_clicking_first_card_opens_space(self, spaces_page):
        spaces_page.open_page()
        spaces_page.when_click_first_card_with_navigation()
        spaces_page.should_navigate_to_space()

    @pytest.mark.low
    @allure.title("First card has expected title and description")
    def test_first_card_title_and_description(self, spaces_page):
        spaces_page.open_page()
        spaces_page.should_have_first_card_title_and_description(
            expected_title="Добро пожаловать в сообщество",
            expected_description_substring="знакомства с платформой"
        )

    @pytest.mark.medium
    @allure.title("Sorting by name orders the cards alphabetically")
    def test_sorting_by_name_orders_cards(self, spaces_page):
        spaces_page.open_page()
        spaces_page.when_sort_by('name')
        spaces_page.should_cards_ordered_by_title(ascending=True)

    @pytest.mark.medium
    @allure.title("Search for unknown keyword returns no results")
    def test_search_returns_no_results_for_unknown_keyword(self, spaces_page):
        spaces_page.open_page()
        spaces_page.when_search_for('qwertyuiopasdfgh')
        spaces_page.should_no_cards_found()

    @pytest.mark.parametrize("status_value", ["none", ""])
    @allure.title("Filter spaces by status with results")
    def test_filter_by_status_with_results_for_unauthorized_user(self, spaces_page, status_value):
        spaces_page.open_page()
        spaces_page.when_filter_by_status(status_value)
        spaces_page.should_have_at_least_one_card()

    @pytest.mark.parametrize("status_value", ["member", "follow", "archived"])
    @allure.title("Filter spaces by status with no results")
    def test_filter_by_status_no_results_for_unauthorized_user(self, spaces_page, status_value):
        spaces_page.open_page()
        spaces_page.when_filter_by_status(status_value)
        spaces_page.should_no_cards_found()
