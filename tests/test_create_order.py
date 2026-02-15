
import pytest
from data import Data
import allure
import helpers
from api_methods.order_methods import OrderMethods

class TestCreateOrder:

    @allure.title('Успешное создание заказа с разными предпочитаемыми цветами')
    @pytest.mark.parametrize('color', Data.create_order_color)
    def test_create_order_success(self, color, create_order):

        create_order_data = helpers.modify_order_body(create_order[0], color)
        response_create_order = OrderMethods.create_order(create_order_data)
        track = response_create_order.json()
        assert 201 == response_create_order.status_code
        assert track['track']

        create_order[0] = {'track': track['track']}

