import requests

response = requests.get('http://dev-ta.mooo.com/api/v1/game?display_type=1')

print(response.json()["data"]["items"])