from utils.create_notice_helper import *
import utils.config as conf


class EmailSubscription(Helper):
    e_subs = (By.XPATH, f"//label[@for='wprf-input-radio-0-8']")
    e_subs_mc = (By.XPATH, f"//label[@for='wprf-input-radio-1-0']")
    e_subs_ck = (By.XPATH, f"//label[@for='wprf-input-radio-1-1']")
    e_subs_zp = (By.XPATH, f"//label[@for='wprf-input-radio-1-2']")
    e_subs_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-1']")
    e_subs_form_list = (By.XPATH, f"//div[@id='mailchimp_list']")
    e_subs_choose_form = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[1]")
    # 1st
    e_subs_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    e_subs_choose_1st_param = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[3]")
    # 2nd
    e_subs_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    e_subs_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-third_param']")
    e_subs_choose_3rd_param = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    # 4th
    e_subs_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-fourth_param']")
    e_subs_choose_4th_param = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")

    e_subs_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                                f"//label[@for='template_adv']")
    e_subs_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                                f"wprf-label-position-right']//label[@for='template_adv']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        self.browser.find_element(*self.add_new).click()

    def create_email_subs_notice(self, src, advanced_design, queue_management, position):
        self.browser.find_element(*self.nx_title).send_keys('NX Email Subscription (' + src.upper() + ') Notification')

        # source page
        self.browser.find_element(*self.e_subs).click()
        if src.__eq__("mc"):
            self.browser.find_element(*self.e_subs_mc).click()
        elif src.__eq__("ck"):
            self.browser.find_element(*self.e_subs_ck).click()
        else:
            self.browser.find_element(*self.e_subs_zp).click()

        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        self.browser.find_element(*self.e_subs_template).click()
        if advanced_design.__eq__('y'):
            self.check_advanced_design('email')
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        # Form List
        self.browser.find_element(*self.e_subs_form_list).click()
        self.browser.find_element(*self.e_subs_choose_form).click()
        # 1st param
        self.browser.find_element(*self.e_subs_template_1st_param).click()
        self.browser.find_element(*self.e_subs_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.e_subs_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.e_subs_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.e_subs_template_2nd_param).send_keys('Subscribed To')
        # 3rd param
        self.browser.find_element(*self.e_subs_template_3rd_param).click()
        self.browser.find_element(*self.e_subs_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.e_subs_template_4th_param).click()
        self.browser.find_element(*self.e_subs_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.e_subs_show_advanced_template).click()
        self.browser.find_element(*self.e_subs_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()

        # common tasks
        self.do_others("email_subs", advanced_design, queue_management, position)
