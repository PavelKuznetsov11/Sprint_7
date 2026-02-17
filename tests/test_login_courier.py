
import allure
from api_methods.courier_methods import CourierMethods
import generators
import helpers
from data import Data
import pytest

class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    def test_login_courier_success(self, login_courier):
        response_login_courier = CourierMethods.get_id_courier(login_courier)
        id_courier = response_login_courier.json()
        assert 200 == response_login_courier.status_code
        assert id_courier[Data.id]


    @allure.title('Ошибка логина курьера при невалидном логине')
    @pytest.mark.parametrize('data_out', Data.data_out_create_courier)
    def test_login_courier_invalid_login_and_password_not_received_id(self, login_courier, data_out):
        modify_login_data = generators.generate_invalid_data_courier(login_courier, data_out)
        response_login_courier = CourierMethods.get_id_courier(modify_login_data)
        id_courier = response_login_courier.json()
        assert 404 == response_login_courier.status_code
        assert Data.login_not_found in id_courier[Data.message]

    @allure.title('Ошибка логина курьера без ввода логина')
    def test_login_courier_without_login_not_received_id(self, login_courier):
        copy_data = login_courier.copy()
        modify_login_data = helpers.modify_courier_body(copy_data, Data.login)
        response_login_courier = CourierMethods.get_id_courier(modify_login_data)
        id_courier = response_login_courier.json()
        assert 400 == response_login_courier.status_code
        assert Data.insufficient_login_information in id_courier[Data.message]

    @allure.title('Ошибка логина курьера без ввода пароля')
    def test_login_courier_without_password_not_received_id(self, login_courier):
        modify_courier_data = login_courier.copy()
        modify_courier_data[Data.password] = ''
        response_login_courier = CourierMethods.get_id_courier(modify_courier_data)
        id_courier = response_login_courier.json()
        assert 400 == response_login_courier.status_code
        assert Data.insufficient_login_information in id_courier[Data.message]


