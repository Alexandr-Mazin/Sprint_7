import allure
from helpers import authorize_courier, Courier
from data import CourierErrors

class TestCourierAuthorize:
    @allure.description('Проверка авторизации нового курьера')
    @allure.title('Авторизация курьера')
    def test_authorize_new_courier(self, create_and_delete_user):
        response, courier = create_and_delete_user

        response_auth, courier_id = authorize_courier(courier)

        assert response_auth.status_code == 200, f"Expected status 200, but got {response_auth.status_code}"

        auth_response_json = response_auth.json()
        assert "id" in auth_response_json, "Response should contain 'id' of the authorized courier."

        assert auth_response_json['id'] == courier_id, "Authorized courier ID does not match."

    @allure.description('Проверка авторизации при указании неверного логина')
    @allure.title('Авторизация с неправильным логином')
    def test_authorize_with_invalid_login(self, create_and_delete_user):
        response, courier = create_and_delete_user

        invalid_courier = Courier(
            login="invalid_login",
            password=courier.password,
            first_name=courier.first_name
        )

        response_auth, _ = authorize_courier(invalid_courier)

        assert response_auth.status_code == 404, f"Expected status 404, but got {response_auth.status_code}"
        assert "message" in response_auth.json(), "Response should contain an error message"

    @allure.description('Проверка авторизации при указании неверного пароля')
    @allure.title('Авторизация с неправильным паролем')
    def test_authorize_with_invalid_password(self, create_and_delete_user):
        response, courier = create_and_delete_user

        invalid_courier = Courier(
            login=courier.login,
            password="invalid_password",
            first_name=courier.first_name
        )

        response_auth, _ = authorize_courier(invalid_courier)

        assert response_auth.status_code == 404, f"Expected status 404, but got {response_auth.status_code}"
        assert "message" in response_auth.json(), "Response should contain an error message"

    @allure.description('Проверка авторизации при отсутствии обязательных полей')
    @allure.title('Авторизация без полей логина или пароля')
    def test_authorize_with_missing_field(self):
        invalid_courier = Courier(
            login="",
            password="valid_password",
            first_name="Courier"
        )

        response_auth, _ = authorize_courier(invalid_courier)

        assert response_auth.status_code == 400, f"Expected status 400 for missing login, but got {response_auth.status_code}"
        assert "message" in response_auth.json(), "Response should contain an error message"
        assert response_auth.json()[
                   "message"] == CourierErrors.error_login_no_data, "Error message should indicate insufficient data for login"

        invalid_courier = Courier(
            login="valid_login",
            password="",
            first_name="Courier"
        )

        response_auth, _ = authorize_courier(invalid_courier)

        assert response_auth.status_code == 400, f"Expected status 400 for missing password, but got {response_auth.status_code}"
        assert "message" in response_auth.json(), "Response should contain an error message"
        assert response_auth.json()[
                   "message"] == CourierErrors.error_login_no_data, "Error message should indicate insufficient data for login"
