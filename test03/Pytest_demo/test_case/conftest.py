import pytest
from selenium import webdriver
from Pytest_demo.web_keys.web_keys import Webkeys

@pytest.fixture(scope='session')
def driver():
    driver = Webkeys('Chrome')
    return driver