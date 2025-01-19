import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from pages.AuthPage import AuthPage
# from pages.MainPage import MainPage

# import json
#
# with open("../config.json", "r") as config_file:
#     config = json.load(config_file)
#
# base_url_api = config.get("base_url_api")
# token_info = config.get("token_info")

@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    driver.get("https://www.kinopoisk.ru")
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()

# def main_page(driver):
#     return MainPage(driver)
#
# def auth_page(driver):
#     return AuthPage(driver)


