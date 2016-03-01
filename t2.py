import requests
import json

url = 'http://www.jerrynest.com'
headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': '(iPhone; iOS 7.0.4; Scale/2.00)'}
r = requests.get(url, verify=False, headers=headers)
print r.json
