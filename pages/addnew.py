from selenium.webdriver.common.by import By
import utils.config as conf


class AddNew:
    ADD_NEW = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[1]/div[1]/div/a')
    NX_TITLE = (By.ID, f'nx-title')
    NEXT_0 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button')
    NEXT_1 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button[2]')
    PUBLISH = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div['
                         f'2]/div[2]/button')

    # common fields
    NT_TEMPLATE_TEXT = (By.ID, f'notification-template')
    RANDOM_ORDER = (By.ID, f'random_order')
    LINK_TYPE = (By.XPATH, f'react-select-8-option-2')
    UTM_CAMPAIGN = (By.ID, f'utm_campaign')
    UTM_MEDIUM = (By.ID, f'utm_medium')
    UTM_SOURCE = (By.ID, f'utm_source')
    SHOW_DEFAULT_IMAGE = (By.ID, f'show_default_image')
    DEFAULT_IMAGE = (By.XPATH, f'//*[@id="display_tab"]/div[1]/div[2]/div[2]/div[2]/div/div/div[5]/div/label/img')
    FEATURE_IMAGE = (By.ID, f'react-select-7-option-1')
    GRAVATAR_IMAGE = (By.ID, f'react-select-7-option-2')
    MAP_IMAGE = (By.ID, f'react-select-7-option-3')
    SHOW_ON = (By.ID, f'react-select-2-option-0')
    DISPLAY_FOR = (By.ID, f'react-select-3-option-0')
    POSITION_LEFT = (By.ID, f'react-select-4-option-0')
    POSITION_RIGHT = (By.ID, f'react-select-4-option-1')
    NOTIFICATION_SIZE = (By.ID, f'size')
    CLOSE_BUTTON = (By.ID, f'close_button')
    HIDE_ON_MOBILE = (By.ID, f'hide_on_mobile')
    GLOBAL_QUEUE = (By.ID, f'global_queue')
    DELAY_BEFORE = (By.ID, f'delay_before')
    DISPLAY_FOR = (By.ID, f'display_for')
    DELAY_BETWEEN = (By.ID, f'delay_between')
    DISPLAY_LAST = (By.ID, f'display_last')
    DISPLAY_FORM = (By.ID, f'display_from')
    LOOP = (By.ID, f'loop')
    LINK_OPEN = (By.ID, f'link_open')

    # Sale notification
    SALE = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[1]/div/label')
    SALE_WOO = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    SALE_EDD = (By.XPATH, f'//*[@id="source_tab"]/div[3]/div[2]/div/div/div/div/div[2]/div/label/img')
    SALE_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[4]/div/label/div')
    SALE_1ST = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    SALE_1ST_CHOOSE = (By.ID, f'react-select-9-option-2')
    SALE_2ND = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    SALE_2ND_CHOOSE = (By.ID, f'react-select-10-option-1')
    SALE_3RD = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    SALE_3RD_CHOOSE = (By.ID, f'react-select-11-option-1')
    SALE_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div/div[2]/div/label')
    SALE_SHOW_PURCHASE_OF = (By.XPATH, f'//*[@id="product_control"]/div/div[2]/div/svg')
    SALE_SHOW_PURCHASE_OF_CHOOSE = (By.ID, f'react-select-12-option-0')
    SALE_EXCLUDE_BY = (By.XPATH, f'//*[@id="product_exclude_by"]/div/div[2]/div/svg')
    SALE_EXCLUDE_BY_CHOOSE = (By.ID, f'react-select-13-option-0')
    SALE_MULTI_ORDER = (By.ID, f'combine_multiorder')
    SALE_MULTI_ORDER_TEXT = (By.ID, f'combine_multiorder_text')

    # comment notification
    COMMENT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[2]/div/label')
    COMMENT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[5]/div/label/img')
    COMMENT_1ST = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    COMMENT_1ST_CHOOSE = (By.ID, f'react-select-9-option-2')
    COMMENT_2ND = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    COMMENT_2ND_CHOOSE = (By.ID, f'react-select-10-option-1')
    COMMENT_3RD = (By.XPATH, f'//*[@id="notification-template"]/div/div[2]/div/svg')
    COMMENT_3RD_CHOOSE = (By.ID, f'react-select-11-option-1')
    COMMENT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div/div[2]/div/label')
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

    def add_sale_notification(self, src):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Sale Notification')

        # source page
        self.browser.find_element(*self.SALE).click()
        self.browser.find_element(*self.SALE_WOO).click() if src == "woo" else \
            self.browser.find_element(*self.SALE_EDD).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.find_element(*self.SALE_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        # 1st
        self.browser.find_element(*self.SALE_1ST).click()
        self.browser.find_element(*self.SALE_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).click().clear().send_keys('Kine fello')
        # 2nd
        self.browser.find_element(*self.SALE_2ND).click()
        self.browser.find_element(*self.SALE_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.SALE_3RD).click()
        self.browser.find_element(*self.SALE_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.SALE_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.SALE_ADVANCED_TEMPLATE).click()
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
        self.browser.find_element(*self.SALE_MULTI_ORDER_TEXT).click().clear().send_keys('Aro onek kichu')
        # next page display
        self.browser.find_element(*self.NEXT_1).click()

        # display page
        # next page customize
        self.browser.find_element(*self.NEXT_1).click()

        # customize page


        # publishing notification
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.PUBLISH).click()
