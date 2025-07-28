#!/usr/bin/python3

import requests
import re

res = requests.get('https://monip.io');
print(res.text)
