import time

from selenium.webdriver.common.by import By
import utils.config as conf


class WpLoginPage:
    USERNAME_ID = (By.ID, 'user_login')
    PASSWORD_ID = (By.ID, 'user_pass')
    BUTTON_ID = (By.ID, 'wp-submit')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_DASHBOARD)

    def login(self, config):
        self.browser.find_element(*self.USERNAME_ID).click()
        self.browser.find_element(*self.USERNAME_ID).clear()
        self.browser.find_element(*self.USERNAME_ID).send_keys(config['username'])
        self.browser.find_element(*self.PASSWORD_ID).click()
        self.browser.find_element(*self.PASSWORD_ID).clear()
        self.browser.find_element(*self.PASSWORD_ID).send_keys(config['password'])
        self.browser.find_element(*self.BUTTON_ID).click()
