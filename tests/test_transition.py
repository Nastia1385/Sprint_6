import allure
from data import URL


@allure.title('Тесты на проверку переходов')
@allure.description('')
class TestTransition:
    def test_go_to_yandex_page_successful(self, driver, transition_page):
        transition_page.go_to_url(URL)
        assert transition_page.go_to_yandex_page

    def test_go_to_the_main_page_scooter(self, driver, transition_page):
        transition_page.go_to_url(URL)
        assert transition_page.go_to_the_main_page_scooter




