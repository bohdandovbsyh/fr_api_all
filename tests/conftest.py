import json
from contextlib import suppress

import allure
import pytest

from api_collections.booking_api import BookingAPI
from api_collections.data_classes.booking_data import Booking
from utilities.config_obj import ConfigObject
from utilities.driver_factory import create_driver_factory


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_html_report_title(report):
    report.title = "Hillel IT school Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>HILLEL: LESSON20</p>"])


@pytest.fixture(scope='session', autouse=True)
def env(request):
    # env_name = request.config.getoption('--env')
    with open('/home/bohdandovbysh/PycharmProjects/selenium_example_quick/configurations/env_1.json') as file:
        f_data = file.read()
    json_data = json.loads(f_data)
    return ConfigObject(**json_data)


@pytest.fixture()
def open_login_page(env, request):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def create_mock_booking(env):
    mock_data = BookingAPI(env).get_booking_by_id(1)  # DataBase request
    booking = Booking(**mock_data.json())
    return booking
