import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение первой страницы заказа')
    def set_first_page_info(self, data):
        self.click_to_element(MainPageLocators.TOP_ORDER_BUTTON)
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, data['name'])
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, data['surname'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, data['address'])
        self.click_to_element(OrderPageLocators.METRO_STATION)
        self.add_text_to_element(OrderPageLocators.METRO_STATION, data['metro_station'])
        self.find_element_with_wait(OrderPageLocators.METRO_STATION_SELECT).click()
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, data['phone'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение второй страницы заказа')
    def set_second_page_info(self, data):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.click_to_element(OrderPageLocators.CURRENT_DATE)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_OPTION)
        self.click_to_element(OrderPageLocators.SCOOTER_COLOR_BLACK)
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, data['comment'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)


    def is_order_successful(self):
        # Проверка успешного создания заказа
        return self.find_element_with_wait(OrderPageLocators.STATUS_BUTTON)








