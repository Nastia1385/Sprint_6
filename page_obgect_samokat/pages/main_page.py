from page_obgect_samokat.locators.main_page_locators import MainPageLocators
from page_obgect_samokat.pages.base_page import BasePage


class MainPage(BasePage):

    # @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formated = self.format_locators(MainPageLocators.QUESTION_LOCATORS, num)
        # self.scroll_to_element(MainPageLocators.QUESTION_LOCATORS_TO_SCROLL)
        self.click_to_element(locator_q_formated)

    # @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formated = self.format_locators(
            MainPageLocators.ANSWER_LOCATORS, num)
        return self.get_text_from_element(locator_a_formated)

    def check_question_and_answer(self, num):
        self.click_to_question(num)
        self.get_answer_text(num)

    # @allure.step('Проверка ответа')
    def check_answer(self, num, my_text):
        self.click_to_question(num)
        text = self.get_answer_text(num)
        return text == my_text

    def click_to_logo(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX_LOCATOR)



