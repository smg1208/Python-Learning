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
import function as f

for site in db.newspaper:
    site_db = db.newspaper.get(site)
    # Check old link from data
    filex = open(site_db.get('list_link'), 'r')
    old_link_from_site = filex.readlines()
    data_w = old_link_from_site
    filex.close()

    # get current link from site
    data_url = f.geturl(site_db.get('url'), site_db.get('cls'))
    link_from_site = f.getlisturl(data_url)

    new_link_from_site = [
        i for i in link_from_site if i+'\n' not in old_link_from_site]
    print(new_link_from_site)
    link_number = len(old_link_from_site) + len(new_link_from_site)
    while link_number > len(old_link_from_site):
        link_number -= 1
        print('Post from %s'.center(120, '-'), site)
        print(link_number, '. ',
              new_link_from_site[link_number-len(old_link_from_site)])
        isPosted = True
        list_cls = site_db.get('sub-cls')
        imgPath = site+'/'
        dataToPost = f.getpostdetail(
            new_link_from_site[link_number-len(old_link_from_site) ], list_cls, link_number, imgPath)
        dataToPost.append(
            new_link_from_site[link_number-len(old_link_from_site)])
        print(dataToPost)
        try:
            f.post_to_fb(db.page_id.get('booking').get('id'), dataToPost, site,
                         '#news #travelling #tuvan #dulich #trainghiem #kinhnghiemdechill #travel #2mbooking #2m' + ' #'+site,db.page_id.get('booking').get('token'))
        except Exception as i:
            print('err: ', i)
            isPosted = False
        
        if isPosted == True:            
            data_w.append(
                new_link_from_site[link_number-len(old_link_from_site)]+'\n')
            filex = open(site_db.get('list_link'), 'w')
            for l in data_w:
                filex.write(l)
            filex.close()
            print('Posted! Waiting for 30mins for next post!')
            time.sleep(30*60)            
        else:
            print('Posting failed! Waiting for next post!')

    break
