import requests
import allure
from data import OrdersUrl


class TestGetOrdersList:

    @allure.description("Получаем список заказов")
    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(
            OrdersUrl.main_url + OrdersUrl.main_orders_url
        )

        assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

        orders_list = response.json().get("orders", [])

        assert isinstance(orders_list, list), "'orders' should be a list"
