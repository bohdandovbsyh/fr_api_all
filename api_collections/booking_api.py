from utilities.api_utilities.base_api import BaseAPI
import allure


class BookingAPI(BaseAPI):

    def __init__(self, env):
        super().__init__(env)
        self.__booking_url = '/booking'

    @allure.step('GET BOOKING API BY ID')
    def get_booking_by_id(self, booking_id, headers=None):
        response = self.get(f'{self.__booking_url}/{booking_id}', headers=headers)
        return response

    @allure.step
    def create_booking(self, booking, headers=None):
        response = self.post(self.__booking_url, booking.get_dikt(), headers=headers)
        return response
