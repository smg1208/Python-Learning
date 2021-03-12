from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from gtts import gTTS
import os

language = 'vi'

Chapter = 1915
driver = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.minimize_window()
while True:
    reader = 'Thất Giới Vũ Thần - Chapter ' + str(Chapter)
    print(reader.center(60, '-'))
    driver.get(
        "https://truyen.tangthuvien.vn/doc-truyen/that-gioi-vu-than/chuong-" + str(Chapter))
    # driver.minimize_window()
    assert "Thất Giới Vũ Thần" in driver.title
    elem = driver.find_element_by_xpath(
        "//div[@class='chapter-c-content']")
    readercontent = elem.text.split(
        'Hãy nhấn like ở mỗi chương để ủng hộ tinh thần các dịch giả bạn nhé!')[0]
    # print(readercontent[0])
    # driver.close()

    myobj = gTTS(text=readercontent, tld='com', lang=language, slow=False)
    ChapterName = 'That Gioi Vu Than - ' + str(Chapter)+'.mp3'
    myobj.save(ChapterName)
    # os.system(ChapterName)
    Chapter += 1
    if Chapter == 2200:
        break
    # isContinue = bool(input(
    #     'Input anything to continue to next Chapter %s' % Chapter))
    # if isContinue == False:
    #     break
