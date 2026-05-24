from data import URL
from page_obgect_samokat.pages.transition_page import TransitionPage


class TestTransition:
    def test_go_to_yandex_page_successful(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.go_to_url(URL)
        assert transition_page.go_to_yandex_page

    def test_go_to_the_main_page_scooter(self, driver):
        transition_page = TransitionPage(driver)
        transition_page.go_to_url(URL)
        assert transition_page.go_to_the_main_page_scooter




