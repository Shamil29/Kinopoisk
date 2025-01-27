import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: webdriver):
        self.__driver = driver

    def title_on_the_auth_page(self):
        title_element = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "head > title")))
        return title_element.get_attribute("textContent")

    @allure.step('Кнопка стрелки назад')
    def back_button(self):
        with (allure.step("Нажатие на кнопку стрелки назад")):
            WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, "svg[class='PreviousStepButton-icon']"))
            ).click()

    @allure.step("Получить текущий URL")
    def get_current_url_main(self):
        return self.__driver.current_url

    @allure.step('Поле "Логин или email"')
    def field_login(self, login):
        with allure.step(
                f'Ввод данных в поле "Логин или email", Логин - {login}'):
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
        with allure.step("Нажатие на кнопку 'Войти с паролем'"):
            self.__driver.find_element(
                By.CSS_SELECTOR, ".PasswordButton").click()

        with allure.step(
                f'Ввод данных в поле "Введите пароль", Пароль - {password}'):
            password_field = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "passwd")))
            password_field.clear()
            password_field.send_keys(password)
            return password_field.get_attribute("value")

    @allure.step("Нажатие на кнопку 'Продолжить'")
    def password_button(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.step("Нажатие на кнопку 'Показать пароль'")
    def show_password(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[title="Показать текст пароля"]').click()
        password_field = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "passwd")))
        return password_field.get_attribute("value")
