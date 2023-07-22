from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_locator import Locator


class LoginPageLocators:

    def __init__(self):
        self.__email_input = Locator(By.CSS_SELECTOR, '#Email')
        self.__user_password_input = Locator(By.XPATH, "//input[@id='Password']")
        self.__login_button = Locator(By.CSS_SELECTOR, 'button')

    @property
    def email_input(self):
        return self.__email_input.get_locator()

    @property
    def user_password_input(self):
        return self.__user_password_input.get_locator()

    @property
    def login_button(self):
        return self.__login_button.get_locator()
