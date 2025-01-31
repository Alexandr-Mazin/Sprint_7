import requests
import random
import string
from data import CourierUrl


class Courier:
    def __init__(self, login: str, password: str, first_name: str):
        self.login = login
        self.password = password
        self.first_name = first_name


def generate_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def register_courier() -> (requests.Response, Courier):
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(CourierUrl.main_url + CourierUrl.courier_url, json=payload)

    if response.status_code == 201:
        return response, Courier(login, password, first_name)

    return response, None


def authorize_courier(courier: Courier) -> (requests.Response, int):
    sign_in = {
        "login": courier.login,
        "password": courier.password
    }

    response = requests.post(CourierUrl.main_url + CourierUrl.login_url, json=sign_in)

    if response.status_code == 200:
        return response, response.json()["id"]

    return response, None

