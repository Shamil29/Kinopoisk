import allure
import pytest
from time import sleep
from pages.MainPage import MainPage
from pages.AuthPage import AuthPage


@allure.suite("Кинопоиск UI")
@allure.feature("Главная страница")
@allure.title("Тест на переход с главной страницы на страницу с авторизацией")
@allure.severity("Blocker")
@allure.id(1)
def test_go_to_the_auth_page(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    with allure.step(
            "Проверка перехода на страницу с авторизацией"):
        assert main_page.get_current_url_auth().startswith("https://passport.yandex.ru")

@allure.suite("Кинопоиск UI")
@allure.feature("Страница с авторизацией")
@allure.title("Тест на переход со страницы с авторизацией на главную страницу")
@allure.severity("Blocker")
@allure.id(2)
def test_go_to_the_main_page(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    auth_page = AuthPage(driver)
    auth_page.back_button()
    with allure.step(
            "Проверка возврата на главную страницу после авторизации"):
        assert auth_page.get_current_url_main().startswith("https://www.kinopoisk.ru/")

@allure.suite("Кинопоиск UI")
@allure.feature("Страница с авторизацией")
@allure.title('Тест поля "Логин или email"')
@allure.severity("Blocker")
@allure.id(3)
def test_field_login(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    auth_page = AuthPage(driver)
    my_login = "shoma291195"
    result_login = auth_page.field_login(my_login)
    with allure.step("Проверка отображения введенного текста в поле" +my_login):
        assert result_login == my_login
    auth_page.login_button()

@allure.suite("Кинопоиск UI")
@allure.feature("Страница с авторизацией")
@allure.title('Тест поля "Введите пароль"')
@allure.severity("Blocker")
@allure.id(4)
def test_field_password(driver):
    main_page = MainPage(driver)
    main_page.login_button()
    auth_page = AuthPage(driver)
    my_login = "shoma291195"
    auth_page.field_login(my_login)
    auth_page.login_button()
    my_password = "!19"
    result_password = auth_page.field_password(my_password)

    with allure.step("Проверка отображения введенного текста в поле" +my_password):
        assert result_password == my_password
    auth_page.password_button()

@allure.suite("Кинопоиск UI")
@allure.feature("Модуль поиска")
@allure.title("Тест поисковой строки на совпадение переданного значения с выводимым в подсказках")
@allure.severity("Blocker")
@allure.id(5)
def test_search_bar(driver):
    main_page = MainPage(driver)
    film_tv_series = "Титаник"
    main_page.search_bar(film_tv_series)
    hints = main_page.get_search_field_list()

    # Проверить наличие хотя бы одной подсказки
    assert len(hints)>0, "Нет подсказок!"

    # Проверить, что первая подсказка содержит введенный поисковый запрос
    first_hint = hints[0]
    assert film_tv_series in first_hint, "Первая подсказка не содержит введенного запроса"

@allure.suite("Кинопоиск UI")
@allure.feature("Модуль поиска")
@allure.title("Тест поиска фильма/сериала/персоны по названию")
@allure.severity("Blocker")
@allure.id(5)
def test_search_film_tv_series_person(driver):
    main_page = MainPage(driver)
    film_tv_series_person = "Троя"
    main_page.search_bar(film_tv_series_person)
    main_page.search_icon()
    result = main_page.search_film_tv_series_person()
    assert result == film_tv_series_person

    sleep(3)