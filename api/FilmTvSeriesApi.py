import requests
import allure


class FilmTvSeriesApi:
    def __init__(self, url):
        self.url = url

    @allure.step("Поиск фильма или сериала по его названию")
    def get_list_films_by_name(self, my_token: str, name_to_search: str):
        """
        Этот метод вернет список фильмов, которые подходят под запрос.
        my_token (str): токен для выполнения запроса,
        name_to_search (str): название фильма или сериала.
        """
        my_headers = {
            "X-API-KEY": my_token
        }
        my_query = name_to_search
        resp = requests.get(
            self.url + '/movie/search?query=' + my_query, headers=my_headers)
        return resp

    @allure.step("Поиск фильма или сериала по ID")
    def get_film_tv_series_by_id(self, my_token: str, id_film_tv_series: int):
        """
        Возвращает всю доступную информацию о сущности.
        my_token (str): токен для выполнения запроса,
        id_film_tv_series (str): id фильма или сериала.
        """
        my_headers = {
            "X-API-KEY": my_token
        }
        search_id = id_film_tv_series
        resp = requests.get(
            self.url + '/movie/' + str(search_id), headers=my_headers)
        return resp
