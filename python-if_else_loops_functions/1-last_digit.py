#!/usr/bin/python3
import requests
req = requests.get('https://monip.io')
print(req.text)
