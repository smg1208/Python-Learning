from selenium.webdriver.common.keys import Keys
from _datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
import selenium
import io
import re
import urllib.request
import urllib.parse
import bs4
from selenium import webdriver

x = urllib.request.urlopen('https://vnexpress.net/tin-tuc-24h')
read = bs4.BeautifulSoup(x, 'lxml')
read1 = read.select('.item-news')


test = []

for i in read1:
    test.append(i.find('a'))
for j in range(len(test)):
    try:
        url = test[j].get('href')
        print(url)
    except Exception:
        print('Error: ', j)


# with open('credential.csv') as f1:
#     csvrow = csv.reader(f1, delimeter=',')
email = '01208127027'
password = 'hanhdan1'

option = webdriver.ChromeOptions()
option.headless = False
prefs = {'profile.default_content_setting.notifications': 2}
option.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
time.sleep(5)
driver.get('https://www.facebook.com/')
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('u_0_b').click()
time.sleep(1000)
