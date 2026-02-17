
from data import Data
import allure
from api_methods.order_methods import OrderMethods

class TestOrderById:

    @allure.title('Успешное получение заказа по id')
    def test_order_by_id_success(self, order_by_id):

        order_by_id_data = { Data.t : order_by_id}
        response_order_by_id = OrderMethods.get_id_order(order_by_id_data)
        order = response_order_by_id.json()[Data.order]
        assert 200 == response_order_by_id.status_code
        assert order[Data.track] == order_by_id

    @allure.title('Невозможно получить заказа по id без id')
    def test_order_by_id_without_id_invalid(self):

        response_order_by_id = OrderMethods.get_id_without_id_order()
        order = response_order_by_id.json()[Data.message]
        assert 400 == response_order_by_id.status_code
        assert Data.not_enough_data_search in order  

    @allure.title('Невозможно получить заказ по id несуществующего id')
    def test_order_by_id_nonexistent_id_invalid(self):
        
        order_by_id_data = { 't' : Data.order_id_nonexistent}
        response_order_by_id = OrderMethods.get_id_order(order_by_id_data)
        order = response_order_by_id.json()[Data.message]
        assert 404 == response_order_by_id.status_code
        assert Data.order_not_found in order  

