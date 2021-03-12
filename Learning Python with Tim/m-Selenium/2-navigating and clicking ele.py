from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "E:\Selenium Webdriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('https://www.python.org')


search = driver.find_element_by_name('q')
search.send_keys('tutorials')
search.send_keys(Keys.RETURN)
# time.sleep(100000)
try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    result = driver.find_elements_by_xpath('//li/h3/a')
    data = [e.text for e in result]
    for e in data:
        ele = driver.find_element_by_link_text(e)
        link = ele.get_attribute('href')
        text = ele.text
        print(link, text)
        ele.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text"))
            )

            driver.back()
            result_label = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//form/h3"))
            )
            print(f'Go to {link} done!')
        except Exception:
            pass


finally:
    driver.quit()

driver.quit()
