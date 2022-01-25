from utils.create_notice_helper import *
import utils.config as conf


class PageAnalytics(Helper):
    p_ana = (By.XPATH, f"//label[@for='wprf-input-radio-0-9']")
    p_ana_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-1']")
    p_ana_product_type = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-inline-label "
                                     f"wprf-name-wp_reviews_product_type']//div[@class='wprf-select-wrapper']")
    # 1st
    p_ana_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    p_ana_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    p_ana_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    p_ana_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-third_param']")
    p_ana_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    p_ana_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-text wprf-label-none "
                                          f"wprf-name-ga_fourth_param']//input[@id='notification-template']")
    # 5th
    p_ana_template_5th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-text wprf-label-none "
                                          f"wprf-name-ga_fifth_param']//input[@id='notification-template']")
    # 6th
    p_ana_template_6th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-label-none "
                                          f"wprf-name-sixth_param']")
    p_ana_choose_6th_param = (By.ID, f'react-select-15-option-1')

    p_ana_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    p_ana_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                        f"//label[@for='template_adv']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_page_analytics_notice(self, pos):
        self.browser.find_element(*self.nx_title).send_keys('NX Page Analytics Notification')

        # source page
        self.browser.find_element(*self.p_ana).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.p_ana_template).click()
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # 1st param
        self.browser.find_element(*self.p_ana_template_1st_param).click()
        self.browser.find_element(*self.p_ana_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.p_ana_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.p_ana_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.p_ana_template_2nd_param).send_keys('Reviewed')
        # 3rd param
        self.browser.find_element(*self.p_ana_template_3rd_param).click()
        self.browser.find_element(*self.p_ana_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.p_ana_template_4th_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.p_ana_template_4th_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.p_ana_template_4th_param).send_keys('In The Last')
        # 5th param
        self.browser.find_element(*self.p_ana_template_5th_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.p_ana_template_5th_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.p_ana_template_5th_param).send_keys('30')
        # 6th param
        self.browser.find_element(*self.p_ana_template_6th_param).click()
        self.browser.find_element(*self.p_ana_choose_6th_param).click()
        # advanced template
        self.browser.find_element(*self.p_ana_show_advanced_template).click()
        self.browser.find_element(*self.p_ana_hide_advanced_template).click()

        # common tasks
        self.do_others('analytics', pos)
