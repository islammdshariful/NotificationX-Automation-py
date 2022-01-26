import time

from utils.create_notice_helper import *
import utils.config as conf


class Sale(Helper):
    sale = (By.XPATH, f"//label[@for='wprf-input-radio-0-0']")
    sale_woo = (By.XPATH, f"//label[@for='wprf-input-radio-1-0']")
    sale_edd = (By.XPATH, f"//label[@for='wprf-input-radio-1-1']")
    sale_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-4']")
    # 1st
    sale_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    sale_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    sale_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    sale_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-third_param']")
    sale_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    sale_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-fourth_param']")
    sale_choose_4th_param = (By.ID, f'react-select-14-option-1')

    sale_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    sale_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    sale_show_purchase_of = (By.XPATH, f"//div[@id='product_control']")
    sale_show_purchase_of_choose = (By.ID, 'react-select-15-option-0')
    sale_exclude_by = (By.XPATH, f"//div[@id='product_exclude_by']")
    sale_exclude_by_choose = (By.ID, 'react-select-16-option-0')
    sale_order_status = (By.XPATH, f"//div[@id='order_status']//div[@class='wprf-select__indicator "
                                   f"wprf-select__dropdown-indicator css-tlfecz-indicatorContainer']//*[name()='svg']")
    sale_hide_order_status = (By.XPATH, f"//div[@id='order_status']//div[@class='wprf-select__indicator "
                                   f"wprf-select__dropdown-indicator css-tlfecz-indicatorContainer']//*[name()='svg']")
    sale_order_choose_hold = (By.ID, 'react-select-16-option-0')
    sale_multi_order = (By.XPATH, f"//input[@id='combine_multiorder']")
    sale_multi_order_text = (By.XPATH, f"//input[@id='combine_multiorder_text']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_sale_notice(self, src, advanced_design, queue_management, position):

        self.browser.find_element(*self.nx_title).send_keys('NX Sale (' + src.upper() + ') Notification')

        # source page
        self.browser.find_element(*self.sale).click()
        self.browser.find_element(*self.sale_woo).click() if src.__eq__("woo") else \
            self.browser.find_element(*self.sale_edd).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.sale_template).click()
        if advanced_design.__eq__('y'):
            self.check_advanced_design('sale')
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        # 1st param
        self.browser.find_element(*self.sale_template_1st_param).click()
        self.browser.find_element(*self.sale_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.sale_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.sale_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.sale_template_2nd_param).send_keys('purchased')
        # 3rd param
        self.browser.find_element(*self.sale_template_3rd_param).click()
        self.browser.find_element(*self.sale_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.sale_template_4th_param).click()
        self.browser.find_element(*self.sale_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.sale_show_advanced_template).click()
        self.browser.find_element(*self.sale_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()
        # show purchased of
        self.browser.find_element(*self.sale_show_purchase_of).click()
        self.browser.find_element(*self.sale_show_purchase_of_choose).click()
        # exclude by
        self.browser.find_element(*self.sale_exclude_by).click()
        self.browser.find_element(*self.sale_exclude_by_choose).click()
        if src.__eq__("woo"):
            # order status
            self.browser.find_element(*self.sale_order_status).click()
            self.browser.find_element(*self.sale_show_purchase_of).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        # multi order
        self.browser.find_element(*self.sale_multi_order).click()
        self.browser.find_element(*self.sale_multi_order).click()
        self.browser.find_element(*self.sale_multi_order_text).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.sale_multi_order_text).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.sale_multi_order_text).send_keys('& more product')

        # common tasks
        self.do_others('sale', advanced_design, queue_management, position)
