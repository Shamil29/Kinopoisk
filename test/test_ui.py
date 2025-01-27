import allure
from pages.MainPage import MainPage
from pages.AuthPage import AuthPage
import json


with open("test/config.json", "r") as config_file:
    config = json.load(config_file)


@allure.suite("Кинопоиск. UI")
@allure.feature("Главная страница. UI")
@allure.title("Тест на переход с главной страницы на страницу с авторизацией")
@allure.severity("Blocker")
@allure.id(1)
def test_go_to_the_auth_page(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    with (allure.step(
            "Проверка перехода на страницу с авторизацией")):
        assert main_page.get_current_url_auth(
        ).startswith("https://passport.yandex.ru")
    with allure.step("Проверка Title страницы"):
        auth_page = AuthPage(driver)
        assert auth_page.title_on_the_auth_page() == "Авторизация"


@allure.suite("Кинопоиск. UI")
@allure.feature("Страница с авторизацией. UI")
@allure.title("Тест на переход со страницы с авторизацией на главную страницу")
@allure.severity("Blocker")
@allure.id(2)
def test_go_to_the_main_page(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    auth_page = AuthPage(driver)
    auth_page.back_button()
    with (allure.step(
            "Проверка возврата на главную страницу после авторизации")):
        assert auth_page.get_current_url_main(
        ).startswith("https://www.kinopoisk.ru/")
    with allure.step("Проверка Title страницы"):
        assert main_page.title_on_the_main_page() == ("Кинопоиск. "
                                                      "Онлайн кинотеатр. "
                                                      "Фильмы "
                                                      "сериалы "
                                                      "мультфильмы "
                                                      "и энциклопедия")


@allure.suite("Кинопоиск. UI")
@allure.feature("Страница с авторизацией. UI")
@allure.title('Тест поля "Логин или email"')
@allure.description("Проверяется ввод текста в поле "
                    "и возможность перейти на след шаг")
@allure.severity("Blocker")
@allure.id(3)
def test_field_login(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    auth_page = AuthPage(driver)
    my_login = config.get("username")
    result_login = auth_page.field_login(my_login)
    with allure.step(
            "Проверка отображения введенного текста в поле" + my_login):
        assert result_login == my_login
    auth_page.login_button()


@allure.suite("Кинопоиск. UI")
@allure.feature("Страница с авторизацией. UI")
@allure.title('Тест поля "Введите пароль"')
@allure.description("Проверяется ввод текста в поле "
                    "и возможность перейти на след шаг")
@allure.severity("Blocker")
@allure.id(4)
def test_field_password(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    auth_page = AuthPage(driver)
    my_login = config.get("username")
    auth_page.field_login(my_login)
    auth_page.login_button()
    my_password = config.get("password")
    result_password = auth_page.field_password(my_password)
    with allure.step(
            "Проверка отображения введенного текста в поле" + my_password):
        assert result_password == my_password
    auth_page.password_button()


@allure.suite("Кинопоиск. UI")
@allure.feature("Модуль поиска. UI")
@allure.title(
    "Тест поисковой строки "
    "на совпадение переданного значения с выводимым в подсказках")
@allure.severity("Blocker")
@allure.id(5)
def test_search_bar(driver):
    main_page = MainPage(driver)
    short_name = "Тит"
    film_tv_series = "Титаник"
    main_page.search_bar(short_name)
    hints = main_page.get_search_field_list()
    with allure.step("Проверка наличия хотя бы одной подсказки"):
        assert len(hints) > 0
    with allure.step(
            "Проверка наличия введённого поискового запроса "
            "в первой подсказке"):
        first_hint = hints[0]
        assert film_tv_series in first_hint


@allure.suite("Кинопоиск. UI")
@allure.feature("Модуль поиска. UI")
@allure.title("Тест поиска фильма/сериала/персоны по названию")
@allure.description("Название фильма/сериала/персоны для поиска "
                    "должно присутствовать в списке 'Скорее всего, вы ищете:'")
@allure.severity("Blocker")
@allure.id(6)
def test_search_film_tv_series_person(driver):
    main_page = MainPage(driver)
    film_tv_series_person = "Вверх"
    main_page.search_bar(film_tv_series_person)
    main_page.search_icon()
    result = main_page.search_film_tv_series_person()
    with allure.step(
            "Проверка наличия введённого поискового запроса "
            "в списке 'Скорее всего, вы ищете:'"):
        assert result == film_tv_series_person
