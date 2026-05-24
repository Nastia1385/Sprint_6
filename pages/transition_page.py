from locators.main_page_locators import MainPageLocators
from locators.transitions_locators import TransitionPageLocators
from pages.base_page import BasePage


class TransitionPage(BasePage):
    # перехода в яндекс
    def go_to_yandex_page(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX_LOCATOR)
        return self.find_element_with_wait(TransitionPageLocators.YANDEX_SEARCH_BAR)

    def go_to_the_main_page_scooter(self):
        self.click_to_element(MainPageLocators.TOP_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.SAMOKAT_LOGO)
        return self.find_element_with_wait(MainPageLocators.MAIN_SLOGAN)








