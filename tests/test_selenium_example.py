import allure

from page_objects.login_page_modules.login_page import LoginPage


# @allure.description('ID175: test to login to main page')
# @allure.epic('Epic-747: https://github.com/bohdandovbsyh/pet_automation_project/blob/master/test_cases/conftest.py')
# @allure.feature('Login page')
# def test_login(open_login_page, env):
#     user_name, password = env.login, env.password
#     driver = open_login_page
#     dashboard_page = LoginPage(driver).set_email(user_name).set_password(password).click_login()
#     assert dashboard_page.is_user_label_displayed(), 'User label is not displayed'


@allure.feature('Login page math calculation')
def test_01():
    from random import randint
    int_r = randint(1, 5)
    assert 1 == int_r
