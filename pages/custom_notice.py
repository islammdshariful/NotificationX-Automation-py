from utils.create_notice_helper import *
import utils.config as conf


class Custom(Helper):
    custom = (By.XPATH, f"//label[@for='wprf-input-radio-0-10']")
    custom_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-1']")
    # 1st
    custom_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                           f'wprf-label-none wprf-name-first_param"]')
    custom_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    custom_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    custom_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                           f"wprf-label-none wprf-name-third_param']")
    custom_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    custom_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                           f"wprf-label-none wprf-name-fourth_param']")
    custom_choose_4th_param = (By.ID, f'react-select-14-option-1')

    custom_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                               f"//label[@for='template_adv']")
    custom_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                               f"wprf-label-position-right']//label[@for='template_adv']")
    add_new_btn = (By.XPATH, f"//button[@class='wprf-repeater-button']")
    duplicate_btn = (By.XPATH, f"//div[@class='wprf-repeater-control']//div[2]//div[1]//div[1]//span[1]")
    # ID 0
    id_0_title = (By.XPATH, f"//input[@id='field-0-0-0']")
    id_0_fname = (By.XPATH, f"//input[@id='field-0-0-5']")
    id_0_lname = (By.XPATH, f"//input[@id='field-0-0-6']")
    id_0_email = (By.XPATH, f"//input[@id='field-0-0-7']")
    id_0_url = (By.XPATH, f"//input[@id='field-0-0-12']")
    id_0_time = (By.XPATH, f"//div[@class='wprf-repeater-content']//div[1]//div[2]//div[7]//div[2]//div[1]")
    # ID 1
    id_1_title = (By.XPATH, f"//input[@id='field-1-1-0']")
    id_1_fname = (By.XPATH, f"//input[@id='field-1-1-5']")
    id_1_lname = (By.XPATH, f"//input[@id='field-1-1-6']")
    id_1_email = (By.XPATH, f"//input[@id='field-1-1-7']")
    id_1_url = (By.XPATH, f"//input[@id='field-1-1-12']")
    id_1_time = (By.XPATH, f"//body[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
                           f"/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div[7]"
                           f"/div[2]/div[1]")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_custom_notice(self, qm, pos):
        self.browser.find_element(*self.nx_title).send_keys('NX Custom Notification')

        # source page
        self.browser.find_element(*self.custom).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.custom_template).click()
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # 1st param
        self.browser.find_element(*self.custom_template_1st_param).click()
        self.browser.find_element(*self.custom_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.custom_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.custom_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.custom_template_2nd_param).send_keys('Subscribed To')
        # 3rd param
        self.browser.find_element(*self.custom_template_3rd_param).click()
        self.browser.find_element(*self.custom_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.custom_template_4th_param).click()
        self.browser.find_element(*self.custom_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.custom_show_advanced_template).click()
        self.browser.find_element(*self.custom_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()

        # ID 0
        self.browser.find_element(*self.id_0_title).send_keys("NotificationX FREE Blog")
        self.browser.find_element(*self.id_0_fname).send_keys("Mr.")
        self.browser.find_element(*self.id_0_lname).send_keys("A")
        self.browser.find_element(*self.id_0_email).send_keys("mr.a@example.com")
        self.browser.find_element(*self.id_0_url).send_keys("www.example.com")
        self.browser.find_element(*self.id_0_time).click()
        self.browser.find_element(*self.add_new_btn).click()
        # ID 1
        self.browser.find_element(*self.id_1_title).send_keys("NotificationX PRO Blog")
        self.browser.find_element(*self.id_1_fname).send_keys("Mr.")
        self.browser.find_element(*self.id_1_lname).send_keys("B")
        self.browser.find_element(*self.id_1_email).send_keys("mr.b@example.com")
        self.browser.find_element(*self.id_1_url).send_keys("www.example.com")
        self.browser.find_element(*self.id_1_time).click()
        # Duplicated
        self.browser.find_element(*self.duplicate_btn).click()

        # common tasks
        self.do_others('custom', qm, pos)
