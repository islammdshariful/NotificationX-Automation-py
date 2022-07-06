import time

from selenium.webdriver.common.by import By

import utils.config as conf


class Notice:
    NX_Image = (By.XPATH, f'/html/body/div[3]/div/div/div/div/div[1]/img')
    NX_1ST_ROW = (By.XPATH, f'/html/body/div[3]/div/div/div/div/div[2]/p[1]')
    NX_2ND_ROW = (By.XPATH, f'/html/body/div[3]/div/div/div/div/div[2]/p[2]')
    NX_3RD_ROW = (By.XPATH, f'/html/body/div[3]/div/div/div/div/div[2]/p[3]')
    NX_CLOSE_BUTTON = (By.XPATH, f'/html/body/div[3]/div/div/div/div/div[3]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(conf.HOME_URL)

    def sale_notice(self):
        if self.browser.find_element(*self.NX_Image).is_displayed():
            print("Image Displayed")
        else:
            print("Image Not Displayed")

        # assert self.browser.find_element(*self.NX_1ST_ROW).text == ''
        # assert self.browser.find_element(*self.NX_2ND_ROW).text == ''
        # assert self.browser.find_element(*self.NX_3RD_ROW).text == ''

        time.sleep(.5)
        self.browser.find_element(*self.NX_CLOSE_BUTTON).click()


