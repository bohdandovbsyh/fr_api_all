from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    def __wait_until_element_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, value, is_clear=True):
        element = self.__wait_until_element_visible(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def is_displayed(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator)).is_displayed()

    def add_cookies(self, name, value):
        """Add cookies in format: {'name' : 'foo', 'value' : 'bar'}"""
        self._driver.add_cookie({'name': name, 'value': value})

    def add_data_to_local_storage(self, key, value):
        self._driver.execute_script(f"window.localStorage['{key}'] = '{value}'")

    def click_via_js(self, locator):
        element = self.__wait_until_element_clickable(locator)
        self._driver.execute_script('arguments[0].click()', element)

    def scroll_to_element(self, locator):
        retries = 15
        while retries:
            try:
                element = self.__wait_until_element_visible(locator)
                return element
            except ElementNotVisibleException:
                self._driver.execute_script('window.scrollTo(100, 100)')
                retries -= 1

    def get_text(self, locator):
        element = self.__wait_until_element_visible(locator)
        return element.text
