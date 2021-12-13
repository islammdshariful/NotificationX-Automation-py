from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utils.config import *


class Helper:
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

    NT_TEMPLATE_TEXT = (By.NAME, f'second_param')
    RANDOM_ORDER = (By.ID, f'random_order')
    LINK_TYPE = (By.XPATH, f'//*[@id="link_type"]/div/div[2]')
    LINK_TYPE_CHOOSE = (By.ID, f'react-select-11-option-2')
    UTM_CAMPAIGN = (By.ID, f'utm_campaign')
    UTM_MEDIUM = (By.ID, f'utm_medium')
    UTM_SOURCE = (By.ID, f'utm_source')
    SHOW_DEFAULT_IMAGE = (By.ID, f'show_default_image')
    DEFAULT_IMAGE = (By.XPATH, f'//*[@id="display_tab"]/div[1]/div[2]/div[2]/div[2]/div/div/div[5]/div/label/img')
    IMAGE = (By.XPATH, f'//*[@id="show_notification_image"]/div/div[2]')
    FEATURE_IMAGE_CHOOSE = (By.ID, f'react-select-10-option-1')
    COMMENT_GRAVATAR_IMAGE = (By.ID, f'react-select-10-option-1')
    GRAVATAR_IMAGE = (By.ID, f'react-select-10-option-2')
    MAP_IMAGE = (By.ID, f'react-select-10-option-3')
    SHOW_ON = (By.XPATH, f'//*[@id="show_on"]/div/div[2]')
    SHOW_ON_CHOOSE = (By.ID, f'react-select-3-option-0')
    DISPLAY_FOR = (By.XPATH, f'//*[@id="show_on_display"]/div/div[2]')
    DISPLAY_FOR_CHOOSE = (By.ID, f'react-select-4-option-0')
    POSITION = (By.XPATH, f'//*[@id="position"]/div/div[2]')
    POSITION_CHOOSE_LEFT = (By.ID, f'react-select-5-option-0')
    POSITION_CHOOSE_RIGHT = (By.ID, f'react-select-5-option-1')
    STICKY_BAR = (By.ID, f'sticky_bar')
    OVERLAPPING = (By.ID, f'pressbar_body')
    NOTIFICATION_SIZE = (By.ID, f'size')
    CLOSE_BUTTON = (By.ID, f'close_button')
    HIDE_ON_MOBILE = (By.ID, f'hide_on_mobile')
    GLOBAL_QUEUE = (By.ID, f'global_queue')
    DELAY_BEFORE = (By.ID, f'delay_before')
    DISPLAY_FOR = (By.ID, f'display_for')
    DELAY_BETWEEN = (By.ID, f'delay_between')
    INITIAL_DELAY = (By.ID, f'initial_delay')
    AUTO_HIDE = (By.ID, f'auto_hide')
    HIDE_AFTER = (By.ID, f'hide_after')
    SOUND = (By.XPATH, f'//*[@id="sound"]/div/div[2]')
    SOUND_CHOOSE = (By.ID, f'react-select-6-option-1')
    DISPLAY_LAST = (By.ID, f'display_last')
    DISPLAY_FORM = (By.ID, f'display_from')
    LOOP = (By.ID, f'loop')
    LINK_OPEN = (By.ID, f'link_open')

    SUCCESS_NOTICE = (By.XPATH, f'//*[@id="notificationx"]/div/div[1]/div[2]/p')

    def __init__(self, browser):
        self.browser = browser

    def double_clicks(self, element):
        self.browser.find_element(*element).click()
        self.browser.find_element(*element).click()

    def common_task(self, src, pos):
        if src != 'nxbarel':
            if src != 'contact' and src != 'email_subs' and src != 'custom' and src != 'nxbar':
                # link type
                self.browser.find_element(*self.LINK_TYPE).click()
                self.browser.find_element(*self.LINK_TYPE_CHOOSE).click()

            # utm controls
            self.browser.find_element(*self.UTM_CAMPAIGN).send_keys('campaign_automation')
            self.browser.find_element(*self.UTM_MEDIUM).send_keys('medium_automation')
            self.browser.find_element(*self.UTM_SOURCE).send_keys('source_automation')

        # next page display
        self.browser.find_element(*self.NEXT_1).click()

        # image
        self.browser.execute_script("window.scrollTo(0, 0)")
        if src != 'nxbarel' and src != 'nxbar':
            self.browser.find_element(*self.SHOW_DEFAULT_IMAGE).click()
            self.browser.find_element(*self.SHOW_DEFAULT_IMAGE).click()
            if src != 'download-stat':
                self.browser.find_element(*self.IMAGE).click()
                if src == 'comment':
                    self.browser.find_element(*self.COMMENT_GRAVATAR_IMAGE).click()
                elif src == 'contact':
                    self.browser.find_element(*self.GRAVATAR_IMAGE).click()
                else:
                    self.browser.find_element(*self.FEATURE_IMAGE_CHOOSE).click()
        # visibility
        self.browser.find_element(*self.SHOW_ON).click()
        self.browser.find_element(*self.SHOW_ON_CHOOSE).click()
        # next page customize
        self.browser.find_element(*self.NEXT_1).click()

        # customize page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # appearance
        self.browser.find_element(*self.POSITION).click()
        if pos == "L" or pos == "T":
            self.browser.find_element(*self.POSITION_CHOOSE_LEFT).click()
        else:
            self.browser.find_element(*self.POSITION_CHOOSE_RIGHT).click()
        # sticky bar
        if src == 'nxbarel' or src == 'nxbar':
            self.browser.find_element(*self.STICKY_BAR).click()
            self.browser.find_element(*self.OVERLAPPING).click()
        # notification size
        if src != 'nxbarel' and src != 'nxbar':
            self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys('400')
        # display close option
        self.double_clicks(self.CLOSE_BUTTON)
        self.double_clicks(self.HIDE_ON_MOBILE)
        # queue management
        if src != 'nxbarel' and src != 'nxbar':
            self.double_clicks(self.GLOBAL_QUEUE)
        # timing
        if src == 'nxbarel' or src == 'nxbar':
            # initial delay
            self.browser.find_element(*self.INITIAL_DELAY).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.INITIAL_DELAY).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.INITIAL_DELAY).send_keys('1')
            # auto hide
            self.browser.find_element(*self.AUTO_HIDE).click()
            self.browser.find_element(*self.HIDE_AFTER).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.HIDE_AFTER).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.HIDE_AFTER).send_keys('20')
        else:
            # delay before
            self.browser.find_element(*self.DELAY_BEFORE).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.DELAY_BEFORE).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.DELAY_BEFORE).send_keys('1')
            # display for
            self.browser.find_element(*self.DISPLAY_FOR).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.DISPLAY_FOR).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.DISPLAY_FOR).send_keys('5')
            # delay between
            self.browser.find_element(*self.DELAY_BETWEEN).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.DELAY_BETWEEN).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.DELAY_BETWEEN).send_keys('2')

        if src != 'nxbarel' and src != 'nxbar':
            # sound
            self.browser.find_element(*self.SOUND).click()
            self.browser.find_element(*self.SOUND_CHOOSE).click()
        # behavior
        if src != 'nxbarel' and src != 'nxbar':
            # display last
            self.browser.find_element(*self.DISPLAY_LAST).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.DISPLAY_LAST).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.DISPLAY_LAST).send_keys('19')
            # display form the last
            self.browser.find_element(*self.DISPLAY_FORM).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.DISPLAY_FORM).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.DISPLAY_FORM).send_keys('20')
            # loop
            self.double_clicks(self.LOOP)
        if src != 'contact' and src != 'email_subs' and src != 'nxbarel':
            # open link in a new tab
            self.browser.find_element(*self.LINK_OPEN).click()

        # publishing notification
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.PUBLISH).click()

        assert self.browser.find_element(*self.SUCCESS_NOTICE).text == 'Successfully Created.'