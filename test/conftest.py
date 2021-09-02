import sys
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def config(scope='session'):
    with open(str(sys.path[1]) + '/utils/config.json') as config_file:
        config = json.load(config_file)

    assert isinstance(config['implicitly_wait'], int)

    return config


@pytest.fixture
def browser(config):
    opts = Options()
    opts.add_experimental_option("detach", True)
    # opts.add_experimental_option('debuggerAddress', 'localhost:9250')
    # b = webdriver.Chrome(str(sys.path[1]) + '/driver/chromedriver.exe')
    b = webdriver.Chrome(executable_path=str(sys.path[1]) + '/driver/chromedriver.exe', chrome_options=opts)
    b.maximize_window()

    b.implicitly_wait(config['implicitly_wait'])

    yield b

    # b.quit()
