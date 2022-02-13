from utils.create_notice_helper import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Manage(Helper):
    delete_btn_on_editor = (By.XPATH, f"//button[normalize-space()='Delete']")
    update_btn_on_editor = (By.XPATH, f"//button[normalize-space()='Update']")
    delete_btn_on_dashboard = (By.XPATH, f"")
    delete_popup_des = (By.XPATH, f"//div[@id='swal2-html-container']")
    delete_popup_icon = (By.XPATH, f"//div[@class='swal2-icon swal2-error swal2-icon-show']")
    delete_popup_no = (By.XPATH, f"//button[normalize-space()='No, Cancel']")
    delete_popup_yes = (By.XPATH, f"//button[normalize-space()='Yes, Delete It']")
    ana_view = f"//span[normalize-space()='Total Views']"
    ana_view_count = (By.XPATH, f'//*[@id="notificationx"]/div/div[1]/div[2]/div[1]/div/a/div/span[1]')
    ana_click = (By.XPATH, f"//span[normalize-space()='Total Clicks']")
    ana_click_count = (By.XPATH, f'//*[@id="notificationx"]/div/div[1]/div[2]/div[2]/div/a/div/span[1]')
    ana_ctr = (By.XPATH, f"//span[normalize-space()='Click-Through-Rate']")
    ana_ctr_count = (By.XPATH, f'//*[@id="notificationx"]/div/div[1]/div[2]/div[3]/div/a/div/span[1]')

    bulk_action = (By.XPATH, f"//div[@class='bulk-action-select css-2b097c-container']")
    bulk_action_enable = (By.ID, f'react-select-2-option-1')
    bulk_action_disable = (By.ID, f'react-select-2-option-2')
    bulk_action_regenerate = (By.ID, f'react-select-2-option-3')
    bulk_action_cdn = (By.ID, f'react-select-2-option-4')
    bulk_action_delete = (By.ID, f'react-select-2-option-5')
    bulk_action_apply_btn = (By.XPATH, f"//button[@class='nx-bulk-action-button']")
    select_all = (By.XPATH, f"//input[@name='nx_all']")

    single_enable_disable_notice = (By.XPATH, f'//tbody/tr[1]/td[4]/div/label')
    single_title = (By.XPATH, f"//tbody/tr[1]/td[2]/div[1]/strong[1]/a[1]")
    single_type = (By.XPATH, f"//tbody/tr[1]/td[5]/div[1]")
    single_status = (By.XPATH, f"//tbody/tr[1]/td[7]/div[1]")
    single_date = (By.XPATH, f"//tbody/tr[1]/td[7]/div[1]/span[1]")
    single_view = (By.XPATH, f"//tbody/tr[1]/td[6]/div[1]/a[1]")
    single_edit = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/a[1]")
    single_wpml = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/a[2]")
    single_duplicate = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/a[3]")
    single_shortcode = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/button[1]")
    single_cross_site_domain = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/a[4]")
    single_regenerate = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/button[2]")
    single_delete = (By.XPATH, f"//tbody/tr[1]/td[8]/div[1]/button[3]")

    toast_msg_icon = f"//div[@class='nx-toast-wrapper']//img"
    toast_msg_des = f"//div[@class='nx-toast-wrapper']//p"
    toast_msg_close_btn = (By.XPATH, f"//button[@class='Toastify__close-button Toastify__close-button--light']")

    toast_msg_bulk_enable_text = "20 Notification Alerts have been Enabled."
    toast_msg_bulk_disable_text = "20 Notification Alerts have been Disabled."
    toast_msg_bulk_regenerate_text = "15 Notification Alerts have been Regenerated."
    toast_msg_bulk_delete_text = "20 notification Alerts have been Deleted."

    toast_msg_enable_text = "Notification Alert has been Enabled."
    toast_msg_disable_text = "Notification Alert has been Disabled."
    toast_msg_regenerate_text = "Notification Alert has been Regenerated."
    toast_msg_cdn_text = "Cross Domain Notice code has been copied to Clipboard."
    toast_msg_delete_text = "Notification Alert has been Deleted."
    toast_msg_shortcode_regular_text = "Regular Notification Alert has been copied to Clipboard."
    toast_msg_shortcode_inline_text = "Inline Notification Alert has been copied to Clipboard."

    popup_title = (By.XPATH, f"//h2[@id='swal2-title']")
    shortcode_popup_regular_copy = (By.XPATH, f"//code[@id='regulat-shortcode']")
    shortcode_popup_inline_copy = (By.XPATH, f"//code[@id='inline-shortcode']")
    popup_cancel = (By.XPATH, f"//button[normalize-space()='Cancel']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def create_shortcode(self):
        self.browser.find_element(*self.single_shortcode).click()
        # Regular
        assert_that(self.browser.find_element(*self.popup_title).text).\
            is_equal_to("Copy to Clipboard")
        self.browser.find_element(*self.shortcode_popup_regular_copy).click()

        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
            is_equal_to(self.toast_msg_shortcode_regular_text)
        self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
        self.browser.find_element(*self.toast_msg_close_btn).click()

        # Inline
        self.browser.find_element(*self.shortcode_popup_inline_copy).click()

        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
            is_equal_to(self.toast_msg_shortcode_inline_text)
        self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
        self.browser.find_element(*self.toast_msg_close_btn).click()

        self.browser.find_element(*self.popup_cancel).click()

    def go_to_edit_page(self):
        self.browser.find_element(*self.single_edit).click()
        if self.browser.find_element(By.XPATH, f"//span[normalize-space()='Source']").is_displayed():
            assert_that(1).is_equal_to(1)
            self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()

        else:
            assert_that('Success').is_equal_to("Edit button not working.")
            self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()

    def duplicate_notice(self):
        self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()
        original_title = self.browser.find_element(*self.single_title).text
        self.browser.find_element(*self.single_duplicate).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[normalize-space()='Publish']")))
        if self.browser.find_element(By.XPATH, f"//button[normalize-space()='Publish']").is_displayed():
            self.browser.find_element(*self.publish_btn).click()
            element = WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located((By.XPATH, self.success_notice)))

            assert_that(element.text).is_equal_to("Successfully Created.")
            self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()
            assert_that(self.browser.find_element(By.XPATH, '//tbody/tr[2]/td[2]/div[1]/strong[1]/a[1]').text).\
                is_equal_to(original_title + " - Copy")
        else:
            assert_that('Success').is_equal_to(0)
            self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()

    def cross_domain_notice(self, type):
        if type.__eq__('bulk'):
            self.browser.find_element(*self.select_all).click()
            self.browser.find_element(*self.bulk_action).click()
            self.browser.find_element(*self.bulk_action_cdn).click()
            self.browser.find_element(*self.bulk_action_apply_btn).click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
            time.sleep(1)
            # assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text).\
            #     is_equal_to(self.toast_msg_cdn_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()
        else:
            self.browser.find_element(*self.single_cross_site_domain).click()
            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))

            assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text).\
                is_equal_to(self.toast_msg_cdn_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()

    def disable_notice(self, type):
        self.browser.execute_script("location.reload(true);")
        if type.__eq__('bulk'):
            self.browser.find_element(*self.select_all).click()
            self.browser.find_element(*self.bulk_action).click()
            self.browser.find_element(*self.bulk_action_disable).click()
            self.browser.find_element(*self.bulk_action_apply_btn).click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
            time.sleep(1)
            # assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text).\
            #     is_equal_to(self.toast_msg_bulk_disable_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()
        else:
            self.browser.find_element(*self.single_enable_disable_notice).click()
            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))

            assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text).\
                is_equal_to(self.toast_msg_disable_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()

    def enable_notice(self, type):
        self.browser.execute_script("location.reload(true);")
        if type.__eq__('bulk'):
            self.browser.find_element(*self.select_all).click()
            self.browser.find_element(*self.bulk_action).click()
            self.browser.find_element(*self.bulk_action_enable).click()
            self.browser.find_element(*self.bulk_action_apply_btn).click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
            time.sleep(1)
            assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text).\
                is_equal_to(self.toast_msg_bulk_enable_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()
        else:
            self.browser.find_element(*self.single_enable_disable_notice).click()
            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))

            assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text).\
                is_equal_to(self.toast_msg_enable_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()

    def regenerate_notice(self, type):
        if type.__eq__('bulk'):
            self.browser.find_element(*self.select_all).click()
            self.browser.find_element(*self.bulk_action).click()
            self.browser.find_element(*self.bulk_action_regenerate).click()
            self.browser.find_element(*self.bulk_action_apply_btn).click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
            time.sleep(1)
            # assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
            #     is_equal_to(self.toast_msg_bulk_regenerate_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()
        else:
            self.browser.find_element(*self.single_regenerate).click()

            assert_that(self.browser.find_element(*self.popup_title).text).\
                is_equal_to("Are you sure you want to Regenerate?")
            self.browser.find_element(*self.popup_cancel).click()
            self.browser.find_element(*self.single_regenerate).click()
            self.browser.find_element(By.XPATH, f"//button[contains(text(),'Regenerate')]").click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))

            assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
                is_equal_to(self.toast_msg_regenerate_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()

    def update_notice(self):
        self.browser.find_element(*self.single_title).click()

        self.browser.find_element(*self.update_btn_on_editor).click()

        element = WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, self.success_notice)))

        assert_that(element.text).is_equal_to("Successfully Updated.")
        self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()

    def delete_notice_from_edit_page(self):
        self.browser.find_element(*self.single_title).click()
        self.browser.find_element(*self.delete_btn_on_editor).click()

        assert_that(self.browser.find_element(*self.popup_title).text).is_equal_to("Are you sure?")
        assert_that(self.browser.find_element(*self.delete_popup_des).text). \
            is_equal_to("You won't be able to revert this!")

        if self.browser.find_element(*self.delete_popup_icon).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that(1).is_equal_to("Icon is not visible")

        self.browser.find_element(*self.delete_popup_no).click()
        self.browser.find_element(*self.delete_btn_on_editor).click()
        self.browser.find_element(*self.delete_popup_yes).click()

        element = WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, self.ana_view)))

        assert_that(element.text).is_equal_to("Total Views")

        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
            is_equal_to(self.toast_msg_delete_text)
        self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
        self.browser.find_element(*self.toast_msg_close_btn).click()

    def delete_notice(self, type):
        if type.__eq__('bulk'):
            self.browser.find_element(By.XPATH, f"//div[normalize-space()='NotificationX']").click()
            self.browser.find_element(*self.select_all).click()
            self.browser.find_element(*self.bulk_action).click()
            self.browser.find_element(*self.bulk_action_delete).click()
            self.browser.find_element(*self.bulk_action_apply_btn).click()

            assert_that(self.browser.find_element(*self.popup_title).text).\
                is_equal_to("Are you sure?")
            self.browser.find_element(*self.delete_popup_no).click()
            time.sleep(1)
            self.browser.find_element(*self.bulk_action_apply_btn).click()
            self.browser.find_element(*self.delete_popup_yes).click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
            time.sleep(1)
            # assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
            #     is_equal_to(self.toast_msg_bulk_delete_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()
        else:
            self.browser.find_element(*self.single_delete).click()

            assert_that(self.browser.find_element(*self.popup_title).text). \
                is_equal_to("Are you sure?")
            self.browser.find_element(*self.delete_popup_no).click()
            time.sleep(1)
            self.browser.find_element(*self.single_delete).click()
            self.browser.find_element(*self.delete_popup_yes).click()

            WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.toast_msg_des)))
            time.sleep(1)
            assert_that(self.browser.find_element(By.XPATH, self.toast_msg_des).text). \
                is_equal_to(self.toast_msg_delete_text)
            self.check_visibility(self.toast_msg_icon, "Toast Notice Icon is not visible.")
            self.browser.find_element(*self.toast_msg_close_btn).click()



