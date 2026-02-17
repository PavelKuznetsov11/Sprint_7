
import allure
from api_methods.order_methods import OrderMethods
from data import Data

class TestListOrders:

    @allure.title('Успешное получение списка из 30 заказов')
    def test_list_orders_success(self):
        response_list_orders = OrderMethods.get_list_order()
        orders = response_list_orders.json()[Data.orders]
        assert 200 == response_list_orders.status_code
        assert orders

