from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utils.config as conf


class AddUser:
    USER_PATH = (By.XPATH, f'//*[@id="menu-users"]/a/div[3]')
    ADD_NEW = (By.XPATH, f'//*[@id="wpbody-content"]/div[3]/a')
    USERNAME = (By.ID, f'user_login')
    EMAIL = (By.ID, f'email')
    F_NAME = (By.ID, f'first_name')
    L_NAME = (By.ID, f'last_name')
    PASSWORD = (By.ID, f'pass1')
    CON_PASSWORD = (By.XPATH, f'//*[@id="createuser"]/table/tbody/tr[8]/td/label')
    ADD_NEW_USER = (By.ID, f'createusersub')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_ADD_USER)

    def add_users(self, int_count):
        count = str(int_count)
        self.browser.find_element(*self.USER_PATH).click()
        self.browser.find_element(*self.ADD_NEW).click()

        self.browser.find_element(*self.USERNAME).send_keys('sub' + count)
        self.browser.find_element(*self.EMAIL).send_keys('testerbhaai+sub' + count + '@gmail.com')
        self.browser.find_element(*self.F_NAME).send_keys('First' + count)
        self.browser.find_element(*self.L_NAME).send_keys('Last' + count)
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.PASSWORD).send_keys('1234')

        self.browser.find_element(*self.CON_PASSWORD).click()
        self.browser.find_element(*self.ADD_NEW_USER).click()

