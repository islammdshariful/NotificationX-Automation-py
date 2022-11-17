import platform
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path


# This will run before all test case
@pytest.fixture(scope='module')
def browser():
    options = Options()
    # # opts.add_experimental_option("detach", True)
    # options.add_experimental_option('debuggerAddress', 'localhost:9250')

    if platform.system().__eq__("Windows"):
        # For Windows
        path = str(Path(__file__).parent.parent) + "/venv/Lib/site-packages/seleniumbase/drivers/chromedriver.exe"
    else:
        # For Mac
        path = str(
            Path(__file__).parent.parent) + "/venv/lib/python3.10/site-packages/seleniumbase/drivers/chromedriver"

    browser = webdriver.Chrome(executable_path=path, chrome_options=options)
    browser.maximize_window()
    browser.implicitly_wait('10')

    yield browser

    # browser.quit()
