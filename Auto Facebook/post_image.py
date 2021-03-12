import facebook
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

graph = facebook.GraphAPI(
    access_token='EAARCN722BG4BABHVxAyaFFh8MQBLq9DFpbzobIoFB9DOfy646IZCMtaHIVBcGvppPUaihDgewL5djBknkIU8CTL2yq0xEFU2hiUvrA6HlKCZBJqrrTKl2M8lyNVZCNamiwv44Ci37Sps6Ts5U1ZBpK0U2lf9mB01AQUDHY4Cv0elwHc9zXUeMd7DMuTHqAsZD', version="3.1")

post = graph.put_photo(
  parent_object='113298130427391',
  connection_name="feed",
  message='Sunflower!',
  image=open("E:\P H O T O\Al\Graduations date\\100NCD90\DSC_0003.JPG",'rb')
)
