from selenium import webdriver

CHROME = 1
FIRE_FOX = 2


def create_driver_factory(driver_id):
    if int(driver_id) == CHROME:
        driver = webdriver.Chrome()
        return driver
    elif int(driver_id) == FIRE_FOX:
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
