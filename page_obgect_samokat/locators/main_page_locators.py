from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATORS = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATORS = By.ID, 'accordion__panel-{}'
    QUESTION_LOCATOR_TO_SCROLL = By.ID, 'accordion__heading-7'
    LOGO_YANDEX_LOCATOR = By.XPATH, '//*[@href="//ya.ru"]'
    TOP_ORDER_BUTTON = By.XPATH, '//*[@class="Button_Button__ra12g"]'
    BOTTOM_REGISTER_BUTTON = By.XPATH, '//*[@class ="Button_Button__ra12g Button_UltraBig__UU3Lp"]'
    SAMOKAT_LOGO = (By.XPATH, '//img[@alt="Scooter"]')


