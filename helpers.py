
import allure

@allure.step('Изменяем предпочитаемые цвета заказа')
def modify_order_body(data, value):
    data['color'] = value
    return data


@allure.step('Удаляем одно поле в логине курьера по ключу ')
def modify_courier_body(data, key):
    courier_data = data.copy()
    courier_data.pop(key)
    return courier_data

