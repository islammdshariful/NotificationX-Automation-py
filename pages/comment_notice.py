from selenium.webdriver.common.keys import Keys
from utils.create_notice_helper import *
import utils.config as conf



class Comment:
    ADD_NEW = (By.XPATH, f'//*[@id="notificationx"]/div/div[1]/div[1]/div[1]/div/a')
    NX_TITLE = (By.ID, f'nx-title')
    NEXT_0 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button')
    NEXT_1 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button[2]')
    PUBLISH = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div['
                         f'2]/div[2]/button')

    # common fields
    CONTENT_1ST = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'1]/div/div/div/div/div[2]')
    CONTENT_1ST_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                                    f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                                    f'1]/div/div/div/div[2]/div/div[2]')

    CONTENT_2ND = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'3]/div/div/div/div/div[2]')
    CONTENT_2ND_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                                    f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                                    f'3]/div/div/div/div[2]/div/div[2]')

    CONTENT_3RD = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'4]/div/div/div/div/div[2]')
    CONTENT_3RD_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                                    f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                                    f'4]/div/div/div/div[2]/div/div[2]')

    CONTENT_4TH = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'5]/div/div/div/div/div[2]')
    CONTENT_4TH_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                                    f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                                    f'5]/div/div/div/div[2]/div/div[2]')

    CONTENT_1ST_REVIEW_DSTAT = (
        By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div['
                  f'1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]')
    CONTENT_1ST_REVIEW_DSTAT_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div['
                                                 f'1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div['
                                                 f'3]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]')

    CONTENT_2ND_REVIEW_DSTAT = (
        By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div['
                  f'1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[3]/div/div/div/div/div[2]')
    CONTENT_2ND_REVIEW_DSTAT_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div['
                                                 f'1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div['
                                                 f'3]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div[2]')

    CONTENT_3RD_REVIEW_DSTAT = (
        By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div['
                  f'1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div/div/div/div[2]')
    CONTENT_3RD_REVIEW_DSTAT_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div['
                                                 f'1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div['
                                                 f'3]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div[3]')

    CONTENT_1ST_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div['
                                           f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
                                           f'2]/div/div/div[1]/div/div/div/div/div[2]')
    CONTENT_1ST_CONTACT_EMAIL_CHOOSE = (By.XPATH, f'')

    CONTENT_2ND_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div['
                                           f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
                                           f'2]/div/div/div[3]/div/div/div/div/div[2]')
    CONTENT_2ND_CONTACT_EMAIL_CHOOSE = (By.XPATH, f'')

    CONTENT_3RD_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div['
                                           f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
                                           f'2]/div/div/div[4]/div/div/div/div/div[2]')
    CONTENT_3RD_CONTACT_EMAIL_CHOOSE = (By.XPATH, f'')

    # comment notification
    COMMENT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[2]/div/label')
    COMMENT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[5]/div/label/img')
    COMMENT_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    COMMENT_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    COMMENT_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    COMMENT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    COMMENT_CONTENT_LENGTH = (By.ID, f'content_trim_length')
    NT_TEMPLATE_TEXT = (By.NAME, f'second_param')
    RANDOM_ORDER = (By.ID, f'random_order')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.execute_script("window.scrollTo(0, 0)")

    def create_comment_notice(self, pos):
        h = Helper(self.browser)

        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Comment Notification')

        # source page
        self.browser.find_element(*self.COMMENT).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.COMMENT_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.CONTENT_1ST).click()
        # self.browser.find_element(*self.COMMENT_1ST_CHOOSE).click()
        self.browser.find_element(*self.CONTENT_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Motamot dilo')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND).click()
        # self.browser.find_element(*self.COMMENT_2ND_CHOOSE).click()
        self.browser.find_element(*self.CONTENT_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD).click()
        # self.browser.find_element(*self.COMMENT_3RD_CHOOSE).click()
        self.browser.find_element(*self.CONTENT_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.COMMENT_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.COMMENT_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # content length
        self.browser.find_element(*self.COMMENT_CONTENT_LENGTH).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.COMMENT_CONTENT_LENGTH).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.COMMENT_CONTENT_LENGTH).send_keys('15')

        # common tasks
        h.common_task('comment', pos)