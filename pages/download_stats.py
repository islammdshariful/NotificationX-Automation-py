from utils.create_notice_helper import *
import utils.config as conf


class DownloadStats(Helper):
    d_stats = (By.XPATH, f"//label[@for='wprf-input-radio-0-3']")
    d_stats_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-1']")
    d_stats_product_type = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-inline-label "
                                      f"wprf-name-wp_stats_product_type']//div[@class='wprf-select-wrapper']")
    d_stats_choose_product_type = (By.ID, f'react-select-15-option-0')

    d_stats_product_slug = (By.XPATH, f"//input[@id='wp_stats_slug']")
    # 1st
    d_stats_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                            f'wprf-label-none wprf-name-first_param"]')
    d_stats_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    d_stats_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    d_stats_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                            f"wprf-label-none wprf-name-third_param']")
    d_stats_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    d_stats_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                            f"wprf-label-none wprf-name-fourth_param']")
    d_stats_choose_4th_param = (By.ID, f'react-select-14-option-2')

    d_stats_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                                f"//label[@for='template_adv']")
    d_stats_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked "
                                                f"wprf-label-position-right']//label[@for='template_adv']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_d_stats_notice(self, qm, pos):
        self.browser.find_element(*self.nx_title).send_keys('NX Download Stats Notification')

        # source page
        self.browser.find_element(*self.d_stats).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.d_stats_template).click()
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # product type
        self.browser.find_element(*self.d_stats_product_type).click()
        self.browser.find_element(*self.d_stats_choose_product_type).click()
        self.browser.find_element(*self.d_stats_product_slug).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.d_stats_product_slug).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.d_stats_product_slug).send_keys('essential-addons-for-elementor-lite')
        # 1st param
        self.browser.find_element(*self.d_stats_template_1st_param).click()
        self.browser.find_element(*self.d_stats_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.d_stats_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.d_stats_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.d_stats_template_2nd_param).send_keys('Downloaded')
        # 3rd param
        self.browser.find_element(*self.d_stats_template_3rd_param).click()
        self.browser.find_element(*self.d_stats_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.d_stats_template_4th_param).click()
        self.browser.find_element(*self.d_stats_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.d_stats_show_advanced_template).click()
        self.browser.find_element(*self.d_stats_hide_advanced_template).click()

        # common tasks
        self.do_others('d_stat', qm, pos)
