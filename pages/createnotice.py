from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utils.config as conf


class AddNew:
    ADD_NEW = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[1]/div[1]/div/a')
    NX_TITLE = (By.ID, f'nx-title')
    NEXT_0 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button')
    NEXT_1 = (By.XPATH, f'//*[@id="notificationx"]/div/div/div[2]/div[1]/div/div[2]/div[2]/button[2]')
    PUBLISH = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div['
                         f'2]/div[2]/button')

    # common fields
    CONTENT_1ST = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'1]/div/div/div/div/div[2]/div')
    CONTENT_2ND = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'3]/div/div/div/div/div[2]/div')
    CONTENT_3RD = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'4]/div/div/div/div/div[2]')
    CONTENT_4TH = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                             f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div['
                             f'5]/div/div/div/div/div[2]')
    CONTENT_1ST_REVIEW_DSTAT = (
        By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                  f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div['
                  f'1]/div/div/div/div/div[2]')
    CONTENT_2ND_REVIEW_DSTAT = (
        By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                  f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div['
                  f'3]/div/div/div/div/div[2]')
    CONTENT_3RD_REVIEW_DSTAT = (
        By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div['
                  f'1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div['
                  f'4]/div/div/div/div/div[2]')
    CONTENT_1ST_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div['
                                           f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
                                           f'2]/div/div/div[1]/div/div/div/div/div[2]')
    CONTENT_2ND_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div['
                                           f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
                                           f'2]/div/div/div[3]/div/div/div/div/div[2]')
    CONTENT_3RD_CONTACT_EMAIL = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div['
                                           f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div['
                                           f'2]/div/div/div[4]/div/div/div/div/div[2]')
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
    STICKY_BAR = (By.ID, f'sticky_bar')
    OVERLAPPING = (By.ID, f'pressbar_body')
    NOTIFICATION_SIZE = (By.ID, f'size')
    CLOSE_BUTTON = (By.ID, f'close_button')
    HIDE_ON_MOBILE = (By.ID, f'hide_on_mobile')
    GLOBAL_QUEUE = (By.ID, f'global_queue')
    DELAY_BEFORE = (By.ID, f'delay_before')
    DISPLAY_FOR = (By.ID, f'display_for')
    DELAY_BETWEEN = (By.ID, f'delay_between')
    INITIAL_DELAY = (By.ID, f'initial_delay')
    AUTO_HIDE = (By.ID, f'auto_hide')
    HIDE_AFTER = (By.ID, f'hide_after')
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
    SALE_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    SALE_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
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
    COMMENT_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    COMMENT_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    COMMENT_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    COMMENT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    COMMENT_CONTENT_LENGTH = (By.ID, f'content_trim_length')

    # review notification
    REVIEW = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[3]/div/label')
    REVIEW_ORG = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    REVIEW_WOO = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[2]/div/label/img')
    REVIEW_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[2]/div/label/img')
    # org
    REVIEW_WP_PRODUCT_TYPE = (By.XPATH, f'//*[@id="wp_reviews_product_type"]/div/div[2]/div')
    REVIEW_WP_PRODUCT_TYPE_CHOOSE = (By.ID, f'react-select-13-option-0')
    REVIEW_WP_SLUG = (By.ID, f'wp_reviews_slug')
    REVIEW_WP_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    REVIEW_WP_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    REVIEW_WP_3RD_CHOOSE = (By.ID, f'react-select-12-option-2')
    REVIEW_WP_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/div')
    # review notification - woo
    REVIEW_WOO_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    REVIEW_WOO_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    REVIEW_WOO_3RD_CHOOSE = (By.ID, f'react-select-12-option-2')
    REVIEW_WOO_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')

    # download notification
    DOWNLOAD_STAT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[4]/div/label')
    DOWNLOAD_STAT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[2]/div/label/img')
    DOWNLOAD_STAT_PRODUCT_TYPE = (By.XPATH, f'//*[@id="wp_stats_product_type"]/div/div[2]/div')
    DOWNLOAD_STAT_PRODUCT_PLUGIN_CHOOSE = (By.ID, f'react-select-13-option-0')
    DOWNLOAD_STAT_PRODUCT_THEME_CHOOSE = (By.ID, f'react-select-13-option-1')
    DOWNLOAD_STAT_SLUG = (By.ID, f'wp_stats_slug')
    DOWNLOAD_STAT_1ST_CHOOSE = (By.ID, f'react-select-10-option-1')
    DOWNLOAD_STAT_2ND_CHOOSE = (By.ID, f'react-select-11-option-3')
    DOWNLOAD_STAT_3RD_CHOOSE = (By.ID, f'react-select-12-option-3')
    DOWNLOAD_STAT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/div')

    # e-learning notification
    eLEARNING = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[5]/div/label')
    eLEARNING_TUTOR = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label/img')
    eLEARNING_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[4]/div/label/img')
    eLEARNING_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    eLEARNING_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    eLEARNING_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    eLEARNING_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    eLEARNING_SHOW_NOTIFICATION_OF = (By.XPATH, f'//*[@id="ld_product_control"]/div/div[2]/div')
    eLEARNING_SHOW_NOTIFICATION_OF_CHOOSE = (By.ID, f'react-select-13-option-1')
    eLEARNING_SELECT_COURSE = (By.XPATH, f'//*[@id="ld_course_list"]/div[1]/div[2]/div')
    eLEARNING_SELECT_COURSE_CHOOSE = (By.ID, f'react-select-14-option-0')

    # donation notification
    DONATION = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[6]/div/label')
    DONATION_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[4]/div/label/img')
    DONATION_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    DONATION_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    DONATION_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    DONATION_4TH_CHOOSE = (By.ID, f'react-select-14-option-1')

    DONATION_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    DONATION_SHOW_NOTIFICATION_OF = (By.XPATH, f'//*[@id="give_forms_control"]/div/div[2]')
    DONATION_SHOW_NOTIFICATION_OF_CHOOSE = (By.ID, f'react-select-13-option-1')
    DONATION_SELECT_FORM = (By.XPATH, f'//*[@id="give_form_list"]/div[1]/div[2]')
    DONATION_SELECT_FORM_CHOOSE = (By.ID, f'react-select-15-option-0')

    # notification bar
    NX_BAR = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[7]/div/label')

    # contact notification
    CONTACT = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[8]/div/label')
    CONTACT_CF7 = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label')
    CONTACT_WPF = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[2]/div/label')
    CONTACT_NIN = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[3]/div/label')
    CONTACT_GRA = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[4]/div/label')
    CONTACT_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[2]/div/label/img')
    CONTACT_FORM = (By.XPATH, f'//*[@id="form_list"]/div/div[2]')
    CONTACT_FORM_CHOOSE = (By.ID, f'react-select-13-option-0')
    CONTACT_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    CONTACT_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    CONTACT_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    CONTACT_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[3]/div[2]/div')

    # email subscription
    EMAIL = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[9]/div/label')
    EMAIL_MAILCHIMP = (By.XPATH, f'//*[@id="source_tab"]/div[2]/div[2]/div/div/div/div/div[1]/div/label')
    EMAIL_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[3]/div/label/img')
    EMAIL_FORM = (By.XPATH, f'//*[@id="mailchimp_list"]/div/div[2]')
    EMAIL_FORM_CHOOSE = (By.ID, f'react-select-13-option-0')
    EMAIL_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    EMAIL_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    EMAIL_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    EMAIL_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[3]/div[2]/div')

    # # custom notification
    # CUSTOM = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[11]/div/label')
    # CUSTOM_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[11]/div/label/img')
    # CUSTOM_1ST = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
    #                         f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]')
    # CUSTOM_1ST_CHOOSE = (By.ID, f'react-select-10-option-2')
    # CUSTOM_2ND = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
    #                         f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/div/div[2]')
    # CUSTOM_2ND_CHOOSE = (By.ID, f'react-select-11-option-1')
    # CUSTOM_3RD = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
    #                         f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[5]/div/div/div/div/div[2]')
    # CUSTOM_3RD_CHOOSE = (By.ID, f'react-select-12-option-1')
    # CUSTOM_4TH = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div['
    #                         f'2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div/div[6]/div/div/div/div/div[2]')
    # CUSTOM_4TH_CHOOSE = (By.ID, f'react-select-13-option-1')
    # CUSTOM_CUSTOM_TEMPLATE_TEXT = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div['
    #                                          f'2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div['
    #                                          f'2]/div/div/div[4]/div/input')
    # CUSTOM_ADVANCED_TEMPLATE = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[2]/div[2]/div')
    #
    # # id : 0
    # TITLE_1 = (By.ID, f'field-0-0-0')
    # F_NAME_1 = (By.ID, f'field-0-0-5')
    # L_NAME_1 = (By.ID, f'field-0-0-6')
    # CITY_1 = (By.ID, f'field-0-0-8')
    # COUNTRY_1 = (By.ID, f'field-0-0-9')
    # IMAGE_1 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[6]/div[2]/div/div/button')
    # MEDIA_LIBRARY = (By.ID, f'menu-item-browse')
    # IMAGE_1_CHOOSE = (By.XPATH, f'/html/body/div[8]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[1]/div/div')
    # SELECT_IMAGE = (By.XPATH, f'/html/body/div[4]/div[1]/div/div/div[4]/div/div[2]/button')
    # URL_1 = (By.ID, f'field-0-0-12')
    # TIME_1 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[8]/div[2]/div')
    # PREVIOUS_MONTH_1 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[8]/div['
    #                               f'2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]')
    # CHOOSE_DATE_1 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[8]/div['
    #                            f'2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div['
    #                            f'2]/div/table/tbody/tr[3]/td[2]')
    # TAB_1 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div/div/h4')
    # ADD_NEW_1 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/button')
    # # id : 1
    # TITLE_2 = (By.ID, f'field-2-1-0')
    # F_NAME_2 = (By.ID, f'field-2-1-5')
    # L_NAME_2 = (By.ID, f'field-2-1-6')
    # CITY_2 = (By.ID, f'field-2-1-8')
    # COUNTRY_2 = (By.ID, f'field-2-1-9')
    # IMAGE_2 = (
    #     By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div[6]/div[2]/div/div/button')
    # IMAGE_2_CHOOSE = (By.XPATH, f'/html/body/div[8]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[2]/div/div')
    # URL_2 = (By.ID, f'field-2-1-12')
    # TIME_2 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div[8]/div[2]/div')
    # TAB_2 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/h4')
    # ADD_NEW_2 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[2]/button')
    # # id : 2
    # TITLE_3 = (By.ID, f'field-4-2-0')
    # F_NAME_3 = (By.ID, f'field-4-2-5')
    # L_NAME_3 = (By.ID, f'field-4-2-6')
    # CITY_3 = (By.ID, f'field-4-2-8')
    # COUNTRY_3 = (By.ID, f'field-4-2-9')
    # IMAGE_3 = (
    #     By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div[6]/div[2]/div/div/button')
    # IMAGE_3_CHOOSE = (By.XPATH, f'/html/body/div[8]/div[1]/div/div/div[3]/div[2]/div/div[3]/ul/li[3]/div/div')
    # URL_3 = (By.ID, f'field-4-2-12')
    # TIME_3 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div[8]/div[2]/div')
    # TAB_3 = (By.XPATH, f'//*[@id="content_tab"]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/h4')

    NOTIFICATION_BAR = (By.XPATH, f'//*[@id="source_tab"]/div[1]/div[2]/div/div/div/div/div[7]/div/label')
    NOTIFICATION_BAR_TEMPLATE = (By.XPATH, f'//*[@id="design_tab"]/div/div[2]/div[1]/div/div/div/div[3]/div/label/img')
    BUILD_WITH_ELEMENTOR = (By.ID, f'build_with_elementor')
    ELEMENTOR_TEMPLATE = (By.XPATH,
                          f'//*[@id="wprf-modal-nx-bar_with_elementor"]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[4]/div/label/img')
    IMPORT_ELEMENTOR_TEMPLATE = (By.ID, f'import_elementor_theme')
    CONTENT = (By.XPATH,
               f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div/div')
    BUTTON_TEXT = (By.ID, f'button_text')
    BUTTON_URL = (By.ID, f'button_url')
    ENABLE_COUNTDOWN = (By.ID, f'enable_countdown')
    PERMANENT_CLOSE = (By.ID, f'close_forever')
    EVERGREEN_TIMER = (By.ID, f'evergreen_timer')
    COUNTDOWN_TEXT = (By.ID, f'countdown_text')
    EXPIRED_TEXT = (By.ID, f'countdown_expired_text')
    START_DATE = (By.XPATH, f'//*[@id="content_tab"]/div[2]/div[2]/div[5]/div[2]/div/button')
    GOTO_PREVIOUS_MONTH = (By.XPATH, f'//*[@id="content_tab"]/div[2]/div[2]/div[5]/div[2]/div/div/div/div/div/div['
                                     f'2]/div/div/div/div[2]/div[1]/div[1]')
    CHOOSE_START_DATE = (By.XPATH, f'//*[@id="content_tab"]/div[2]/div[2]/div[5]/div[2]/div/div/div/div/div/div['
                                   f'2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]')
    END_DATE = (By.XPATH, f'//*[@id="content_tab"]/div[2]/div[2]/div[6]/div[2]/div/button')
    GOTO_NEXT_MONTH = (By.XPATH, f'//*[@id="content_tab"]/div[2]/div[2]/div[6]/div[2]/div/div/div/div/div/div['
                                 f'2]/div/div/div/div[2]/div[1]/div[2]')
    CHOOSE_END_DATE = (By.XPATH, f'//*[@id="content_tab"]/div[2]/div[2]/div[6]/div[2]/div/div/div/div/div/div['
                                 f'2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]/div')
    START_DATE_EL = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[3]/div[2]/div/button')
    GOTO_PREVIOUS_MONTH_EL = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div['
                                        f'2]/div/div/div/div[2]/div[1]/div[1]')
    CHOOSE_START_DATE_EL = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div['
                                      f'2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]/div')
    END_DATE_EL = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[4]/div[2]/div/button')
    GOTO_NEXT_MONTH_EL = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[4]/div[2]/div/div/div/div/div/div['
                                    f'2]/div/div/div/div[2]/div[1]/div[2]')
    CHOOSE_END_DATE_EL = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[4]/div[2]/div/div/div/div/div/div['
                                    f'2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]/div')
    RANDOMIZE = (By.ID, f'time_randomize')
    RANDOMIZE_START_TIME = (By.NAME, f'start_time')
    RANDOMIZE_END_TIME = (By.NAME, f'end_time')
    TIME_ROTATION = (By.ID, f'time_rotation')
    TIME_RESET = (By.XPATH, f'time_reset')

    def __init__(self, browser):
        self.browser = browser
        self.cursor = ActionChains(browser)

    def load(self):
        # self.browser.get(conf.URL_NX)
        self.browser.find_element(By.XPATH, '//*[@id="toplevel_page_nx-admin"]/a/div[3]').click()

    def double_clicks(self, element):
        self.browser.find_element(*element).click()
        self.browser.find_element(*element).click()

    def common_task(self, src):
        if src != 'nxbarel':
            if src != 'contact' and src != 'email_subs' and src != 'custom' and src != 'nxbar':
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
        if src != 'nxbarel' and src != 'nxbar':
            self.browser.find_element(*self.SHOW_DEFAULT_IMAGE).click()
            self.browser.find_element(*self.SHOW_DEFAULT_IMAGE).click()
            if src != 'download-stat':
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
        # sticky bar
        if src == 'nxbarel' or src == 'nxbar':
            self.browser.find_element(*self.STICKY_BAR).click()
            self.browser.find_element(*self.OVERLAPPING).click()
        # notification size
        if src != 'nxbarel' and src != 'nxbar':
            self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.NOTIFICATION_SIZE).send_keys('400')
        # display close option
        self.double_clicks(self.CLOSE_BUTTON)
        self.double_clicks(self.HIDE_ON_MOBILE)
        # queue management
        if src != 'nxbarel' and src != 'nxbar':
            self.double_clicks(self.GLOBAL_QUEUE)
        # timing
        if src == 'nxbarel' or src == 'nxbar':
            # initial delay
            self.browser.find_element(*self.INITIAL_DELAY).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.INITIAL_DELAY).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.INITIAL_DELAY).send_keys('1')
            # auto hide
            self.browser.find_element(*self.AUTO_HIDE).click()
            self.browser.find_element(*self.HIDE_AFTER).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.HIDE_AFTER).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.HIDE_AFTER).send_keys('20')
        else:
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

        if src != 'nxbarel' and src != 'nxbar':
            # sound
            self.browser.find_element(*self.SOUND).click()
            self.browser.find_element(*self.SOUND_CHOOSE).click()
        # behavior
        if src != 'nxbarel' and src != 'nxbar':
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
        if src != 'contact' and src != 'email_subs' and src != 'nxbarel':
            # open link in a new tab
            self.browser.find_element(*self.LINK_OPEN).click()

        # publishing notification
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.PUBLISH).click()

        assert self.browser.find_element(*self.SUCCESS_NOTICE).text == 'Successfully Created.'

    def create_sale_notice(self, src):
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
        self.browser.find_element(*self.CONTENT_1ST).click()
        self.browser.find_element(*self.SALE_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Kine nilo')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND).click()
        self.browser.find_element(*self.SALE_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD).click()
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

    def create_comment_notice(self):
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
        self.browser.find_element(*self.CONTENT_1ST).click()
        self.browser.find_element(*self.COMMENT_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Motamot dilo')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND).click()
        self.browser.find_element(*self.COMMENT_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD).click()
        self.browser.find_element(*self.COMMENT_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.COMMENT_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.COMMENT_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # content length
        self.browser.find_element(*self.COMMENT_CONTENT_LENGTH).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.COMMENT_CONTENT_LENGTH).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.COMMENT_CONTENT_LENGTH).send_keys('15')

        # common tasks
        self.common_task('comment')

    def create_review_notice(self, src):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Review (WP) Notification') if src == 'wp' else \
            self.browser.find_element(*self.NX_TITLE).send_keys('NX Review (WOO) Notification')

        # source page
        self.browser.find_element(*self.REVIEW).click()
        # choose source
        self.browser.find_element(*self.REVIEW_ORG).click() if src == 'wp' else \
            self.browser.find_element(*self.REVIEW_WOO).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.REVIEW_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        if src == 'wp':
            # choose product type
            self.browser.find_element(*self.REVIEW_WP_PRODUCT_TYPE).click()
            self.browser.find_element(*self.REVIEW_WP_PRODUCT_TYPE_CHOOSE).click()
            # slug
            self.browser.find_element(*self.REVIEW_WP_SLUG).send_keys('essential-addons-for-elementor-lite')
            # 1st
            self.browser.find_element(*self.CONTENT_1ST_REVIEW_DSTAT).click()
            self.browser.find_element(*self.REVIEW_WP_1ST_CHOOSE).click()
            # nt template
            self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Rate koreche')
            # 2nd
            self.browser.find_element(*self.CONTENT_2ND_REVIEW_DSTAT).click()
            self.browser.find_element(*self.REVIEW_WP_2ND_CHOOSE).click()
            # 3rd
            self.browser.find_element(*self.CONTENT_3RD_REVIEW_DSTAT).click()
            self.browser.find_element(*self.REVIEW_WP_3RD_CHOOSE).click()
            # advanced template
            self.browser.find_element(*self.REVIEW_WP_ADVANCED_TEMPLATE).click()
            self.browser.find_element(*self.REVIEW_WP_ADVANCED_TEMPLATE).click()
        else:
            # 1st
            self.browser.find_element(*self.CONTENT_1ST).click()
            self.browser.find_element(*self.REVIEW_WOO_1ST_CHOOSE).click()
            # nt template
            self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Rate koreche')
            # 2nd
            self.browser.find_element(*self.CONTENT_2ND).click()
            self.browser.find_element(*self.REVIEW_WOO_2ND_CHOOSE).click()
            # 3rd
            self.browser.find_element(*self.CONTENT_3RD).click()
            self.browser.find_element(*self.REVIEW_WOO_3RD_CHOOSE).click()
            # advanced template
            self.browser.find_element(*self.REVIEW_WOO_ADVANCED_TEMPLATE).click()
            self.browser.find_element(*self.REVIEW_WOO_ADVANCED_TEMPLATE).click()

        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()

        # common tasks
        self.common_task('review')

    def create_download_stat_notice(self):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Download Stat Notification')

        # source page
        self.browser.find_element(*self.DOWNLOAD_STAT).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.DOWNLOAD_STAT_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # choose product type
        self.browser.find_element(*self.DOWNLOAD_STAT_PRODUCT_TYPE).click()
        self.browser.find_element(*self.DOWNLOAD_STAT_PRODUCT_PLUGIN_CHOOSE).click()
        # slug
        self.browser.find_element(*self.DOWNLOAD_STAT_SLUG).send_keys('essential-addons-for-elementor-lite')
        # 1st
        self.browser.find_element(*self.CONTENT_1ST_REVIEW_DSTAT).click()
        self.browser.find_element(*self.DOWNLOAD_STAT_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Download kora hoise')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND_REVIEW_DSTAT).click()
        self.browser.find_element(*self.DOWNLOAD_STAT_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD_REVIEW_DSTAT).click()
        self.browser.find_element(*self.DOWNLOAD_STAT_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.DOWNLOAD_STAT_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.DOWNLOAD_STAT_ADVANCED_TEMPLATE).click()

        # common tasks
        self.common_task('download-stat')

    def create_e_learning_notice(self):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX eLearning Notification')

        # source page
        self.browser.find_element(*self.eLEARNING).click()
        self.browser.find_element(*self.eLEARNING_TUTOR).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.eLEARNING_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.CONTENT_1ST).click()
        self.browser.find_element(*self.eLEARNING_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Enroll kore fello')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND).click()
        self.browser.find_element(*self.eLEARNING_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD).click()
        self.browser.find_element(*self.eLEARNING_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.eLEARNING_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.eLEARNING_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # show notification of
        self.browser.find_element(*self.eLEARNING_SHOW_NOTIFICATION_OF).click()
        self.browser.find_element(*self.eLEARNING_SHOW_NOTIFICATION_OF_CHOOSE).click()
        # select course
        self.browser.find_element(*self.eLEARNING_SELECT_COURSE).click()
        self.browser.find_element(*self.eLEARNING_SELECT_COURSE_CHOOSE).click()

        # common tasks
        self.common_task('e-learning')

    def create_donation_notice(self):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Donation Notification')

        # source page
        self.browser.find_element(*self.DONATION).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.DONATION_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.CONTENT_1ST).click()
        self.browser.find_element(*self.DONATION_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Dan korlo')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND).click()
        self.browser.find_element(*self.DONATION_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD).click()
        self.browser.find_element(*self.DONATION_3RD_CHOOSE).click()
        # 4th
        self.browser.find_element(*self.CONTENT_4TH).click()
        self.browser.find_element(*self.DONATION_4TH_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.DONATION_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.DONATION_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()
        # show notification of
        self.browser.find_element(*self.DONATION_SHOW_NOTIFICATION_OF).click()
        self.browser.find_element(*self.DONATION_SHOW_NOTIFICATION_OF_CHOOSE).click()
        # select course
        self.browser.find_element(*self.DONATION_SELECT_FORM).click()
        self.browser.find_element(*self.DONATION_SELECT_FORM_CHOOSE).click()

        # common tasks
        self.common_task('donation')

    def create_contact_notice(self, src):
        self.browser.find_element(*self.ADD_NEW).click()
        if src == 'cf7':
            self.browser.find_element(*self.NX_TITLE).send_keys('NX Contact (Contact Form 7) Notification')
        elif src == 'wpf':
            self.browser.find_element(*self.NX_TITLE).send_keys('NX Contact (WPForm) Notification')
        elif src == 'ninja':
            self.browser.find_element(*self.NX_TITLE).send_keys('NX Contact (Ninja Form) Notification')
        else:
            self.browser.find_element(*self.NX_TITLE).send_keys('NX Contact (Gravity Form) Notification')

        # source page
        self.browser.find_element(*self.CONTACT).click()
        if src == 'cf7':
            self.browser.find_element(*self.CONTACT_CF7).click()
        elif src == 'wpf':
            self.browser.find_element(*self.CONTACT_WPF).click()
        elif src == 'ninja':
            self.browser.find_element(*self.CONTACT_NIN).click()
        else:
            self.browser.find_element(*self.CONTACT_GRA).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.CONTACT_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # select a form
        self.browser.find_element(*self.CONTACT_FORM).click()
        self.browser.find_element(*self.CONTACT_FORM_CHOOSE).click()
        # 1st
        self.browser.find_element(*self.CONTENT_1ST_CONTACT_EMAIL).click()
        self.browser.find_element(*self.CONTACT_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Jogajog korlo')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND_CONTACT_EMAIL).click()
        self.browser.find_element(*self.CONTACT_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD_CONTACT_EMAIL).click()
        self.browser.find_element(*self.CONTACT_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.CONTACT_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.CONTACT_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()

        # common tasks
        self.common_task('contact')

    def create_email_subs_notice(self):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Email Subscription Notification')

        # source page
        self.browser.find_element(*self.EMAIL).click()
        self.browser.find_element(*self.EMAIL_MAILCHIMP).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.EMAIL_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # select a form
        self.browser.find_element(*self.EMAIL_FORM).click()
        self.browser.find_element(*self.CONTACT_FORM_CHOOSE).click()
        # 1st
        self.browser.find_element(*self.CONTENT_1ST_CONTACT_EMAIL).click()
        self.browser.find_element(*self.EMAIL_1ST_CHOOSE).click()
        # nt template
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('Subscription korse')
        # 2nd
        self.browser.find_element(*self.CONTENT_2ND_CONTACT_EMAIL).click()
        self.browser.find_element(*self.EMAIL_2ND_CHOOSE).click()
        # 3rd
        self.browser.find_element(*self.CONTENT_3RD_CONTACT_EMAIL).click()
        self.browser.find_element(*self.EMAIL_3RD_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.EMAIL_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.EMAIL_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()

        # common tasks
        self.common_task('email_subs')

    def create_custom_notice(self):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys('NX Custom Notification')

        # source page
        self.browser.find_element(*self.CUSTOM).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.browser.find_element(*self.CUSTOM_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        # 1st
        self.browser.find_element(*self.CUSTOM_1ST).click()
        self.browser.find_element(*self.CUSTOM_1ST_CHOOSE).click()
        # nt template 1
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.NT_TEMPLATE_TEXT).send_keys('from')
        # 2nd
        self.browser.find_element(*self.CUSTOM_2ND).click()
        self.browser.find_element(*self.CUSTOM_2ND_CHOOSE).click()
        # nt template 2
        self.browser.find_element(*self.CUSTOM_CUSTOM_TEMPLATE_TEXT).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.CUSTOM_CUSTOM_TEMPLATE_TEXT).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.CUSTOM_CUSTOM_TEMPLATE_TEXT).send_keys('kine nilo')
        # 3rd
        self.browser.find_element(*self.CUSTOM_3RD).click()
        self.browser.find_element(*self.CUSTOM_3RD_CHOOSE).click()
        # 4th
        self.browser.find_element(*self.CUSTOM_4TH).click()
        self.browser.find_element(*self.CUSTOM_4TH_CHOOSE).click()
        # advanced template
        self.browser.find_element(*self.CUSTOM_ADVANCED_TEMPLATE).click()
        self.browser.find_element(*self.CUSTOM_ADVANCED_TEMPLATE).click()
        # random order
        self.browser.find_element(*self.RANDOM_ORDER).click()
        self.browser.find_element(*self.RANDOM_ORDER).click()

        # input content 1
        self.browser.find_element(*self.TITLE_1).send_keys('Momo chocolate')
        self.browser.find_element(*self.F_NAME_1).send_keys('One')
        self.browser.find_element(*self.L_NAME_1).send_keys('Two')
        self.browser.find_element(*self.CITY_1).send_keys('Uttara')
        self.browser.find_element(*self.COUNTRY_1).send_keys('Bangladesh')
        self.browser.find_element(*self.IMAGE_1).click()
        self.browser.find_element(*self.IMAGE_1_CHOOSE).click()
        self.browser.find_element(*self.SELECT_IMAGE).click()
        self.browser.find_element(*self.URL_1).send_keys('https://translate.google.com/')
        self.browser.find_element(*self.TIME_1).click()
        self.browser.find_element(*self.PREVIOUS_MONTH_1).click()
        self.browser.find_element(*self.CHOOSE_DATE_1).click()
        self.browser.find_element(*self.TAB_1).click()
        # input content 1
        self.browser.find_element(*self.ADD_NEW_1).click()
        self.browser.find_element(*self.TITLE_2).send_keys('Momo chocolate')
        self.browser.find_element(*self.F_NAME_2).send_keys('One')
        self.browser.find_element(*self.L_NAME_2).send_keys('Two')
        self.browser.find_element(*self.CITY_2).send_keys('Uttara')
        self.browser.find_element(*self.COUNTRY_2).send_keys('Bangladesh')
        self.browser.find_element(*self.IMAGE_2).click()
        self.browser.find_element(*self.IMAGE_2_CHOOSE).click()
        self.browser.find_element(*self.SELECT_IMAGE).click()
        self.browser.find_element(*self.URL_2).send_keys('https://translate.google.com/')
        self.browser.find_element(*self.TIME_2).click()
        self.browser.find_element(*self.PREVIOUS_MONTH_2).click()
        self.browser.find_element(*self.CHOOSE_DATE_2).click()
        self.browser.find_element(*self.TAB_1).click()

        # common tasks
        self.common_task('custom')

    def create_notificationbar(self, src):
        self.browser.find_element(*self.ADD_NEW).click()
        self.browser.find_element(*self.NX_TITLE).send_keys(
            'Notification Bar') if src == 'nxbar' else self.browser.find_element(*self.NX_TITLE).send_keys(
            'Notification Bar (Elementor)')

        # source page
        self.browser.find_element(*self.NOTIFICATION_BAR).click()
        # next page design
        self.browser.find_element(*self.NEXT_0).click()

        # design page
        self.browser.execute_script("window.scrollTo(0, 0)")
        if src == 'nxbar':
            self.browser.find_element(*self.NOTIFICATION_BAR_TEMPLATE).click()
        else:
            self.browser.find_element(*self.BUILD_WITH_ELEMENTOR).click()
            self.browser.find_element(*self.ELEMENTOR_TEMPLATE).click()
            self.browser.find_element(*self.IMPORT_ELEMENTOR_TEMPLATE).click()
        # next page content
        self.browser.find_element(*self.NEXT_1).click()

        # content page
        self.browser.execute_script("window.scrollTo(0, 0)")
        if src == 'nxbar':
            self.browser.find_element(*self.CONTENT).click()
            self.browser.find_element(*self.CONTENT).send_keys('NotificationX Automation camp is Running...')
            # button text
            self.browser.find_element(*self.BUTTON_TEXT).send_keys('Grab')
            # button url
            self.browser.find_element(*self.BUTTON_URL).send_keys('https://translate.google.com/')

        # enable countdown
        self.browser.find_element(*self.ENABLE_COUNTDOWN).click()
        if src == 'nxbar':
            self.browser.find_element(*self.COUNTDOWN_TEXT).send_keys('Grab it before')
            self.browser.find_element(*self.EXPIRED_TEXT).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.EXPIRED_TEXT).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.EXPIRED_TEXT).send_keys('You missed it buddy, Try next time.')
            self.browser.find_element(*self.START_DATE).click()
            self.browser.find_element(*self.GOTO_PREVIOUS_MONTH).click()
            self.browser.find_element(*self.CHOOSE_START_DATE).click()
            self.browser.find_element(*self.START_DATE).click()
            self.browser.find_element(*self.END_DATE).click()
            self.browser.find_element(*self.GOTO_NEXT_MONTH).click()
            self.browser.find_element(*self.CHOOSE_END_DATE).click()
            self.browser.find_element(*self.END_DATE).click()
        else:
            self.browser.find_element(*self.START_DATE_EL).click()
            self.browser.find_element(*self.GOTO_PREVIOUS_MONTH_EL).click()
            self.browser.find_element(*self.CHOOSE_START_DATE_EL).click()
            self.browser.find_element(*self.START_DATE_EL).click()
            self.browser.find_element(*self.END_DATE_EL).click()
            self.browser.find_element(*self.GOTO_NEXT_MONTH_EL).click()
            self.browser.find_element(*self.CHOOSE_END_DATE_EL).click()
            self.browser.find_element(*self.END_DATE_EL).click()

        self.browser.find_element(*self.PERMANENT_CLOSE).click()

        # common tasks
        self.common_task(src)
