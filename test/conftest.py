import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from utils.config import URL_DASHBOARD, USERNAME, PASSWORD


@pytest.fixture(scope='session', autouse=True)
def browser():
    options = Options()
    # options.add_experimental_option("detach", True)
    # options.add_experimental_option('debuggerAddress', 'localhost:9250')
    browser = webdriver.Chrome(chrome_options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)
    login_to_dashboard(browser)

    yield browser

    browser.quit()


def login_to_dashboard(browser):
    browser.get(URL_DASHBOARD)
    browser.find_element(By.ID, 'user_login').send_keys(USERNAME)
    browser.find_element(By.ID, 'user_pass').send_keys(PASSWORD)
    browser.find_element(By.ID, 'wp-submit').click()
