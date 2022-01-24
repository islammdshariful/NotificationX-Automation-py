from utils.create_notice_helper import *
import utils.config as conf


class ContactForm(Helper):
    contact = (By.XPATH, f"//label[@for='wprf-input-radio-0-7']")
    contact_cf7 = (By.XPATH, f"//label[@for='wprf-input-radio-1-0']")
    contact_wpf = (By.XPATH, f"//label[@for='wprf-input-radio-1-1']")
    contact_nf = (By.XPATH, f"//label[@for='wprf-input-radio-1-2']")
    contact_gf = (By.XPATH, f"//label[@for='wprf-input-radio-1-3']")
    contact_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-1']")
    contact_form_list = (By.XPATH, f"//div[@id='form_list']")
    contact_choose_form = (By.ID, f'react-select-15-option-0')
    # 1st
    contact_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    contact_choose_1st_param = (By.ID, f'react-select-12-option-2')
    # 2nd
    contact_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    contact_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-third_param']")
    contact_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    contact_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-fourth_param']")
    contact_choose_4th_param = (By.ID, f'react-select-14-option-1')

    contact_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                                f"//label[@for='template_adv']")
    contact_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                                f"wprf-label-position-right']//label[@for='template_adv']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_review_notice(self, src, pos):
        self.browser.find_element(*self.nx_title).send_keys('NX Contact Form (' + src.upper() + ') Notification')

        # source page
        self.browser.find_element(*self.contact).click()
        if src.__eq__("cf7"):
            self.browser.find_element(*self.contact_cf7).click()
        elif src.__eq__("wpf"):
            self.browser.find_element(*self.contact_wpf).click()
        elif src.__eq__("nf"):
            self.browser.find_element(*self.contact_nf).click()
        else:
            self.browser.find_element(*self.contact_gf).click()

        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.contact_template).click()
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # Form List
        self.browser.find_element(*self.contact_form_list).click()
        self.browser.find_element(*self.contact_choose_form).click()
        # 1st param
        self.browser.find_element(*self.contact_template_1st_param).click()
        self.browser.find_element(*self.contact_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.contact_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.contact_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.contact_template_2nd_param).send_keys('Contacted Via')
        # 3rd param
        self.browser.find_element(*self.contact_template_3rd_param).click()
        self.browser.find_element(*self.contact_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.contact_template_4th_param).click()
        self.browser.find_element(*self.contact_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.contact_show_advanced_template).click()
        self.browser.find_element(*self.contact_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()

        # common tasks
        self.do_others("contact", pos)
