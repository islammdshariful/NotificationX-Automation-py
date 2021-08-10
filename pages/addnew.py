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
    SALE_NAME = (By.ID, f'react-select-9-option-2')
    SALE_TEXT = (By.ID, f'notification-template')
    SALE_TITLE = (By.ID, f'react-select-10-option-1')
    SALE_TIME = (By.ID, f'react-select-11-option-1')
    SALE_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div/div[2]/div/label')
    SALE_RANDOM_ORDER = (By.ID, f'random_order')
    SALE_SHOW_PURCHASE_OF = (By.ID, f'react-select-12-option-0')
    SALE_EXCLUDE_BY = (By.ID, f'react-select-13-option-0')
    SALE_MULTI_ORDER = (By.ID, f'combine_multiorder')
    SALE_MULTI_ORDER_TEXT = (By.ID, f'combine_multiorder_text')

    # comment notification
    COMMENT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[2]/div/label')
    COMMENT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[5]/div/label/img')
    COMMENT_NAME = (By.ID, f'react-select-9-option-2')
    COMMENT_TEXT = (By.ID, f'notification-template')
    COMMENT_TITLE = (By.ID, f'react-select-10-option-1')
    COMMENT_TIME = (By.ID, f'react-select-11-option-1')
    COMMENT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div/div[2]/div/label')
    COMMENT_RANDOM_ORDER = (By.ID, f'random_order')
    COMMENT_CONTENT_LENGHT = (By.ID, f'content_trim_length')

    # review notification
    REVIEW = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[3]/div/label')
    REVIEW_ORG = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    REVIEW_WOO = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[2]/div/label/img')
    REVIEW_TEMPLATE = (By.ID, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[2]/div/label/img')
    # org
    REVIEW_USERNAME = (By.ID, f'')
    REVIEW_TEXT = (By.ID, f'')
    REVIEW_RATING = (By.ID, f'')

    # review notification - woo



    DOWNLOAD_STAT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[4]/div/label')

    ELEARNING = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[5]/div/label')
    ELEARNING_TUTOR = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')

    DONATION = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[6]/div/label')

    NXBAR = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[7]/div/label')

    CONTACT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[8]/div/label')

    CONTACT_CF7 = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label')
    CONTACT_WPF = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[2]/div/label')
    CONTACT_NIN = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[3]/div/label')
    CONTACT_GRA = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[4]/div/label/div')

    EMAIL = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[9]/div/label')
    EMAIL_MC = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label')

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

        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.find_element(*self.NEXT_1).click()

        # display page
        self.browser.find_element(*self.NEXT_1).click()

        # publishing notification
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.PUBLISH).click()
