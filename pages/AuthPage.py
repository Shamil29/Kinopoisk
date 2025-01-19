import pytest
import allure
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: webdriver):
        self.__url = "https://passport.yandex.ru/auth?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D0a2952cf-2a30-4582-be40-bde644427c28"
        self.__driver = driver
        # self.driver.get(
        #     "https://passport.yandex.ru/auth?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%26uuid%3D0a2952cf-2a30-4582-be40-bde644427c28")
        # self.__url = "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fid.yandex.ru%2F&noreturn=1"

    @allure.step('Кнопка стрелки назад')
    def back_button(self):
        with allure.step("Нажатие на кнопку стрелки назад"):
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[class='PreviousStepButton-icon']"))).click()

    @allure.step("Получить текущий URL")
    def get_current_url_main(self):
        return self.__driver.current_url

    @allure.step('Поле "Логин или email"')
    def field_login(self, login):
        with allure.step(f'Ввод данных в поле "Логин или email", Логин - {login}'):
            username_field = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "login")))
            username_field.clear()
            username_field.send_keys(login)
            return username_field.get_attribute("value")

    @allure.step('Нажатие на кнопку "Войти"')
    def login_button(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.step('Поле "Пароль"')
    def field_password(self, password):
        # with allure.step("Нажатие на кнопку 'Войти с паролем'"):
        #     self.__driver.find_element(By.CSS_SELECTOR, ".PasswordButton").click()

        with allure.step(f'Ввод данных в поле "Введите пароль", Пароль - {password}'):
            password_field = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "passwd")))
            password_field.clear()
            password_field.send_keys(password)
            return password_field.get_attribute("value")

    @allure.step("Нажатие на кнопку 'Продолжить'")
    def password_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.step("Нажатие на кнопку 'Показать пароль'")
    def show_password(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'button[title="Показать текст пароля"]').click()
        password_field = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "passwd")))
        return password_field.get_attribute("value")

    # @allure.step('Текст "Не помню пароль"')
    # def not_remember_pass(self):
    #     with allure.step('Нажатие на текст "Не помню пароль"'):
    #         self.__driver.find_element(
    #             By.CSS_SELECTOR, "button[type='submit']").click()


    # @allure.step("Авторизация по номеру телефона")
    # def phone_auth(self,number_phone):
    #      with allure.step('Нажатие на вкладку "Телефон"'):
    #          WebDriverWait(self.__driver, 10).until(
    #             EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-type='phone']"))).click()
    #
    #      with allure.step(f"Ввод данных в поле номера телефона, Номер телефона - {number_phone}"):
    #          phone_field = WebDriverWait(self.__driver, 10).until(
    #              EC.visibility_of_element_located((By.ID, "passp-field-phone")))
    #          phone_field.send_keys(number_phone)
    #
    #      # with allure.step("Нажатие на кнопку 'Продолжить'"):
    #      #     self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #
    #      with allure.step(
    #              "Если появляется капча пытаемся её нажать, иначе продолжаем следующие шаги."
    #      ):
    #          try:
    #              self.__driver.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
    #          except NoSuchElementException:
    #              pass
