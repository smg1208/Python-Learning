from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "E:\Selenium Webdriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('https://www.python.org')
print(driver.title)

search = driver.find_element_by_name('q')
search.send_keys('a')
search.send_keys(Keys.RETURN)
# time.sleep(100000)
try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    result = content.find_elements_by_tag_name('li')
    for i in result:
        title = i.find_element_by_tag_name('h3')
        print(title.text)
    
finally: 
    driver.quit()

driver.quit()