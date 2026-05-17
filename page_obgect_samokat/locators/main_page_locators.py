from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATORS = By.ID, 'id="accordion__heading-{}"'
    ANSWER_LOCATORS = By.ID, 'id="accordion__panel-{}"'
    QUESTION_LOCATORS_TO_SCROLL = By.ID, 'id="accordion__heading-7"'
    LOGO_YANDEX_LOCATOR = By.XPATH, '//*[@href="//ya.ru"]'

