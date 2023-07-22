class Locator:

    def __init__(self, method, locator_str):
        self.__method = method
        self.__locator_str = locator_str

    def get_locator(self):
        return self.__method, self.__locator_str
