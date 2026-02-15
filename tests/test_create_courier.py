
import allure
from api_methods.courier_methods import CourierMethods
import generators
import helpers

class TestCreateCourier:

    @allure.title('Успешное создание id одного курьера')
    def test_create_courier_success(self, create_courier):

        create_courier_data = generators.generate_create_courier()
        response_create_courier = CourierMethods.create_courier(create_courier_data)
        assert 201 == response_create_courier.status_code
        assert response_create_courier.json()['ok'] == True
        
        create_courier.append(create_courier_data)


    @allure.title('Невозможно создание идентичного id курьера уже ранее созданного')
    def test_create_two_identical_courier_not_created(self, create_courier):

        create_courier_data = generators.generate_create_courier()
        response_create_courier = CourierMethods.create_courier(create_courier_data)
        assert 201 == response_create_courier.status_code
        assert response_create_courier.json()['ok'] == True
        response_create_courier_2 = CourierMethods.create_courier(create_courier_data)
        assert 409 == response_create_courier_2.status_code
        assert 'Этот логин уже используется' in response_create_courier_2.json()['message']

        create_courier.append(create_courier_data)

    @allure.title('Невозможно создать id курьера без логина')
    def test_create_courier_without_login_not_created(self):

        create_courier_data = generators.generate_create_courier()
        modify_courier_data = helpers.modify_courier_body(create_courier_data, 'login')
        response_create_courier = CourierMethods.create_courier(modify_courier_data)
        assert 400 == response_create_courier.status_code
        assert "Недостаточно данных для создания учетной записи" in response_create_courier.json()['message']


    @allure.title('Невозможно создать id курьера без пароля')
    def test_create_courier_without_password_not_created(self):

        create_courier_data = generators.generate_create_courier()
        modify_courier_data = helpers.modify_courier_body(create_courier_data, 'password')
        response_create_courier = CourierMethods.create_courier(modify_courier_data)
        assert 400 == response_create_courier.status_code
        assert "Недостаточно данных для создания учетной записи" in response_create_courier.json()['message']



