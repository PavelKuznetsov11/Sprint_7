
import allure
from api_methods.courier_methods import CourierMethods
import generators
import helpers
from data import Data
import pytest

class TestCreateCourier:

    @allure.title('Успешное создание id одного курьера')
    def test_create_courier_success(self, create_courier):

        create_courier_data = generators.generate_create_courier()
        response_create_courier = CourierMethods.create_courier(create_courier_data)
        assert 201 == response_create_courier.status_code
        assert response_create_courier.json()[Data.ok] == True
        
        create_courier.append(create_courier_data)


    @allure.title('Невозможно создание идентичного id курьера уже ранее созданного')
    def test_create_two_identical_courier_not_created(self, create_two_courier):

        response_create_courier_2 = CourierMethods.create_courier(create_two_courier[0])
        assert 409 == response_create_courier_2.status_code
        assert Data.login_already_use in response_create_courier_2.json()[Data.message]


    @allure.title('Невозможно создать id курьера без логина и пароля')
    @pytest.mark.parametrize('data_out', Data.data_out_create_courier)
    def test_create_courier_without_login_and_password_not_created(self, data_out):

        create_courier_data = generators.generate_create_courier()
        modify_courier_data = helpers.modify_courier_body(create_courier_data, data_out)
        response_create_courier = CourierMethods.create_courier(modify_courier_data)
        assert 400 == response_create_courier.status_code
        assert Data.not_enough_data_create_courier in response_create_courier.json()[Data.message]


