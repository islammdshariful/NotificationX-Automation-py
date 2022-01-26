from utils.create_notice_helper import *
import utils.config as conf


class Review(Helper):
    review = (By.XPATH, f"//label[@for='wprf-input-radio-0-2']")
    review_org = (By.XPATH, f"//label[@for='wprf-input-radio-1-0']")
    review_woo = (By.XPATH, f"//label[@for='wprf-input-radio-1-1']")
    review_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-1']")
    review_product_type = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select wprf-inline-label "
                                     f"wprf-name-wp_reviews_product_type']//div[@class='wprf-select-wrapper']")
    review_choose_product_type = (By.ID, f'react-select-15-option-0')
    review_product_slug = (By.XPATH, f"//input[@id='wp_reviews_slug']")
    # 1st
    review_template_1st_param = (By.XPATH, f'//div[@class="wprf-control-wrapper wprf-type-select '
                                         f'wprf-label-none wprf-name-first_param"]')
    review_choose_1st_param = (By.ID, f'react-select-12-option-1')
    # 2nd
    review_template_2nd_param = (By.XPATH, f"//input[@id='notification-template']")
    # 3rd
    review_template_3rd_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-third_param']")
    review_choose_3rd_param = (By.ID, f'react-select-13-option-1')
    # 4th
    review_template_4th_param = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-select "
                                         f"wprf-label-none wprf-name-fourth_param']")
    review_choose_4th_param = (By.ID, f'react-select-14-option-2')

    review_show_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    review_hide_advanced_template = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                        f"//label[@for='template_adv']")
    review_show_purchase_of = (By.XPATH, f"//div[@id='product_control']")
    review_show_purchase_of_choose = (By.ID, 'react-select-16-option-0')
    review_exclude_by = (By.XPATH, f"//div[@id='product_exclude_by']")
    review_exclude_by_choose = (By.ID, 'react-select-17-option-0')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.add_new).click()

    def create_review_notice(self, src, advanced_design, queue_management, position):
        self.browser.find_element(*self.nx_title).send_keys('NX Review (' + src.upper() + ') Notification')

        # source page
        self.browser.find_element(*self.review).click()
        self.browser.find_element(*self.review_woo).click() if src.__eq__("woo-review") else \
            self.browser.find_element(*self.review_org).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        self.browser.find_element(*self.review_template).click()
        if advanced_design.__eq__('y'):
            self.check_advanced_design(src)
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        if src.__eq__("org-review"):
            # product type
            self.browser.find_element(*self.review_product_type).click()
            self.browser.find_element(*self.review_choose_product_type).click()
            self.browser.find_element(*self.review_product_slug).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.review_product_slug).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.review_product_slug).send_keys('essential-addons-for-elementor-lite')
        # 1st param
        self.browser.find_element(*self.review_template_1st_param).click()
        self.browser.find_element(*self.review_choose_1st_param).click()
        # 2nd param
        self.browser.find_element(*self.review_template_2nd_param).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.review_template_2nd_param).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.review_template_2nd_param).send_keys('Reviewed')
        # 3rd param
        self.browser.find_element(*self.review_template_3rd_param).click()
        self.browser.find_element(*self.review_choose_3rd_param).click()
        # 4th param
        self.browser.find_element(*self.review_template_4th_param).click()
        self.browser.find_element(*self.review_choose_4th_param).click()
        # advanced template
        self.browser.find_element(*self.review_show_advanced_template).click()
        self.browser.find_element(*self.review_hide_advanced_template).click()
        # random order
        self.browser.find_element(*self.random_order).click()
        self.browser.find_element(*self.random_order).click()

        if src.__eq__("woo-review"):
            # show purchased of
            self.browser.find_element(*self.review_show_purchase_of).click()
            self.browser.find_element(*self.review_show_purchase_of_choose).click()
            # exclude by
            self.browser.find_element(*self.review_exclude_by).click()
            self.browser.find_element(*self.review_exclude_by_choose).click()

        # common tasks
        self.do_others(src, advanced_design, queue_management, position)
