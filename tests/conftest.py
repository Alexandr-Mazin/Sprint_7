import pytest
import requests
from helpers import register_courier
from data import CourierUrl


@pytest.fixture()
def create_and_delete_user():
    response, courier = register_courier()

    yield response, courier

    sign_in = {
        "login": courier.login,
        "password": courier.password
    }

    courier_signin = requests.post(CourierUrl.main_url + CourierUrl.login_url, data=sign_in)
    courier_id = courier_signin.json()["id"]

    requests.delete(CourierUrl.main_url + CourierUrl.courier_url + str(courier_id))
