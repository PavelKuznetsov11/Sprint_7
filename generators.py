
from faker import Faker
import allure 

fake = Faker()

@allure.step('Генерируем одного курьера')
def generate_create_courier():
    create_courier = {
    'login': fake.pystr(min_chars=10, max_chars=20),
    'password': fake.password(length=15),
    'firstName': fake.first_name()
    }
    return create_courier

@allure.step('Генерируем один заказ')
def generate_create_order():
    create_order = {
        'firstName': fake.first_name(), 
        'lastName': fake.last_name(), 
        'address' : fake.address(),
        'metroStation' : str(fake.pyint(min_value=1, max_value=50)), 
        'phone' : fake.phone_number(), 
        'rentTime' : fake.pyint(min_value=1, max_value=10), 
        'deliveryDate' : fake.date(), 
        'comment' : fake.sentence()
    }
    return create_order

@allure.step('Генерируем курьера с неверными данными')
def generate_invalid_data_courier(courier_data, change):
    modify_courier_data = courier_data.copy()
    if change == 'login':
        modify_courier_data[change] = fake.pystr(min_chars=30, max_chars=40)
        return modify_courier_data
    modify_courier_data[change] = fake.password(length=30)
    return modify_courier_data

