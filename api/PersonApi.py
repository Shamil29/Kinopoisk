import requests
import allure


class PersonApi:
    def __init__(self, url):
        self.url = url

    @allure.step("Поиск персоны по имени")
    def get_list_person_by_name(self, my_token: str, name_to_search: str):
        """
        Этот метод вернет список персон, которые подходят под запрос.
        my_token (str): токен для выполнения запроса,
        name_to_search (str): имя и фамилия персоны.
        """
        my_headers = {
            "X-API-KEY": my_token
        }
        my_query = name_to_search
        resp = requests.get(
            self.url + '/person/search?query=' + my_query, headers=my_headers)
        return resp
