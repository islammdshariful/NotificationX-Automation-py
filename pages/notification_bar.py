from utils.create_notice_helper import *
import utils.config as conf
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotificationBar(Helper):
    nx_bar = (By.XPATH, f"//label[@for='wprf-input-radio-0-6']")
    nxbar_template = (By.XPATH, f"//label[@for='wprf-input-radio-2-2']")
    build_w_ele = (By.XPATH, f"//button[@id='build_with_elementor']")
    nx_bar_ele_template = (By.XPATH, f"//label[@for='wprf-input-radio-3-1']")
    import_btn = (By.XPATH, f"//button[@id='import_elementor_theme']")

    content = (By.XPATH, f"//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    button_text = (By.ID, f'button_text')
    button_url = (By.ID, f'button_url')
    enable_countdown = (By.ID, f'enable_countdown')
    permanent_close = (By.ID, f'close_forever')
    evergreen_timer = (By.ID, f'evergreen_timer')
    countdown_text = (By.ID, f'countdown_text')
    expired_text = (By.ID, f'countdown_expired_text')
    start_date = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-date "
                            f"wprf-inline-label wprf-name-countdown_start_date']"
                            f"//div[@class='components-dropdown wprf-control-datetime']")
    goto_previous_month = (By.XPATH, f"//div[@aria-label='Move backward to switch to the previous month.']")
    choose_start_date = (By.XPATH, f'//*[@id="countdown_timer"]/div[2]/div[5]/div[2]/div/div/div/div/div/div[2]/div'
                                   f'/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]')
    end_date = (By.XPATH, f"//div[@class='wprf-control-wrapper wprf-type-date "
                          f"wprf-inline-label wprf-name-countdown_end_date']"
                          f"//div[@class='components-dropdown wprf-control-datetime']")
    goto_next_month = (By.XPATH, f"//div[@aria-label='Move forward to switch to the next month.']")
    choose_end_date = (By.XPATH, f'//*[@id="countdown_timer"]/div[2]/div[6]/div[2]/div/div/div/div/div/div[2]/div/div'
                                 f'/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]')
    # Elementor
    choose_start_date_el = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[3]/div[2]/div/div/div/div/div/div['
                                      f'2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]/div')
    choose_end_date_el = (By.XPATH, f'//*[@id="content_tab"]/div/div[2]/div[4]/div[2]/div/div/div/div/div/div['
                                    f'2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]/div')

    randomize = (By.ID, f'time_randomize')
    randomize_start_time = (By.NAME, f'start_time')
    randomize_end_time = (By.NAME, f'end_time')
    time_rotation = (By.ID, f'time_rotation')
    time_reset = (By.ID, f'time_reset')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(conf.URL_NX)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        self.browser.find_element(*self.add_new).click()

    def create_nxbar_notice(self, src, advanced_design, position):
        self.browser.find_element(*self.nx_title).send_keys('Notification Bar') if src.__eq__("nxbar") else \
            self.browser.find_element(*self.nx_title).send_keys('Notification Bar (Elementor)')

        # source page
        self.browser.find_element(*self.nx_bar).click()
        # next page design
        self.browser.find_element(*self.next_btn).click()

        # design page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        if src.__eq__("nxbar"):
            self.browser.find_element(*self.nxbar_template).click()
            if advanced_design.__eq__('y'):
                self.check_advanced_design(src)
        else:
            self.browser.find_element(*self.build_w_ele).click()
            self.browser.find_element(*self.nx_bar_ele_template).click()
            self.browser.find_element(*self.import_btn).click()
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.next_btn_for_wait)))
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.remove_elementor_design)))
            time.sleep(2)
        # next page content
        self.browser.find_element(*self.next_btn).click()

        # content page
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        if src.__eq__("nxbar"):
            self.browser.find_element(*self.content).click()
            self.browser.find_element(*self.content).send_keys('NotificationX Automation camp is Running...')
            # button text
            self.browser.find_element(*self.button_text).send_keys('Grab')
            # button url
            self.browser.find_element(*self.button_url).send_keys('https://notificationx.com/')

        # enable countdown
        self.browser.find_element(*self.enable_countdown).click()
        # if src.__eq__("nxbar"):
        # evergreen
        self.browser.find_element(*self.evergreen_timer).click()
        if src.__eq__("nxbar"):
            # countdown text
            self.browser.find_element(*self.countdown_text).send_keys('Grab it before')
        # randomize
        self.browser.find_element(*self.randomize).click()
        # randomize start time
        self.browser.find_element(*self.randomize_start_time).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.randomize_start_time).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.randomize_start_time).send_keys('5')
        # randomize end time
        self.browser.find_element(*self.randomize_end_time).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.randomize_end_time).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.randomize_end_time).send_keys('10')
        # daily time reset
        self.browser.find_element(*self.time_reset).click()
        # randomize
        self.browser.find_element(*self.randomize).click()
        # time rotation
        self.browser.find_element(*self.time_rotation).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*self.time_rotation).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.time_rotation).send_keys('9')
        # evergreen timer
        self.browser.find_element(*self.evergreen_timer).click()
        if src.__eq__("nxbar"):
            # expired text
            self.browser.find_element(*self.expired_text).send_keys(Keys.CONTROL, 'a')
            self.browser.find_element(*self.expired_text).send_keys(Keys.BACKSPACE)
            self.browser.find_element(*self.expired_text).send_keys('You missed it buddy, Try next time.')
        # start date
        self.browser.find_element(*self.start_date).click()
        self.browser.find_element(*self.goto_previous_month).click()
        if src.__eq__("nxbar"):
            self.browser.find_element(*self.choose_start_date).click()
            self.browser.find_element(*self.choose_start_date).click()
        else:
            self.browser.find_element(*self.choose_start_date_el).click()
            self.browser.find_element(*self.choose_start_date_el).click()
        # if src.__eq__("nxbar"):
        self.browser.find_element(*self.start_date).click()
        # end date
        self.browser.find_element(*self.end_date).click()
        self.browser.find_element(*self.goto_next_month).click()
        if src.__eq__("nxbar"):
            self.browser.find_element(*self.choose_end_date).click()
            self.browser.find_element(*self.choose_end_date).click()
        else:
            self.browser.find_element(*self.choose_end_date_el).click()
            self.browser.find_element(*self.choose_end_date_el).click()
        self.browser.find_element(*self.end_date).click()
        # permanent close
        self.browser.find_element(*self.permanent_close).click()

        # common tasks
        self.do_others(src, advanced_design, 'null', position)
