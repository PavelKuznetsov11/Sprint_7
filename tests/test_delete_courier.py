
from data import Data
import allure
from api_methods.courier_methods import CourierMethods

class TestDeleteCourier:

    @allure.title('Успешное удаление id курьера')
    def test_delete_courier_success(self, delete_courier):

        response_delete_courier = CourierMethods.delete_courier(delete_courier)
        assert 200 == response_delete_courier.status_code
        assert response_delete_courier.json()[Data.ok] == True

    @allure.title('Невозможно удалить курьера без id')
    def test_delete_courier_without_id_failed(self):

        delete_courier = CourierMethods.delete_courier_without_id()
        assert 404 == delete_courier.status_code
        assert Data.not_enough_data_delete_courier in delete_courier.json()[Data.message]

    @allure.title('Невозможно удалить курьера по несуществующему id')
    def test_delete_courier_nonexistent_id_failed(self):
        delete_courier = CourierMethods.delete_courier(Data.courier_id_nonexistent)
        assert 404 == delete_courier.status_code
        assert Data.not_courier_with_id in delete_courier.json()[Data.message]


