#!/usr/bin/env python3
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.content)
