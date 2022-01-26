import time

from utils.create_notice_helper import *
import utils.config as conf


class Inline(Helper):
    inline = (By.XPATH, f"//label[@for='wprf-input-radio-0-11']")
    inline_woo = (By.XPATH, f"//label[@for='wprf-input-radio-1-0']")
    inline_edd = (By.XPATH, f"//label[@for='wprf-input-radio-1-1']")
    inline_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-0']")
    # 1st
    inline_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    inline_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    inline_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    inline_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-third_param']")
    inline_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    inline_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-fourth_param']")
    inline_choose_4th_param = (By.ID, f'react-select-14-option-3')

    inline_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    inline_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    inline_show_purchase_of = (By.XPATH, f"//div[@id='product_control']")
    inline_show_purchase_of_choose = (By.ID, 'react-select-15-option-0')
    inline_exclude_by = (By.XPATH, f"//div[@id='product_exclude_by']")
    inline_exclude_by_choose = (By.ID, 'react-select-16-option-0')
    inline_order_status = (By.XPATH, f"//div[@id='order_status']//div[@class='wprf-select__indicator "
                                   f"wprf-select__dropdown-indicator css-tlfecz-indicatorContainer']//*[name()='svg']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_inline_notice(self, src):
        self.browser.find_element(*self.nx_title).send_keys('NX Inline (' + src.upper() + ') Notification')

        # source page
        self.browser.find_element(*self.inline).click()
        self.browser.find_element(*self.inline_woo).click() if src.__eq__("woo") else \
            self.browser.find_element(*self.inline_edd).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.inline_template).click()
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # 1st param
        self.browser.find_element(*self.inline_template_1st_param).click()
        self.browser.find_element(*self.inline_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.inline_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.inline_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.inline_template_2nd_param).send_keys('People Purchased')
        # 3rd param
        self.browser.find_element(*self.inline_template_3rd_param).click()
        self.browser.find_element(*self.inline_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.inline_template_4th_param).click()
        self.browser.find_element(*self.inline_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.inline_show_advanced_template).click()
        self.browser.find_element(*self.inline_hide_advanced_template).click()
        # show purchased of
        self.browser.find_element(*self.inline_show_purchase_of).click()
        self.browser.find_element(*self.inline_show_purchase_of_choose).click()
        # exclude by
        self.browser.find_element(*self.inline_exclude_by).click()
        self.browser.find_element(*self.inline_exclude_by_choose).click()
        if src.__eq__("woo"):
            # order status
            self.browser.find_element(*self.inline_order_status).click()
            self.browser.find_element(*self.inline_show_purchase_of).click()
        # common tasks
        self.do_others('inline', 'null', 'null')
