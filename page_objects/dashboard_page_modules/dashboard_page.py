import allure

from page_objects.dashboard_page_modules.dashboard_page_locators import DashboardPageLocators
from utilities.ui_utilities.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__dashboard_locators = DashboardPageLocators()

    @allure.step
    def is_user_label_displayed(self):
        return self.is_displayed(self.__dashboard_locators.user_label)
