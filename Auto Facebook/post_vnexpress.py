import facebook
from selenium.webdriver.common.keys import Keys
from _datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
import selenium
import io
import os
import re
import urllib.request
import urllib.parse
import bs4
from selenium import webdriver

# get new source


def geturl(url, cls):
    req = urllib.request.urlopen(url)
    parse_lxml = bs4.BeautifulSoup(req, 'lxml')
    return parse_lxml.select(cls)


# get list url from new source
def getlisturl(data):
    list_a = []
    news = []
    for i in data:
        list_a.append(i.find('a'))
    for j in range(len(list_a)):
        try:
            url_j = list_a[j].get('href')
            # print(j, '. ', url_j)
            news.append(url_j)
        except Exception:
            print('Error: ', j)
    return news


# get data from news
def getpostdetail(url, cls, numberofpost, imgPath):
    # print(url)
    title_data = geturl(url, cls[0])
    title = title_data[0].text.strip()
    print('title: ', title)

    desc_data = geturl(url, cls[1])
    desc = desc_data[0].text.strip()
    print('Descriptions: ', desc)

    try:
        img_data = geturl(url, cls[2])[0].find('img').get('data-src')
        full_path = imgPath + str(numberofpost)+'.jpg'
        # download image
        urllib.request.urlretrieve(img_data, full_path)

    except Exception:
        full_path = ''
    return [title, desc, full_path]

# post to facebook


def post_to_fb(pageid, data, resource, hashtag):
    graph = facebook.GraphAPI(
        access_token='EAARCN722BG4BABHVxAyaFFh8MQBLq9DFpbzobIoFB9DOfy646IZCMtaHIVBcGvppPUaihDgewL5djBknkIU8CTL2yq0xEFU2hiUvrA6HlKCZBJqrrTKl2M8lyNVZCNamiwv44Ci37Sps6Ts5U1ZBpK0U2lf9mB01AQUDHY4Cv0elwHc9zXUeMd7DMuTHqAsZD', version="3.1")

    fbmess = data[0] + '\n' + data[1] + '\n' + \
        resource + ' ' + data[3] + '\n' + hashtag    
    if data[2] != '':
        post = graph.put_photo(
            parent_object=pageid,
            connection_name="feed",
            message=fbmess,            
            image=open(data[2], 'rb')
        )
    else:
        graph.put_object(
            parent_object=pageid,
            connection_name="feed",
            message=fbmess,            
        )


Booking_ID = '113298130427391'
Hands_ID = '106368554441874'
# Get link from vnexpress
url = 'https://vnexpress.net/du-lich/tu-van/kinh-nghiem'
cls = '.item-news'
data_url = geturl(url, cls)
news_vnexpress = getlisturl(data_url)

vnexpress = 0
tuoitre = 0
while vnexpress < len(news_vnexpress):
    print('www.vnexpress.net'.center(120, '-'))
    print(vnexpress, '. ', news_vnexpress[vnexpress])
    isPosted = True
    list_cls = ['.title-detail', '.description', '.tplCaption']
    imgPath = 'vnexpress/'
    dataToPost = getpostdetail(
        news_vnexpress[vnexpress], list_cls, vnexpress, imgPath)
    dataToPost.append(news_vnexpress[vnexpress])
    print(dataToPost)
    try:
        post_to_fb(Booking_ID, dataToPost, 'Xem thêm tại ',
                   '#news #travelling #tuvan #dulich #trainghiem #kinhnghiemdechill #summer #travel #2mbooking #2m #vnepress')
    except Exception as i:
        print('err: ', i)
        isPosted = False

    vnexpress += 1
    if isPosted == True:
        print('Posted! Waiting for 30mins for next post!')
        time.sleep(30*60)
    else:
        print('Posting failed! Waiting for next post!')
