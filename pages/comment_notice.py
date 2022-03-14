from selenium.webdriver.common.keys import Keys
from utils.create_notice_helper import *
import utils.config as conf


class Comment(Helper):
    comment = (By.XPATH, f"//label[@for='wprf-input-radio-0-1']")
    comment_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-4']")
    # 1st
    comment_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                            f'wprf-label-none wprf-name-first_param"]')
    comment_choose_1st_param = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    # 2nd
    comment_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    comment_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                            f"wprf-label-none wprf-name-third_param']")
    comment_choose_3rd_param = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    # 4th
    comment_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                            f"wprf-label-none wprf-name-fourth_param']")
    comment_choose_4th_param = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")

    comment_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                                f"//label[@for='template_adv']")
    comment_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                                f"wprf-label-position-right']//label[@for='template_adv']")
    comment_content_length = (By.XPATH, f"//input[@id='content_trim_length']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_comment_notice(self, advanced_design, queue_management, position):
        h = Helper(self.browser)

        self.browser.find_element(*self.nx_title).send_keys('NX Comment Notification')

        # source page
        self.browser.find_element(*self.comment).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.comment_template).click()
        if advanced_design.__eq__('y'):
            self.check_advanced_design('comment')
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.comment_template_1st_param).click()
        self.browser.find_element(*self.comment_choose_1st_param).click()
        # nt template
        self.browser.find_element(*self.comment_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.comment_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.comment_template_2nd_param).send_keys('Commented on')
        # 2nd
        self.browser.find_element(*self.comment_template_3rd_param).click()
        self.browser.find_element(*self.comment_choose_3rd_param).click()
        # 3rd
        self.browser.find_element(*self.comment_template_4th_param).click()
        self.browser.find_element(*self.comment_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.comment_show_advanced_template).click()
        self.browser.find_element(*self.comment_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()
        # content length
        self.browser.find_element(*self.comment_content_length).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.comment_content_length).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.comment_content_length).send_keys('20')
        # random order
        self.browser.find_element(*self.random_order).click()

        # common tasks
        h.do_others('comment', advanced_design, queue_management, position)
