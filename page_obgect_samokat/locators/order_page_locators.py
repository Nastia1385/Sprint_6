from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локаторы первого шага формы заказа
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_SELECT = (By.XPATH, "//div[@class='select-search__select']")
    NAME_METRO_STATION = (By.XPATH, "//input[@value='Чистые пруды']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы второго шага формы заказа
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CURRENT_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    SCOOTER_COLOR_BLACK = (By.XPATH, "//label[@for='black']")
    SCOOTER_COLOR_GREY = (By.XPATH, "//label[@for='grey']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    STATUS_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

