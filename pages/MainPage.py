import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver:webdriver):
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    @allure.step("Нажатие на кнопку 'Войти' на главной странице")
    def login_button(self):
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_loginButton__LWZQp"))).click()

    @allure.step("Получить текущий URL")
    def get_current_url_auth(self):
        return self.__driver.current_url

    @allure.step("Строка поиска на главной странице")
    def search_bar(self, value):
        with allure.step(f'Ввод данных в строку поиска, {value}'):
            search_bar = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "kp_query")))
            search_bar.clear()
            search_bar.send_keys(value)

    @allure.step("Получить текст элементов в подсказках к поисковому полю.")
    def get_search_field_list(self):
        hints = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.styles_groupsContainer__Uw6bW')))
        return [hint.text for hint in hints]

    @allure.step("Нажатие на значок 'Поиска'")
    def search_icon(self):
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-form-submit-button__icon'))).click()

    @allure.step("Поиска фильма/сериала/персоны по названию")
    def search_film_tv_series_person(self):
        div = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.most_wanted')))
        div_info = div.find_element(By.CSS_SELECTOR, '.info')
        p_name = div_info.find_element(By.CSS_SELECTOR, '.name')
        a_result = p_name.find_element(By.CSS_SELECTOR, 'a')
        result = a_result.text
        return result
