import time

from utils.create_notice_helper import *
import utils.config as conf


class Donation(Helper):
    donation = (By.XPATH, f"//label[@for='wprf-input-radio-0-5']")
    donation_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-4']")
    # 1st
    donation_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    donation_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    donation_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    donation_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-label-none "
                                             f"wprf-name-third_param']")
    donation_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    donation_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-label-none "
                                             f"wprf-name-fourth_param']")
    donation_choose_4th_param = (By.ID, f'react-select-14-option-1')
    # 5th
    donation_template_5th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-label-none "
                                             f"wprf-name-fifth_param']")
    donation_choose_5th_param = (By.ID, f'react-select-16-option-1')

    donation_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    donation_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                                 f"wprf-label-position-right']//label[@for='template_adv']")
    donation_show_notification_of = (By.XPATH, f"//div[@id='give_forms_control']")
    donation_show_notification_of_choose = (By.ID, 'react-select-15-option-0')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_donation_notice(self, advanced_design, queue_management, position):
        self.browser.find_element(*self.nx_title).send_keys('NX Donation Notification')
        # source page
        self.browser.find_element(*self.donation).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.donation_template).click()
        if advanced_design.__eq__('y'):
            self.check_advanced_design('donation')
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        # 1st param
        self.browser.find_element(*self.donation_template_1st_param).click()
        self.browser.find_element(*self.donation_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.donation_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.donation_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.donation_template_2nd_param).send_keys('Donated')
        # 3rd param
        self.browser.find_element(*self.donation_template_3rd_param).click()
        self.browser.find_element(*self.donation_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.donation_template_4th_param).click()
        self.browser.find_element(*self.donation_choose_4th_param).click()
        # 4th param
        self.browser.find_element(*self.donation_template_5th_param).click()
        self.browser.find_element(*self.donation_choose_5th_param).click()
        # advanced template
        self.browser.find_element(*self.donation_show_advanced_template).click()
        self.browser.find_element(*self.donation_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()
        # show purchased of
        self.browser.find_element(*self.donation_show_notification_of).click()
        self.browser.find_element(*self.donation_show_notification_of_choose).click()

        # common tasks
        self.do_others('donation', advanced_design, queue_management, position)
