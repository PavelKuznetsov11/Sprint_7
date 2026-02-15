
import pytest
from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods
import generators
import helpers

@pytest.fixture
def create_courier():
    courier = []


    yield courier

    login_courier_data = helpers.modify_courier_body(courier[0], 'firstName')
    response_login_id = CourierMethods.get_id_courier(login_courier_data)
    login_id = response_login_id.json()
    assert 200 == response_login_id.status_code
    assert login_id['id']

    delete_courier = CourierMethods.delete_courier(login_id['id'])
    assert 200 == delete_courier.status_code
    assert delete_courier.json()['ok'] == True    

@pytest.fixture
def login_courier():

    create_courier_data = generators.generate_create_courier()
    response_create_courier = CourierMethods.create_courier(create_courier_data)
    login_courier_data = helpers.modify_courier_body(create_courier_data, 'firstName')
    assert 201 == response_create_courier.status_code
    assert response_create_courier.json()['ok'] == True

    yield login_courier_data
    

    response_login_id = CourierMethods.get_id_courier(login_courier_data)
    login_id = response_login_id.json()
    assert 200 == response_login_id.status_code
    assert login_id['id']

    delete_courier = CourierMethods.delete_courier(login_id['id'])
    assert 200 == delete_courier.status_code
    assert delete_courier.json()['ok'] == True  


@pytest.fixture
def delete_courier():

    create_courier_data = generators.generate_create_courier()
    response_create_courier = CourierMethods.create_courier(create_courier_data)
    login_courier_data = helpers.modify_courier_body(create_courier_data, 'firstName')
    assert 201 == response_create_courier.status_code
    assert response_create_courier.json()['ok'] == True

    response_login_courier = CourierMethods.get_id_courier(login_courier_data)
    id_courier = response_login_courier.json()
    assert 200 == response_login_courier.status_code
    assert id_courier['id']

    yield id_courier['id']    


@pytest.fixture
def create_order():
    order = [generators.generate_create_order()]

    yield order

    response_delete = OrderMethods.cancel_order(order[0])
    assert 200 == response_delete.status_code
    assert response_delete.json()['ok'] == True

@pytest.fixture
def order_by_id():
    
    order_data = generators.generate_create_order()
    response_create_order = OrderMethods.create_order(order_data)
    track = response_create_order.json()
    assert 201 == response_create_order.status_code
    assert track['track']

    yield track['track']

    response_delete = OrderMethods.cancel_order(track)
    assert 200 == response_delete.status_code
    assert response_delete.json()['ok'] == True

