import time
import platform
from assertpy import assert_that, soft_assertions
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.basepage import BasePage


class Helper(BasePage):
    add_new = (By.XPATH, f"//a[@class='nx-add-new-btn']")
    nx_title = (By.ID, f'nx-title')
    next_btn_for_wait = f"//button[normalize-space()='Next']"
    remove_elementor_design = f"//button[@id='nx-bar_with_elementor-remove']"
    next_btn = (By.XPATH, f"//button[normalize-space()='Next']")
    prev_btn = (By.XPATH, f"//button[normalize-space()='Previous']")
    publish_btn = (By.XPATH, f"//button[normalize-space()='Publish']")
    random_order = (By.ID, f'random_order')
    # LINK OPTIONS
    link_type = (By.XPATH, f"//div[@id='link_type']")
    link_type_choose = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[3]")
    # UTM CONTROL
    utm_campaign = (By.ID, f'utm_campaign')
    utm_medium = (By.ID, f'utm_medium')
    utm_source = (By.ID, f'utm_source')
    # IMAGE
    show_default_image = (By.ID, f'show_default_image')
    default_image = (By.XPATH, f"//label[@for='wprf-input-radio-3-4']")
    image = (By.XPATH, f"//div[@id='show_notification_image']")
    feature_image_choose = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    comment_gravatar_image = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    gravatar_image = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[3]")
    map_image = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[4]")
    # VISIBILITY
    show_on = (By.XPATH, f"//div[@id='show_on']")
    show_on_choose_everywhere = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[1]")
    show_on_display = (By.XPATH, f"//div[@id='show_on_display']")
    show_on_display_choose_everyone = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[1]")
    # VISIBILITY - INLINE
    locations = (By.XPATH, f"//div[@id='inline_location']")
    locations_archive_page = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[1]")
    locations_archive_page_1 = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[1]")
    locations_archive_page_2 = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    locations_shop_cart = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[3]")
    # APPEARANCE
    position = (By.XPATH, f"//div[@id='position']")
    position_choose_left = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[1]")
    position_choose_right = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    sticky_bar = (By.ID, f'sticky_bar')
    overlapping = (By.ID, f'pressbar_body')
    notification_size = (By.ID, f'size')
    close_button = (By.ID, f'close_button')
    hide_on_mobile = (By.ID, f'hide_on_mobile')
    # QUEUE MANAGEMENT
    global_queue = (By.ID, f'global_queue')
    # TIMING
    delay_before_first_notification = (By.ID, f'delay_before')
    display_for = (By.ID, f'display_for')
    delay_between = (By.ID, f'delay_between')
    initial_delay = (By.ID, f'initial_delay')
    auto_hide = (By.ID, f'auto_hide')
    hide_after = (By.ID, f'hide_after')
    # SOUND SETTINGS
    sound = (By.XPATH, f"//div[@id='sound']")
    sound_choose = (By.XPATH, f"//div[@class='wprf-select__menu css-26l3qy-menu']//div//div[2]")
    volume_reset_btn = (By.XPATH, f"//button[normalize-space()='Reset']")
    volume = (By.XPATH, f"//input[@id='inspector-input-control-1']")
    volume_1 = (By.XPATH, f"//input[@id='inspector-input-control-4']")
    volume_src_custom = (By.XPATH, f"//input[@id='inspector-input-control-9']")

    # BEHAVIOUR
    display_last = (By.ID, f'display_last')
    display_form = (By.ID, f'display_from')
    loop = (By.ID, f'loop')
    link_open = (By.ID, f'link_open')

    # Advanced Design
    ad_toggle_on = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-label-position-right']"
                              f"//label[@for='advance_edit']")
    ad_toggle_off = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                               f"//label[@for='advance_edit']")
    # background color
    ad_bg_color = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                             f"wprf-name-bg_color']//span[@class='wprf-picker-display']")
    ad_color_hx = (By.XPATH, f"//button[@aria-label='Show detailed inputs']//*[name()='svg']")
    ad_color_reset = (By.XPATH, f"//button[@class='wprf-colorpicker-reset']")
    # text color
    ad_txt_color = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                              f"wprf-name-text_color']//span[@class='wprf-picker-display']")
    # border
    ad_border = (By.XPATH, f"//input[@id='border']")
    ad_border_size = (By.XPATH, f"//input[@id='border_size']")
    ad_border_style = (By.XPATH, f"//div[@id='border_style']")
    ad_border_style_choose = (By.ID, f'react-select-22-option-1')
    ad_border_comment_style_choose = (By.ID, f'react-select-19-option-1')
    ad_border_org_review_style_choose = (By.ID, f'react-select-20-option-1')
    ad_border_woo_review_style_choose = (By.ID, f'react-select-22-option-1')
    ad_border_donation_style_choose = (By.ID, f'react-select-21-option-1')
    ad_border_color = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                                 f"wprf-name-border_color']//span[@class='wprf-picker-display']")
    ad_border_color_hx = (By.XPATH, f"//button[@aria-label='Show detailed inputs']//*[name()='svg']")
    # notification bar
    ad_bg_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                             f"wprf-name-bar_bg_color']//span[@class='wprf-picker-display']")
    ad_txt_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                              f"wprf-name-bar_text_color']//span[@class='wprf-picker-display']")
    ad_btn_bg_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                                     f"wprf-name-bar_btn_bg']//span[@class='wprf-picker-display']")
    ad_btn_txt_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                                      f"wprf-name-bar_btn_text_color']//span[@class='wprf-picker-display']")
    ad_countdown_bg_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label"
                                           f" wprf-name-bar_counter_bg']//span[@class='wprf-picker-display']")
    ad_countdown_txt_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker "
                                            f"wprf-inline-label wprf-name-bar_counter_text_color']"
                                            f"//span[@class='wprf-picker-display']")
    ad_close_btn_color_bar = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-colorpicker wprf-inline-label "
                                        f"wprf-name-bar_close_color']//span[@class='wprf-picker-display']")
    ad_btn_position_bar = (By.XPATH, f"//div[@id='bar_close_position']")
    ad_btn_position_choose_bar = (By.ID, f'react-select-16-option-1')
    ad_font_size_bar = (By.XPATH, f"//input[@id='bar_font_size']")
    # font size
    ad_font_1st_size = (By.XPATH, f"//input[@id='first_font_size']")
    ad_font_2nd_size = (By.XPATH, f"//input[@id='second_font_size']")
    ad_font_3rd_size = (By.XPATH, f"//input[@id='third_font_size']")
    # image
    ad_image = (By.XPATH, f"//div[@id='image_shape']")
    ad_image_choose = (By.ID, f'react-select-20-option-3')
    ad_image_comment_choose = (By.ID, f'react-select-17-option-3')
    ad_image_review_choose = (By.ID, f'react-select-18-option-3')
    ad_image_donation_choose = (By.ID, f'react-select-19-option-3')
    ad_image_radius = (By.XPATH, f"//input[@id='custom_image_shape']")
    ad_image_position = (By.XPATH, f"//div[@id='image_position']")
    ad_image_position_choose = (By.ID, f'react-select-21-option-0')
    ad_image_comment_position_choose = (By.ID, f'react-select-18-option-0')
    ad_image_review_position_choose = (By.ID, f'react-select-19-option-0')
    ad_image_donation_position_choose = (By.ID, f'react-select-20-option-0')
    # Message
    success_notice = f'//*[@id="notificationx"]/div/div[1]/div[2]/p'

    def __init__(self, browser):
        self.browser = browser

    def double_clicks(self, element):
        self.browser.find_element(*element).click()
        self.browser.find_element(*element).click()

    def check_advanced_design(self, source):
        self.browser.find_element(*self.ad_toggle_on).click()
        self.browser.find_element(*self.ad_toggle_off).click()
        self.browser.find_element(*self.ad_toggle_on).click()
        # DESIGN
        if source.__eq__("nxbar"):
            # background color
            self.browser.find_element(*self.ad_bg_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # text color
            self.browser.find_element(*self.ad_txt_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # button background color
            self.browser.find_element(*self.ad_btn_bg_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # button text color
            self.browser.find_element(*self.ad_btn_txt_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # countdown background color
            self.browser.find_element(*self.ad_countdown_bg_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # countdown text color
            self.browser.find_element(*self.ad_countdown_txt_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # close button color
            self.browser.find_element(*self.ad_close_btn_color_bar).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # close button position
            self.browser.find_element(*self.ad_btn_position_bar).click()
            self.browser.find_element(*self.ad_btn_position_choose_bar).click()
            # TYPOGRAPHY
            # font size
            self.do_field_input_select_all(self.ad_font_size_bar)
            self.browser.find_element(*self.ad_font_size_bar).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.ad_font_size_bar).send_keys('14')
        else:
            # background color
            self.browser.find_element(*self.ad_bg_color).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # text color
            self.browser.find_element(*self.ad_txt_color).click()
            self.browser.find_element(*self.ad_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            # border
            self.browser.find_element(*self.ad_border).click()
            self.do_field_input_select_all(self.ad_border_size)
            self.browser.find_element(*self.ad_border_size).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.ad_border_size).send_keys('2')
            self.browser.find_element(*self.ad_border_style).click()
            if source == "comment" or source == "custom":
                self.browser.find_element(*self.ad_border_comment_style_choose).click()
            elif source == "org-review" or source == "d_stats" or source == 'tutor' or source == 'contact' or \
                    source == 'email' or source == 'analytics':
                self.browser.find_element(*self.ad_border_org_review_style_choose).click()
            elif source.__eq__("woo-review"):
                self.browser.find_element(*self.ad_border_woo_review_style_choose).click()
            elif source.__eq__('donation'):
                self.browser.find_element(*self.ad_border_donation_style_choose).click()
            else:
                self.browser.find_element(*self.ad_border_style_choose).click()
            self.browser.find_element(*self.ad_border_color).click()
            self.browser.find_element(*self.ad_border_color_hx).click()
            self.browser.find_element(*self.ad_color_reset).click()
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            # TYPOGRAPHY
            # 1st
            self.do_field_input_select_all(self.ad_font_1st_size)
            self.browser.find_element(*self.ad_font_1st_size).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.ad_font_1st_size).send_keys('14')
            # 2nd
            self.do_field_input_select_all(self.ad_font_2nd_size)
            self.browser.find_element(*self.ad_font_2nd_size).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.ad_font_2nd_size).send_keys('15')
            # 3rd
            self.do_field_input_select_all(self.ad_font_3rd_size)
            self.browser.find_element(*self.ad_font_3rd_size).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.ad_font_3rd_size).send_keys('12')
            # IMAGE APPEARANCE
            self.browser.find_element(*self.ad_image).click()
            if source == "comment" or source == "custom":
                self.browser.find_element(*self.ad_image_comment_choose).click()
            elif source == "org-review" or source == "d_stats" or source == 'tutor' or source == 'contact' or \
                    source == 'email' or source == 'analytics':
                self.browser.find_element(*self.ad_image_review_choose).click()
            elif source.__eq__('donation'):
                self.browser.find_element(*self.ad_image_donation_choose).click()
            elif source == "sale" or source == "woo-review":
                self.browser.find_element(*self.ad_image_choose).click()

            self.do_field_input_select_all(self.ad_image_radius)
            self.browser.find_element(*self.ad_image_radius).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.ad_image_radius).send_keys('50')
            self.browser.find_element(*self.ad_image_position).click()
            if source == "comment" or source == "custom":
                self.browser.find_element(*self.ad_image_comment_position_choose).click()
            elif source == "org-review" or source == "d_stats" or source == 'tutor' or source == 'contact' or \
                    source == 'email' or source == 'analytics':
                self.browser.find_element(*self.ad_image_review_position_choose).click()
            elif source == "sale" or source == "woo-review":
                self.browser.find_element(*self.ad_image_position_choose).click()
            elif source.__eq__('donation'):
                self.browser.find_element(*self.ad_image_donation_position_choose).click()

    def check_visibility(self, element, error_message):
        if self.browser.find_element(By.XPATH, element).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that('Success').is_equal_to(error_message)

    def do_others(self, src, advanced_design, queue_management, position):
        with soft_assertions():
            if src.__eq__("inline-woo"):
                self.browser.find_element(*self.locations).click()
                self.browser.find_element(*self.locations_archive_page_1).click()
                self.browser.find_element(*self.locations).click()
                self.browser.find_element(*self.locations_archive_page_1).click()
                self.browser.find_element(*self.locations).click()
                self.browser.find_element(*self.locations_archive_page_1).click()
            elif src.__eq__("inline-edd"):
                self.browser.find_element(*self.locations).click()
                self.browser.find_element(*self.locations_archive_page).click()
            elif src.__eq__("inline-tutor") or src.__eq__("inline-ld"):
                self.browser.find_element(*self.locations).click()
                self.browser.find_element(*self.locations_archive_page).click()
            else:
                if src != 'nxbarel' and src != 'analytics':
                    if src != 'contact' and src != 'email_subs' and src != 'custom' and src != 'nxbar':
                        # LINK OPTIONS
                        self.browser.find_element(*self.link_type).click()
                        self.browser.find_element(*self.link_type_choose).click()

                    # UTM CONTROL
                    self.browser.find_element(*self.utm_campaign).send_keys('campaign_automation')
                    self.browser.find_element(*self.utm_medium).send_keys('medium_automation')
                    self.browser.find_element(*self.utm_source).send_keys('source_automation')

                # next page display
                self.browser.find_element(*self.next_btn).click()

                # IMAGE
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(1)
                if src != 'nxbarel' and src != 'nxbar':
                    self.browser.find_element(*self.show_default_image).click()
                    self.browser.find_element(*self.show_default_image).click()
                    if src != 'd_stat' and src != 'analytics':
                        self.browser.find_element(*self.image).click()
                        if src == 'comment':
                            self.browser.find_element(*self.comment_gravatar_image).click()
                        elif src == 'contact':
                            self.browser.find_element(*self.gravatar_image).click()
                        else:
                            self.browser.find_element(*self.feature_image_choose).click()
                # VISIBILITY
                # show on
                self.browser.find_element(*self.show_on).click()
                self.browser.find_element(*self.show_on_choose_everywhere).click()
                # display for
                self.browser.find_element(*self.show_on_display).click()
                self.browser.find_element(*self.show_on_display_choose_everyone).click()
                # next page customize
                self.browser.find_element(*self.next_btn).click()

                # customize page
                self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(1)
                # APPEARANCE
                self.browser.find_element(*self.position).click()
                if position == "L" or position == "T":
                    self.browser.find_element(*self.position_choose_left).click()
                else:
                    self.browser.find_element(*self.position_choose_right).click()
                # sticky bar
                if src == 'nxbarel' or src == 'nxbar':
                    self.browser.find_element(*self.sticky_bar).click()
                    self.browser.find_element(*self.overlapping).click()
                # notification size
                if src != 'nxbarel' and src != 'nxbar':
                    self.browser.find_element(*self.notification_size).click()
                    self.do_field_input_select_all(self.notification_size)
                    self.browser.find_element(*self.notification_size).send_keys(Keys.BACKSPACE)
                    self.browser.find_element(*self.notification_size).send_keys('400')
                # display close option
                self.double_clicks(self.close_button)
                self.double_clicks(self.hide_on_mobile)
                # QUEUE MANAGEMENT
                if src != 'nxbarel' and src != 'nxbar':
                    if queue_management.__eq__("y"):
                        self.browser.find_element(*self.global_queue).click()
                    else:
                        self.double_clicks(self.global_queue)

                # TIMING
                if src == 'nxbarel' or src == 'nxbar':
                    # initial delay
                    self.do_field_input_select_all(self.initial_delay)
                    self.browser.find_element(*self.initial_delay).send_keys(Keys.BACKSPACE)
                    self.browser.find_element(*self.initial_delay).send_keys('1')
                    # auto hide
                    self.browser.find_element(*self.auto_hide).click()
                    self.do_field_input_select_all(self.hide_after)
                    self.browser.find_element(*self.hide_after).send_keys(Keys.BACKSPACE)
                    self.browser.find_element(*self.hide_after).send_keys('20')
                else:
                    if queue_management != 'y':
                        # delay before
                        self.do_field_input_select_all(self.delay_before_first_notification)
                        self.browser.find_element(*self.delay_before_first_notification).send_keys(Keys.BACKSPACE)
                        self.browser.find_element(*self.delay_before_first_notification).send_keys('1')
                        # display for
                        self.do_field_input_select_all(self.display_for)
                        self.browser.find_element(*self.display_for).send_keys(Keys.BACKSPACE)
                        self.browser.find_element(*self.display_for).send_keys('5')
                        # delay between
                        self.do_field_input_select_all(self.delay_between)
                        self.browser.find_element(*self.delay_between).send_keys(Keys.BACKSPACE)
                        self.browser.find_element(*self.delay_between).send_keys('2')

                if src != 'nxbarel' and src != 'nxbar':
                    # SOUND SETTINGS
                    self.browser.find_element(*self.sound).click()
                    self.browser.find_element(*self.sound_choose).click()
                    self.browser.find_element(*self.volume_reset_btn).click()
                    if advanced_design.__eq__('y'):
                        self.do_field_input_select_all(self.volume_1)
                        self.browser.find_element(*self.volume_1).send_keys(Keys.BACKSPACE)
                        self.browser.find_element(*self.volume_1).send_keys('30')
                    else:
                        if not src.__eq__('custom'):
                            self.do_field_input_select_all(self.volume)
                            self.browser.find_element(*self.volume).send_keys(Keys.BACKSPACE)
                            self.browser.find_element(*self.volume).send_keys('30')
                        else:
                            self.do_field_input_select_all(self.volume_src_custom)
                            self.browser.find_element(*self.volume_src_custom).send_keys(Keys.BACKSPACE)
                            self.browser.find_element(*self.volume_src_custom).send_keys('30')
                # BEHAVIOUR
                if src != 'nxbarel' and src != 'nxbar':
                    if src != 'analytics':
                        # display last
                        self.do_field_input_select_all(self.display_last)
                        self.browser.find_element(*self.display_last).send_keys(Keys.BACKSPACE)
                        self.browser.find_element(*self.display_last).send_keys('5')
                        # display form the last
                        self.do_field_input_select_all(self.display_form)
                        self.browser.find_element(*self.display_form).send_keys(Keys.BACKSPACE)
                        self.browser.find_element(*self.display_form).send_keys('20')
                    # loop
                    if queue_management != 'y':
                        self.double_clicks(self.loop)
                if src != 'contact' and src != 'email_subs' and src != 'nxbarel' and src != 'analytics':
                    # open link in a new tab
                    self.browser.find_element(*self.link_open).click()

            # publishing notification
            self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(1.5)
            self.browser.find_element(*self.publish_btn).click()

            element = WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located((By.XPATH, self.success_notice)))

            assert_that(element.text).is_equal_to("Successfully Created.")
