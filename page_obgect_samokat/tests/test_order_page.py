import pytest

from data import ORDER_DATA_1, ORDER_DATA_2, URL
from page_obgect_samokat.locators.main_page_locators import MainPageLocators
from page_obgect_samokat.locators.order_page_locators import OrderPageLocators
from page_obgect_samokat.pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.TOP_ORDER_BUTTON, ORDER_DATA_1),
            (MainPageLocators.BOTTOM_REGISTER_BUTTON, ORDER_DATA_2)
        ]
    )
    def test_create_order(self, driver,locator, order_data):
        order_page = OrderPage(driver)
        order_page.go_to_url(URL)
        order_page.set_first_page_info(order_data)
        order_page.set_second_page_info(order_data)
        assert order_page.is_order_successful()







