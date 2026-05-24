import allure
import pytest

from data import URL, answers_data


@allure.title('Тесты на проверку вопросов')
@allure.description('')
class TestMainPage:

    @pytest.mark.parametrize(
        'num',
        [0,1, 2, 3, 4, 5, 6, 7]
    )
    def test_questions_and_answers(self, num, main_page):
        main_page.go_to_url(URL)
        assert (main_page.check_answer(num, answers_data[num]))

