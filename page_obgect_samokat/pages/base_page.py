from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(locator).click()

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def switch_to_another_window(self, driver):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1])

    # def scroll_to_element(self, locator):
    #     # Скролл до элемента
    #     element = self.find_element_with_wait(locator)
    #     self.driver.execute_script("arguments[7].scrollIntoView();", element)

