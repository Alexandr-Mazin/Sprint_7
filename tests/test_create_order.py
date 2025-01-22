import json
import requests
import pytest
import allure
from data import DataOrdered, OrdersUrl

class TestCreateOrder:

    @allure.description('Создаем заказ с разными вариантами цвета')
    @allure.title('Создание заказа')
    @pytest.mark.parametrize('order_data', [
        DataOrdered.order_color_black,
        DataOrdered.order_color_grey,
        DataOrdered.order_color_black_and_grey,
        DataOrdered.order_no_color
    ])
    def test_order_creation_with_different_colors_success(self, order_data):
        payload = json.dumps(order_data)
        response = requests.post(OrdersUrl.main_url + OrdersUrl.main_orders_url, data=payload)

        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

        response_json = response.json()
        assert 'track' in response_json, "'track' key not found in response"
