import sys
import os
import pytest
from selenium import webdriver
import time

# Добавляем текущую папку в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    time.sleep(3)
    yield driver
    driver.quit()