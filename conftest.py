
import pytest
from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods
import generators
import helpers
from data import Data

@pytest.fixture
def create_courier():
    courier = []


    yield courier

    login_courier_data = helpers.modify_courier_body(courier[0], 'firstName')
    response_login_id = CourierMethods.get_id_courier(login_courier_data)
    login_id = response_login_id.json()


    CourierMethods.delete_courier(login_id[Data.id])


@pytest.fixture
def create_two_courier(create_courier):
    create_courier_data = generators.generate_create_courier()
    CourierMethods.create_courier(create_courier_data)
    create_courier.append(create_courier_data)
    return create_courier


@pytest.fixture
def login_courier():

    create_courier_data = generators.generate_create_courier()
    CourierMethods.create_courier(create_courier_data)
    login_courier_data = helpers.modify_courier_body(create_courier_data, Data.firstName)


    yield login_courier_data
    

    response_login_id = CourierMethods.get_id_courier(login_courier_data)
    login_id = response_login_id.json()


    CourierMethods.delete_courier(login_id[Data.id])



@pytest.fixture
def delete_courier():

    create_courier_data = generators.generate_create_courier()
    CourierMethods.create_courier(create_courier_data)
    login_courier_data = helpers.modify_courier_body(create_courier_data, Data.firstName)


    response_login_courier = CourierMethods.get_id_courier(login_courier_data)
    id_courier = response_login_courier.json()


    return id_courier[Data.id]    


@pytest.fixture
def create_order():
    order = [generators.generate_create_order()]

    yield order

    OrderMethods.cancel_order(order[0])

@pytest.fixture
def order_by_id():
    
    order_data = generators.generate_create_order()
    response_create_order = OrderMethods.create_order(order_data)
    track = response_create_order.json()

    yield track[Data.track]

    OrderMethods.cancel_order(track)

