import requests
from html import unescape
from html import escape
import io

# Making a GET request
r = requests.get('https://11bet.us/api/v1/tp/numberGameUrl')
json = r.json()
print(json)
for i in json:
    print(i['partner_provider'])
print('-'*50)
for i in json:
    print(i['partner_game_id'])
print('-'*50)
for i in json:
    print(i['name'])