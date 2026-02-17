
import requests
import allure
from urls import Urls


class OrderMethods:

    @staticmethod
    @allure.step('Создаем заказ')
    def create_order(order_data):
        return requests.post(Urls.CREATE_ORDER, json=order_data, timeout=30)    
    
    @staticmethod
    @allure.step('Отменяем заказ')
    def cancel_order(order_data):
        return requests.put(Urls.CANCEL_ORDER, params=order_data, timeout=30)
    
    @staticmethod
    @allure.step('Получаем список заказов')
    def get_list_order():
        return requests.get(Urls.LIST_ORDERS, timeout=30)
    
    @staticmethod
    @allure.step('Получаем заказ по id')
    def get_id_order(order_data):
        return requests.get(Urls.ORDER_BY_ID, params=order_data, timeout=30)
    
    @staticmethod
    @allure.step('Неполучение заказа по id без id')
    def get_id_without_id_order():
        return requests.get(Urls.ORDER_BY_ID, timeout=30)


