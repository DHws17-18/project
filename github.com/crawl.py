#!/usr/bin/env python
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.content)
