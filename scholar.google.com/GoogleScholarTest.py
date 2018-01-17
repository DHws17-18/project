#!/usr/bin/env python3
from GoogleScholar import Crawler

#
topic = 'hello world'

# search multible pages at once
raw_scholar_data = Crawler(topic).search_pages(pages=2)

# search specific page
#raw_scholar_data = Crawler(topic).search_page(100000000000000)

print(raw_scholar_data)
