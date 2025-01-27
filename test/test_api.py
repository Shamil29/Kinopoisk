import allure
import pytest
import json
from api.FilmTvSeriesApi import FilmTvSeriesApi
from api.PersonApi import PersonApi
from translate import Translator


with open("test/config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

my_token = config.get("token_info")
positive_films_data = config.get("film_title_for_positive")
negative_films_data = config.get("film_title_for_negative")
positive_person_data = config.get("name_to_search_for_positive")
negative_person_data = config.get("name_to_search_for_negative")
search_id = config.get("id_film_tv_series")


@allure.suite("Кинопоиск. API")
@allure.feature("Поиск фильма/сериала. API")
@allure.title("Позитивный тест поиска фильма/сериала по названию")
@allure.severity("Blocker")
@allure.id(1)
@pytest.mark.parametrize("film_title_for_positive", positive_films_data)
def test_get_list_films_by_name_pos(
        api_film: FilmTvSeriesApi, film_title_for_positive):
    list_films = api_film.get_list_films_by_name(
        my_token, film_title_for_positive)
    with allure.step("Проверка статус-кода"):
        assert list_films.status_code == 200
    with allure.step("Проверка наличия переданного названия в ответе"):
        assert film_title_for_positive in list_films.json()[
            'docs'][1]['internalNames']


@allure.suite("Кинопоиск. API")
@allure.feature("Поиск фильма/сериала. API")
@allure.title("Негативный тест поиска фильма/сериала по названию")
@allure.severity("Blocker")
@allure.id(2)
@pytest.mark.parametrize("film_title_for_negative", negative_films_data)
def test_get_list_films_by_name_neg(
        api_film: FilmTvSeriesApi, film_title_for_negative):
    list_films = api_film.get_list_films_by_name(
        my_token, film_title_for_negative)
    with allure.step("Проверка статус-кода"):
        assert list_films.status_code == 200
    with allure.step("Проверка пустого списка в ответе"):
        assert len(list_films.json()['docs']) == 0


@allure.suite("Кинопоиск. API")
@allure.feature("Поиск персоны. API")
@allure.title("Позитивный тест поиска персоны по имени")
@allure.severity("Blocker")
@allure.id(3)
@pytest.mark.parametrize("name_to_search_for_positive", positive_person_data)
def test_get_list_person_by_name_pos(
        api_person: PersonApi, name_to_search_for_positive):
    person = api_person.get_list_person_by_name(
        my_token, name_to_search_for_positive)
    with allure.step("Проверка статус-кода"):
        assert person.status_code == 200

    name_in_response = person.json()['docs'][0]['name']
    name_to_search = name_to_search_for_positive
    translator = Translator(from_lang='en', to_lang='ru')
    translated_name = translator.translate(name_to_search)
    with allure.step("Проверка наличия переданного названия в ответе"):
        assert translated_name in name_in_response


@allure.suite("Кинопоиск. API")
@allure.feature("Поиск персоны. API")
@allure.title("Негативный тест поиска персоны по имени")
@allure.severity("Blocker")
@allure.id(4)
@pytest.mark.parametrize("name_to_search_for_negative", negative_person_data)
def test_get_list_person_by_name_neg(
        api_person: PersonApi, name_to_search_for_negative):
    person = api_person.get_list_person_by_name(
        my_token, name_to_search_for_negative)
    with allure.step("Проверка статус-кода"):
        assert person.status_code == 200
    with allure.step("Проверка пустого списка в ответе"):
        assert len(person.json()['docs']) == 0


@allure.suite("Кинопоиск. API. API")
@allure.feature("Поиск фильма/сериала")
@allure.title("Позитивный тест поиска фильма/сериала по ID")
@allure.severity("Blocker")
@allure.id(5)
@pytest.mark.parametrize("id_film_tv_series", search_id)
def test_get_film_tv_series_by_id(
        api_film: FilmTvSeriesApi, id_film_tv_series):
    film_tv_series = api_film.get_film_tv_series_by_id(
        my_token, id_film_tv_series)
    with allure.step("Проверка статус-кода"):
        assert film_tv_series.status_code == 200
    with allure.step("Проверка наличия переданного id в ответе"):
        assert film_tv_series.json()['id'] == id_film_tv_series
