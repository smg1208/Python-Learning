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
import database as db

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
def post_to_fb(pageid, data, resource, hashtag, token):
    graph = facebook.GraphAPI(
        access_token=token, version="3.1")

    fbmess = '['+resource+'] '+data[0] + '\n' + data[1] + '\n' + \
        'Xem thêm tại: ' + ' ' + data[3] + '\n' + hashtag
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

# Created folder


def create_folder(name):
    parent_dir = os.getcwd()
    create_dir = parent_dir + '\\'+name
    try:
        os.mkdir(create_dir)
    except Exception as i:
        print('Error: ', i)
