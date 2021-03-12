import pytest
import json

from pages.result import PythonSearchResult
from pages.search import PythonSearch

from selenium.webdriver import Chrome, Firefox
import time

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome(
            executable_path="D:\Selenium Webdriver\chromedriver.exe")
    else:
        raise Exception(f'"{config_browser}" is not supported browser')

    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


def test_basic_python_search(browser):
    phrase = 'pycon'

    search_page = PythonSearch(browser)
    search_page.load()
    search_page.search(phrase)

    results_page = PythonSearchResult(browser)
    assert results_page.phrase_result_count() > 0
    assert results_page.search_input_value() == phrase
    time.sleep(10)
