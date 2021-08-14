import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utils.config as conf


class AddNew:
    ADD_NEW = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[1]/div[1]/div/a')
    NX_TITLE = (By.ID, f'nx-title')
    NEXT_0 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button')
    NEXT_1 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button[2]')
    PUBLISH = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div['
                         f'2]/div[2]/button')

    # common fields
    NT_TEMPLATE_TEXT = (By.NAME, f'second_param')
    RANDOM_ORDER = (By.ID, f'random_order')
    LINK_TYPE = (By.XPATH, f'//*[@id="link_type"]/div/div[2]')
    LINK_TYPE_CHOOSE = (By.ID, f'react-select-9-option-2')
    UTM_CAMPAIGN = (By.ID, f'utm_campaign')
    UTM_MEDIUM = (By.ID, f'utm_medium')
    UTM_SOURCE = (By.ID, f'utm_source')
    SHOW_DEFAULT_IMAGE = (By.ID, f'show_default_image')
    DEFAULT_IMAGE = (By.XPATH, f'//*[@id="display_tab"]/div[1]/div[2]/div[2]/div[2]/div/div/div[5]/div/label/img')
    IMAGE = (By.XPATH, f'//*[@id="show_notification_image"]/div/div[2]')
    FEATURE_IMAGE_CHOOSE = (By.ID, f'react-select-8-option-1')
    COMMENT_GRAVATAR_IMAGE = (By.ID, f'react-select-8-option-1')
    GRAVATAR_IMAGE = (By.ID, f'react-select-8-option-2')
    MAP_IMAGE = (By.ID, f'react-select-8-option-3')
    SHOW_ON = (By.XPATH, f'//*[@id="show_on"]/div/div[2]')
    SHOW_ON_CHOOSE = (By.ID, f'react-select-2-option-0')
    DISPLAY_FOR = (By.XPATH, f'//*[@id="show_on_display"]/div/div[2]')
    DISPLAY_FOR_CHOOSE = (By.ID, f'react-select-3-option-0')
    POSITION = (By.XPATH, f'//*[@id="position"]/div/div[2]')
    POSITION_CHOOSE_LEFT = (By.ID, f'react-select-4-option-0')
    POSITION_CHOOSE_RIGHT = (By.ID, f'react-select-4-option-1')
    NOTIFICATION_SIZE = (By.ID, f'size')
    CLOSE_BUTTON = (By.ID, f'close_button')
    HIDE_ON_MOBILE = (By.ID, f'hide_on_mobile')
    GLOBAL_QUEUE = (By.ID, f'global_queue')
    DELAY_BEFORE = (By.ID, f'delay_before')
    DISPLAY_FOR = (By.ID, f'display_for')
    DELAY_BETWEEN = (By.ID, f'delay_between')
    SOUND = (By.XPATH, f'//*[@id="sound"]/div/div[2]')
    SOUND_CHOOSE = (By.ID, f'react-select-5-option-1')
    DISPLAY_LAST = (By.ID, f'display_last')
    DISPLAY_FORM = (By.ID, f'display_from')
    LOOP = (By.ID, f'loop')
    LINK_OPEN = (By.ID, f'link_open')

    SUCCESS_NOTICE = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/p')

    # Sale notification
    SALE = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2] /div/div/div/div/div[1]/div/label')
    SALE_WOO = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    SALE_EDD = (By.XPATH, f'//*[@id="source_tab"]/div[3]/div[2]/div/div/div/div/div[2]/div/label/img')
    SALE_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[4]/div/label/img')
    SALE_1ST = (By.XPATH,
                f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div['
                f'1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div')
    SALE_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    SALE_2ND = (By.XPATH,
                f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div['
                f'1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/div/div[2]/div')
    SALE_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    SALE_3RD = (By.XPATH,
                f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div['
                f'1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[2]/div')
    SALE_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    SALE_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    SALE_SHOW_PURCHASE_OF = (By.XPATH, f'//*[@id="product_control"]/div/div[2]')
    SALE_SHOW_PURCHASE_OF_CHOOSE = (By.ID, f'react-select-13-option-0')
    SALE_EXCLUDE_BY = (By.XPATH, f'//*[@id="product_exclude_by"]/div/div[2]')
    SALE_EXCLUDE_BY_CHOOSE = (By.ID, f'react-select-14-option-0')
    SALE_MULTI_ORDER = (By.ID, f'combine_multiorder')
    SALE_MULTI_ORDER_TEXT = (By.ID, f'combine_multiorder_text')

    # comment notification
    COMMENT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[2]/div/label')
    COMMENT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[5]/div/label/img')
    COMMENT_1ST = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
                             f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]')
    COMMENT_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    COMMENT_2ND = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
                             f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/div/div[2]')
    COMMENT_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    COMMENT_3RD = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
                             f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[2]')
    COMMENT_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    COMMENT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    COMMENT_CONTENT_LENGHT = (By.ID, f'content_trim_length')

    # review notification
    REVIEW = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[3]/div/label')
    REVIEW_ORG = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    REVIEW_WOO = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[2]/div/label/img')
    REVIEW_TEMPLATE = (By.ID, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[2]/div/label/img')
    # org
    REVIEW_WP_PRODUCT_TYPE = (By.XPATH, f'//*[@id="wp_reviews_product_type"]/div/div[2]/div/svg')
    REVIEW_WP_PRODUCT_TYPE_CHOOSE = (By.ID, f'react-select-13-option-0')
    REVIEW_WP_SLUG = (By.ID, f'wp_reviews_slug')
    REVIEW_WP_1ST = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    REVIEW_WP_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    REVIEW_WP_2ND = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    REVIEW_WP_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    REVIEW_WP_3RD = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    REVIEW_WP_3RD_CHOOSE = (By.ID, f'react-select-12-option-2')
    REVIEW_WP_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/div/label')
    # review notification - woo
    REVIEW_WOO_1ST = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    REVIEW_WOO_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    REVIEW_WOO_2ND = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    REVIEW_WOO_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    REVIEW_WOO_3RD = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    REVIEW_WOO_3RD_CHOOSE = (By.ID, f'react-select-12-option-2')
    REVIEW_WOO_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/div/label')

    # download notification
    DOWNLOAD_STAT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[4]/div/label')
    DOWNLOAD_STAT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[2]/div/label/img')
    DOWNLOAD_STAT_PRODUCT_TYPE = (By.XPATH, f'//*[@id="wp_stats_product_type"]/div/div[2]/div/svg')
    DOWNLOAD_STAT_PRODUCT_TYPE_CHOOSE = (By.ID, f'react-select-15-option-0')
    DOWNLOAD_STAT_PRODUCT_PLUGIN = (By.ID, f'react-select-13-option-0')
    DOWNLOAD_STAT_SLUG = (By.ID, f'wp_stats_slug')
    DOWNLOAD_STAT_1ST = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    DOWNLOAD_STAT_1ST_CHOOSE = (By.ID, f'react-select-9-option-1')
    DOWNLOAD_STAT_2ND = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    DOWNLOAD_STAT_2ND_CHOOSE = (By.ID, f'react-select-10-option-3')
    DOWNLOAD_STAT_3RD = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    DOWNLOAD_STAT_3RD_CHOOSE = (By.ID, f'react-select-11-option-3')
    DOWNLOAD_STAT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/div/label')

    # elearning notification
    ELEARNING = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[5]/div/label')
    ELEARNING_TUTOR = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    ELEARNING_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[4]/div/label/img')
    ELEARNING_1ST = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    ELEARNING_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    ELEARNING_2ND = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    ELEARNING_2ND_CHOOSE = (By.ID, f'react-select-25-option-1')
    ELEARNING_3RD = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    ELEARNING_3RD_CHOOSE = (By.ID, f'react-select-26-option-1')
    ELEARNING_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div/label')
    ELEARNING_SHOW_NOTIFICATION_OF = (By.XPATH, f'//*[@id="ld_product_control"]/div/div[2]/div/svg')
    ELEARNING_SHOW_NOTIFICATION_OF_CHOOSE = (By.ID, f'react-select-27-option-1')
    ELEARNING_SELECT_COURSE = (By.XPATH, f'//*[@id="ld_course_list"]/div[1]/div[2]/div/svg')
    ELEARNING_SELECT_COURSE_CHOOSE = (By.ID, f'react-select-35-option-0')

    # donation notification
    DONATION = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[6]/div/label')

    # notification bar
    NXBAR = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[7]/div/label')

    # contact notification
    CONTACT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[8]/div/label')

    CONTACT_CF7 = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label')
    CONTACT_WPF = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[2]/div/label')
    CONTACT_NIN = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[3]/div/label')
    CONTACT_GRA = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[4]/div/label/div')

    # email subscription
    EMAIL = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[9]/div/label')
    EMAIL_MC = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label')

    # custom notification
    CUSTOM = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[11]/div/label')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)

    def double_clicks(self, element):
        self.browser.find_element(*element).click()
        self.browser.find_element(*element).click()

    def common_task(self, src):
        # link type
        self.browser.find_element(*self.LINK_TYPE).click()
        self.browser.find_element(*self.LINK_TYPE_CHOOSE).click()
        # utm controls
        self.browser.find_element(*self.UTM_CAMPAIGN).send_keys('campaign_automation')
        self.browser.find_element(*self.UTM_MEDIUM).send_keys('medium_automation')
        self.browser.find_element(*self.UTM_SOURCE).send_keys('source_automation')

        # next page display
        self.browser.find_element(*self.NEXT_1).click()

        # image
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.SHOW_DEFAULT_IMAGE).click()
        self.browser.find_element(*self.SHOW_DEFAULT_IMAGE).click()
        self.browser.find_element(*self.IMAGE).click()
        self.browser.find_element(*self.COMMENT_GRAVATAR_IMAGE).click() if src == 'comment' else \
            self.browser.find_element(*self.FEATURE_IMAGE_CHOOSE).click()
        # visibility
        self.browser.find_element(*self.SHOW_ON).click()
        self.browser.find_element(*self.SHOW_ON_CHOOSE).click()
        # next page customize
        self.browser.find_element(*self.NEXT_1).click()

        # customize page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # appearance
        self.browser.find_element(*self.POSITION).click()
        self.browser.find_element(*self.POSITION_CHOOSE_RIGHT).click()
        # notification size
        self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys('400')
        # display close option
        self.double_clicks(self.CLOSE_BUTTON)
        self.double_clicks(self.HIDE_ON_MOBILE)
        # queue management
        self.double_clicks(self.GLOBAL_QUEUE)
        # timing
        # delay before
        self.browser.find_element(*self.DELAY_BEFORE).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.DELAY_BEFORE).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.DELAY_BEFORE).send_keys('1')
        # display for
        self.browser.find_element(*self.DISPLAY_FOR).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.DISPLAY_FOR).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.DISPLAY_FOR).send_keys('5')
        # delay between
        self.browser.find_element(*self.DELAY_BETWEEN).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.DELAY_BETWEEN).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.DELAY_BETWEEN).send_keys('2')
        # sound
        self.browser.find_element(*self.SOUND).click()
        self.browser.find_element(*self.SOUND_CHOOSE).click()
        # behavior
        # display last
        self.browser.find_element(*self.DISPLAY_LAST).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.DISPLAY_LAST).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.DISPLAY_LAST).send_keys('19')
        # display form the last
        self.browser.find_element(*self.DISPLAY_FORM).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.DISPLAY_FORM).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.DISPLAY_FORM).send_keys('20')
        # loop
        self.double_clicks(self.LOOP)
        # open link in a new tab
        self.browser.find_element(*self.LINK_OPEN).click()

        # publishing notification
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.PUBLISH).click()

        assert self.browser.find_element(*self.SUCCESS_NOTICE).text == 'Successfully Created.'

    def create_sale_notification(self, src):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Sale Notification')

        # source page
        self.browser.find_element(*self.SALE).click()
        self.browser.find_element(*self.SALE_WOO).click() if src == "woo" else \
            self.browser.find_element(*self.SALE_EDD).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.SALE_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.SALE_1ST).click()
        self.browser.find_element(*self.SALE_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Kine nilo')
        # 2nd
        self.browser.find_element(*self.SALE_2ND).click()
        self.browser.find_element(*self.SALE_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.SALE_3RD).click()
        self.browser.find_element(*self.SALE_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.SALE_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.SALE_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # show purchased of
        self.browser.find_element(*self.SALE_SHOW_PURCHASE_OF).click()
        self.browser.find_element(*self.SALE_SHOW_PURCHASE_OF_CHOOSE).click()
        # exclude by
        self.browser.find_element(*self.SALE_EXCLUDE_BY).click()
        self.browser.find_element(*self.SALE_EXCLUDE_BY_CHOOSE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # multi order
        self.browser.find_element(*self.SALE_MULTI_ORDER).click()
        self.browser.find_element(*self.SALE_MULTI_ORDER).click()
        self.browser.find_element(*self.SALE_MULTI_ORDER_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.SALE_MULTI_ORDER_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.SALE_MULTI_ORDER_TEXT).send_keys('Aro onek kichu')

        # common tasks
        self.common_task('sale')

    def create_comment_notification(self):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Comment Notification')

        # source page
        self.browser.find_element(*self.COMMENT).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.COMMENT_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.COMMENT_1ST).click()
        self.browser.find_element(*self.COMMENT_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Motamot dilo')
        # 2nd
        self.browser.find_element(*self.COMMENT_2ND).click()
        self.browser.find_element(*self.COMMENT_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.COMMENT_3RD).click()
        self.browser.find_element(*self.COMMENT_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.COMMENT_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.COMMENT_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # content length
        self.browser.find_element(*self.COMMENT_CONTENT_LENGHT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.COMMENT_CONTENT_LENGHT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.COMMENT_CONTENT_LENGHT).send_keys('15')

        # common tasks
        self.common_task('comment')
