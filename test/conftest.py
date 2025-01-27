import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.FilmTvSeriesApi import FilmTvSeriesApi
from api.PersonApi import PersonApi
import json


with open("test/config.json", "r") as config_file:
    config = json.load(config_file)

base_url_api = config.get("base_url_api")
base_url_ui = config.get("base_url_ui")


@pytest.fixture
def driver():
    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        driver.get(base_url_ui)
        driver.implicitly_wait(4)
        driver.maximize_window()
        yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def api_film() -> FilmTvSeriesApi:
    return FilmTvSeriesApi(base_url_api)


@pytest.fixture
def api_person() -> PersonApi:
    return PersonApi(base_url_api)
