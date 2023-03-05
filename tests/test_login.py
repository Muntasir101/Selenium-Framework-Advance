import pytest
from pages.login_page import LoginPage
from utils.config import Config
from utils.logger import logger
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    config = Config()
    login_page = LoginPage(driver)
    login_page.load(config.base_url)
    login_page.login(config.username, config.password)
    assert driver.title == 'Home Page - Ultimate QA'
