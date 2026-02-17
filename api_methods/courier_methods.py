
import requests
import allure
from urls import Urls


class CourierMethods:

    @staticmethod
    @allure.step('Создаем курьера')
    def create_courier(courier_data):
        return  requests.post(Urls.CREATE_COURIER, json=courier_data, timeout=30)      
    
    @staticmethod
    @allure.step('Получаем id курьера')
    def get_id_courier(courier_data):
        data = courier_data.copy()
        return requests.post(Urls.LOGIN_COURIER, json=data, timeout=30)
    
    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(login_id):
        return requests.delete(f'{Urls.DELETE_COURIER}{login_id}', timeout=30)        
    
    @staticmethod
    @allure.step('Нельзя удалить курьера без id')
    def delete_courier_without_id():
        return requests.delete(Urls.DELETE_COURIER, timeout=30)        


