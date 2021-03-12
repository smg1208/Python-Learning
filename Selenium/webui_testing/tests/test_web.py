import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def browser():
    driver = Chrome(executable_path="D:\Selenium Webdriver\chromedriver.exe")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_basic_python_org_search(browser):
    URL = 'https://www.python.org'
    PHRASE = 'pycon'

    browser.get(URL)

    search_input = browser.find_element_by_name('q')
    search_input.send_keys(PHRASE + Keys.RETURN)

    # link_divs = browser.find_elements_by_css_selector('#links > div')
    # assert len(link_divs) > 0

    xpath = "//ul[@class='list-recent-events menu']/li"
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == PHRASE
    time.sleep(5)