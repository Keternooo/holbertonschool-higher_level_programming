#!/usr/bin/python3

import requests
res = requests.get('https://monip.io')
print(res.text)
