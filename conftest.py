import pytest
from selenium import webdriver
from page_obgect_samokat.pages.main_page import MainPage
from page_obgect_samokat.pages.order_page import OrderPage


@pytest.fixture(scope="function")
def driver():
    # Фикстура для инициализации и закрытия браузера Firefox
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.timeout = 10
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.timeout = 10
    return page

