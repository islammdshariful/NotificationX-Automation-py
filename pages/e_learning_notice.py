from utils.create_notice_helper import *
import utils.config as conf


class ELearning(Helper):
    e_learn = (By.XPATH, f"//label[@for='wprf-input-radio-0-4']")
    e_learn_tutor = (By.XPATH, f"//label[@for='wprf-input-radio-1-0']")
    e_learn_ld = (By.XPATH, f"//label[@for='wprf-input-radio-1-1']")
    e_learn_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-4']")
    # 1st
    e_learn_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                            f'wprf-label-none wprf-name-first_param"]')
    e_learn_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    e_learn_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    e_learn_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                            f"wprf-label-none wprf-name-third_param']")
    e_learn_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    e_learn_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                            f"wprf-label-none wprf-name-fourth_param']")
    e_learn_choose_4th_param = (By.ID, f'react-select-14-option-1')

    e_learn_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                                f"//label[@for='template_adv']")
    e_learn_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                                f"wprf-label-position-right']//label[@for='template_adv']")
    e_learn_show_purchase_of = (By.XPATH, f"//div[@id='ld_product_control']")
    sale_show_purchase_of_choose = (By.ID, 'react-select-15-option-0')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_e_learning_notice(self, src, advanced_design, queue_management, position):
        self.browser.find_element(*self.nx_title).send_keys('NX Sale (' + src.upper() + ') Notification')

        # source page
        self.browser.find_element(*self.e_learn).click()
        self.browser.find_element(*self.e_learn_tutor).click() if src.__eq__("tutor") else \
            self.browser.find_element(*self.e_learn_ld).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.e_learn_template).click()
        if advanced_design.__eq__('y'):
            self.check_advanced_design(src)
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # 1st param
        self.browser.find_element(*self.e_learn_template_1st_param).click()
        self.browser.find_element(*self.e_learn_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.e_learn_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.e_learn_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.e_learn_template_2nd_param).send_keys('Enrolled in')
        # 3rd param
        self.browser.find_element(*self.e_learn_template_3rd_param).click()
        self.browser.find_element(*self.e_learn_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.e_learn_template_4th_param).click()
        self.browser.find_element(*self.e_learn_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.e_learn_show_advanced_template).click()
        self.browser.find_element(*self.e_learn_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()
        # show purchased of
        self.browser.find_element(*self.e_learn_show_purchase_of).click()
        self.browser.find_element(*self.sale_show_purchase_of_choose).click()

        # common tasks
        self.do_others('tutor', advanced_design, queue_management, position)
