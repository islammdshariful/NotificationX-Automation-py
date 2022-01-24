import time

from assertpy import assert_that, soft_assertions
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import *


class Helper:
    add_new = (By.XPATH, f"//a[@class='nx-add-new-btn']")
    nx_title = (By.ID, f'nx-title')
    next_btn_for_wait = f"//button[normalize-space()='Next']"
    next_btn = (By.XPATH, f"//button[normalize-space()='Next']")
    prev_btn = (By.XPATH, f"//button[normalize-space()='Previous']")
    publish_btn = (By.XPATH, f"//button[normalize-space()='Publish']")

    # # common fields
    # CONTENT_1ST = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                          f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                          f'1]/div/div/div/div/div[2]')
    # CONTENT_1ST_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                                 f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                                 f'1]/div/div/div/div[2]/div/div[2]')
    #
    # CONTENT_2ND = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                          f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                          f'3]/div/div/div/div/div[2]')
    # CONTENT_2ND_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                                 f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                                 f'3]/div/div/div/div[2]/div/div[2]')
    #
    # CONTENT_3RD = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                          f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                          f'4]/div/div/div/div/div[2]')
    # CONTENT_3RD_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                                 f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                                 f'4]/div/div/div/div[2]/div/div[2]')
    #
    # CONTENT_4TH = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                          f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                          f'5]/div/div/div/div/div[2]')
    # CONTENT_4TH_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
    #                                 f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
    #                                 f'5]/div/div/div/div[2]/div/div[2]')
    #
    # CONTENT_1ST_REVIEW_DSTAT = (
    #     By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div['
    #               f'1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div/div/div/div[2]')
    # CONTENT_1ST_REVIEW_DSTAT_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div['
    #                                              f'1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div['
    #                                              f'3]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[2]')
    #
    # CONTENT_2ND_REVIEW_DSTAT = (
    #     By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div['
    #               f'1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[3]/div/div/div/div/div[2]')
    # CONTENT_2ND_REVIEW_DSTAT_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div['
    #                                              f'1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div['
    #                                              f'3]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div[2]')
    #
    # CONTENT_3RD_REVIEW_DSTAT = (
    #     By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div['
    #               f'1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div/div/div/div[2]')
    # CONTENT_3RD_REVIEW_DSTAT_CHOOSE = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div['
    #                                              f'1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div['
    #                                              f'3]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div[3]')
    #
    # CONTENT_1ST_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div['
    #                                        f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
    #                                        f'2]/div/div/div[1]/div/div/div/div/div[2]')
    # CONTENT_1ST_CONTACT_EMAIL_CHOOSE = (By.XPATH, f'')
    #
    # CONTENT_2ND_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div['
    #                                        f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
    #                                        f'2]/div/div/div[3]/div/div/div/div/div[2]')
    # CONTENT_2ND_CONTACT_EMAIL_CHOOSE = (By.XPATH, f'')
    #
    # CONTENT_3RD_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div['
    #                                        f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
    #                                        f'2]/div/div/div[4]/div/div/div/div/div[2]')
    # CONTENT_3RD_CONTACT_EMAIL_CHOOSE = (By.XPATH, f'')

    # nt_template_text = (By.NAME, f'second_param')
    random_order = (By.ID, f'random_order')
    # LINK OPTIONS
    link_type = (By.XPATH, f"//div[@id='link_type']")
    link_type_choose = (By.ID, f'react-select-11-option-2')
    # UTM CONTROL
    utm_campaign = (By.ID, f'utm_campaign')
    utm_medium = (By.ID, f'utm_medium')
    utm_source = (By.ID, f'utm_source')
    # IMAGE
    show_default_image = (By.ID, f'show_default_image')
    default_image = (By.XPATH, f"//label[@for='wprf-input-radio-3-4']")
    image = (By.XPATH, f"//div[@id='show_notification_image']")
    feature_image_choose = (By.ID, f'react-select-10-option-1')
    comment_gravatar_image = (By.ID, f'react-select-10-option-1')
    gravatar_image = (By.ID, f'react-select-10-option-2')
    map_image = (By.ID, f'react-select-10-option-3')
    # VISIBILITY
    show_on = (By.XPATH, f"//div[@id='show_on']")
    show_on_choose_everywhere = (By.ID, f'react-select-3-option-0')
    show_on_display = (By.XPATH, f"//div[@id='show_on_display']")
    show_on_display_choose_everyone = (By.ID, f'react-select-4-option-0')
    # APPEARANCE
    position = (By.XPATH, f"//div[@id='position']")
    position_choose_left = (By.ID, f'react-select-5-option-0')
    position_choose_right = (By.ID, f'react-select-5-option-1')
    sticky_bar = (By.ID, f'sticky_bar')
    overlapping = (By.ID, f'pressbar_body')
    notification_size = (By.ID, f'size')
    close_button = (By.ID, f'close_button')
    hide_on_mobile = (By.ID, f'hide_on_mobile')
    # QUEUE MANAGEMENT
    global_queue = (By.ID, f'global_queue')
    # TIMING
    delay_before_first_notification = (By.ID, f'delay_before')
    display_for = (By.ID, f'display_for')
    delay_between = (By.ID, f'delay_between')
    initial_delay = (By.ID, f'initial_delay')
    auto_hide = (By.ID, f'auto_hide')
    hide_after = (By.ID, f'hide_after')
    # SOUND SETTINGS
    sound = (By.XPATH, f"//div[@id='sound']")
    sound_choose = (By.ID, f'react-select-6-option-1')
    # BEHAVIOUR
    display_last = (By.ID, f'display_last')
    display_form = (By.ID, f'display_from')
    loop = (By.ID, f'loop')
    link_open = (By.ID, f'link_open')

    success_notice = f'//*[@id="notificationx"]/div/div[1]/div[2]/p'

    def __init__(self, browser):
        self.browser = browser

    def double_clicks(self, element):
        self.browser.find_element(*element).click()
        self.browser.find_element(*element).click()

    def do_others(self, src, pos):
        with soft_assertions():
            if src != 'nxbarel':
                if src != 'contact' and src != 'email_subs' and src != 'custom' and src != 'nxbar':
                    # link type
                    self.browser.find_element(*self.link_type).click()
                    self.browser.find_element(*self.link_type_choose).click()

                # utm controls
                self.browser.find_element(*self.utm_campaign).send_keys('campaign_automation')
                self.browser.find_element(*self.utm_medium).send_keys('medium_automation')
                self.browser.find_element(*self.utm_source).send_keys('source_automation')

            # next page display
            self.browser.find_element(*self.next_btn).click()

            # image
            self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            if src != 'nxbarel' and src != 'nxbar':
                self.browser.find_element(*self.show_default_image).click()
                self.browser.find_element(*self.show_default_image).click()
                if src != 'd_stat':
                    self.browser.find_element(*self.image).click()
                    if src == 'comment':
                        self.browser.find_element(*self.comment_gravatar_image).click()
                    elif src == 'contact':
                        self.browser.find_element(*self.gravatar_image).click()
                    else:
                        self.browser.find_element(*self.feature_image_choose).click()
            # visibility
            # show on
            self.browser.find_element(*self.show_on).click()
            self.browser.find_element(*self.show_on_choose_everywhere).click()
            # display for
            self.browser.find_element(*self.show_on_display).click()
            self.browser.find_element(*self.show_on_display_choose_everyone).click()
            # next page customize
            self.browser.find_element(*self.next_btn).click()

            # customize page
            self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            # appearance
            self.browser.find_element(*self.position).click()
            if pos == "L" or pos == "T":
                self.browser.find_element(*self.position_choose_left).click()
            else:
                self.browser.find_element(*self.position_choose_right).click()
            # sticky bar
            if src == 'nxbarel' or src == 'nxbar':
                self.browser.find_element(*self.sticky_bar).click()
                self.browser.find_element(*self.overlapping).click()
            # notification size
            if src != 'nxbarel' and src != 'nxbar':
                self.browser.find_element(*self.notification_size).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.notification_size).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.notification_size).send_keys('400')
            # display close option
            self.double_clicks(self.close_button)
            self.double_clicks(self.hide_on_mobile)
            # queue management
            if src != 'nxbarel' and src != 'nxbar':
                self.double_clicks(self.global_queue)
            # timing
            if src == 'nxbarel' or src == 'nxbar':
                # initial delay
                self.browser.find_element(*self.initial_delay).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.initial_delay).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.initial_delay).send_keys('1')
                # auto hide
                self.browser.find_element(*self.auto_hide).click()
                self.browser.find_element(*self.hide_after).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.hide_after).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.hide_after).send_keys('20')
            else:
                # delay before
                self.browser.find_element(*self.delay_before_first_notification).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.delay_before_first_notification).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.delay_before_first_notification).send_keys('1')
                # display for
                self.browser.find_element(*self.display_for).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.display_for).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.display_for).send_keys('5')
                # delay between
                self.browser.find_element(*self.delay_between).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.delay_between).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.delay_between).send_keys('2')

            if src != 'nxbarel' and src != 'nxbar':
                # sound
                self.browser.find_element(*self.sound).click()
                self.browser.find_element(*self.sound_choose).click()
            # behavior
            if src != 'nxbarel' and src != 'nxbar':
                # display last
                self.browser.find_element(*self.display_last).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.display_last).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.display_last).send_keys('5')
                # display form the last
                self.browser.find_element(*self.display_form).send_keys(Keys.CONTROL, 'a')
                self.browser.find_element(*self.display_form).send_keys(Keys.BACKSPACE)
                self.browser.find_element(*self.display_form).send_keys('2')
                # loop
                self.double_clicks(self.loop)
            if src != 'contact' and src != 'email_subs' and src != 'nxbarel':
                # open link in a new tab
                self.browser.find_element(*self.link_open).click()

            # publishing notification
            self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(1.5)
            self.browser.find_element(*self.publish_btn).click()

            element = WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located((By.XPATH, self.success_notice)))

            assert_that(element.text).is_equal_to("Successfully Created.")
