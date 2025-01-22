import pytest
import allure
import requests
from data import CourierErrors, CourierUrl


class TestCourierCreate:
    @allure.description('Проверка создания курьера и ответа на него')
    @allure.title('Создание нового курьера')
    def test_create_new_courier(self, create_and_delete_user):
        response = create_and_delete_user[0]
        assert response.status_code == 201, f"Expected status 201, but got {response.status_code}"
        assert response.json() == {"ok": True}, f"Expected response {{'ok': True}}, but got {response.json()}"


    @allure.description('Проверка что нельзя создать двух одинаковых курьеров')
    @allure.title('Создание двух одинаковых курьеров')
    def test_create_identical_users(self, create_and_delete_user):
        response, courier = create_and_delete_user

        identical_courier_data = {
            "login": courier.login,
            "password": courier.password,
            "firstName": courier.first_name
        }

        response = requests.post(CourierUrl.main_url + CourierUrl.courier_url, data=identical_courier_data)

        assert response.status_code == 409, f"Expected status 409, but got {response.status_code}"
        assert response.json().get('message') == CourierErrors.error_create_already_exist, \
            f"Expected message '{CourierErrors.error_create_already_exist}', but got '{response.json()['message']}'"



    @pytest.mark.parametrize("missing_field, expected_error_message", [
        ("login", CourierErrors.error_create_no_data),
        ("password", CourierErrors.error_create_no_data)
    ])
    @allure.description('Проверка создания курьера с отсутствующими обязательными полями')
    @allure.title('Создание курьера с отсутствующими обязательными полями')
    def test_create_courier_missing_fields(self, missing_field, expected_error_message):
        courier_data = {
            "login": "unique_login",
            "password": "strong_password",
            "firstName": "John"
        }

        if missing_field in courier_data:
            del courier_data[missing_field]

        response = requests.post(CourierUrl.main_url + CourierUrl.courier_url, data=courier_data)

        assert response.status_code == 400, f"Expected status 400, but got {response.status_code}"
        assert response.json().get('message') == expected_error_message, \
            f"Expected message '{expected_error_message}', but got '{response.json().get('message')}'"


    @allure.description('Проверка создания курьера с существующим логином')
    @allure.title('Создание курьера с существующим логином')
    def test_create_courier_with_existing_login(self, create_and_delete_user):
        response, courier = create_and_delete_user

        identical_courier_data = {
            "login": courier.login,
            "password": "new_password",
            "firstName": "NewFirstName"
        }

        response_duplicate = requests.post(CourierUrl.main_url + CourierUrl.courier_url, data=identical_courier_data)

        assert response_duplicate.status_code == 409, f"Expected status 409, but got {response_duplicate.status_code}"
        assert response_duplicate.json().get('message') == CourierErrors.error_create_already_exist, \
            f"Expected message '{CourierErrors.error_create_already_exist}', but got '{response_duplicate.json()['message']}'"
