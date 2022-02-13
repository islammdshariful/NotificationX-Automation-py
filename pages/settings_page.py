from utils.create_notice_helper import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Settings(Helper):
    settings_menu = (By.XPATH, f"//a[@href='admin.php?page=nx-settings']")
    save_settings_btn = (By.XPATH, f"//button[normalize-space()='Save Settings']")
    general = (By.XPATH, f"//span[normalize-space()='General']")
    advanced_settings = (By.XPATH, f"//span[normalize-space()='Advanced Settings']")
    analytics = (By.XPATH, f"//span[normalize-space()='Analytics & Reporting']")
    cache_Settings = (By.XPATH, f"//span[normalize-space()='Cache Settings']")
    miscellaneous = (By.XPATH, f"//span[normalize-space()='Miscellaneous']")
    api_integrations = (By.XPATH, f"//span[normalize-space()='API Integrations']")
    license = (By.XPATH, f"//span[normalize-space()='License']")
    general_module_nx_bar = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                       f"//label[@for='modules_bar']")
    general_module_cf7 = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                       f"//label[@for='modules_cf7']")
    general_module_freemius = (By.XPATH, f"//div[@class='wprf-toggle-wrap wprf-checked wprf-label-position-right']"
                                       f"//label[@for='modules_freemius']")

    def general_tab(self):
        self.browser.find_element(*self.settings_menu).click()
        self.browser.find_element(*self.general).click()

        self.browser.find_element(*self.general_module_nx_bar).click()
        self.browser.find_element(*self.general_module_cf7).click()
        self.browser.find_element(*self.general_module_freemius).click()

        self.browser.find_element(*self.save_settings_btn).click()
