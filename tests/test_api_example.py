from http import HTTPStatus

import allure

from api_collections.booking_api import BookingAPI
from api_collections.data_classes.booking_data import Booking


@allure.feature('API tests')
def test_status_code_200(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.get_booking_by_id(booking_id=1)
    actual_booking = Booking(**response.json())
    assert response.status_code == HTTPStatus.OK
    assert create_mock_booking.get_dikt() == actual_booking.get_dikt()


@allure.feature('API tests')
def test_create_booking(env, create_mock_booking):
    booking_api = BookingAPI(env)
    response = booking_api.create_booking(create_mock_booking)
