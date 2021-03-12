from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
driver.get('https://www.python.org')
assert "Python" in driver.title
ele = driver.find_element_by_name('q')
ele.clear()
ele.send_keys('pycon')
ele.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
time.sleep(30)
driver.close()