import sys
import json
import pytest
from selenium import webdriver


@pytest.fixture
def config(scope='session'):
    with open(str(sys.path[1]) + '/utils/config.json') as config_file:
        config = json.load(config_file)

    assert isinstance(config['implicitly_wait'], int)

    return config


@pytest.fixture
def browser(config):
    b = webdriver.Chrome(str(sys.path[1]) + '/driver/chromedriver.exe')
    b.maximize_window()

    b.implicitly_wait(config['implicitly_wait'])
