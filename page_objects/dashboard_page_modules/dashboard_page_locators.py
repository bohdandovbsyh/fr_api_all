from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_locator import Locator


class DashboardPageLocators:

    def __init__(self):
        self.__user_label = Locator(By.XPATH, "//a[text()='John Smith']")

    @property
    def user_label(self):
        return self.__user_label.get_locator()
