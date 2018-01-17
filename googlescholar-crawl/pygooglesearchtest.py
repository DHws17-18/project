#!/usr/bin/env python

from pyGoogleSearch import *

topic = 'hello world'

# COLLECT DATA FROM GOOGLE SCHOLAR SEARCH

# outputs in json format
raw_scholar_data = Google(topic, pages=1).search_scholar()
print(raw_scholar_data)
# print('source: ' + raw_scholar_data['source'])

# takes data from json, collects content from all urls and outputs to a list comprehension
# output_scholar_data = DataHandler(raw_scholar_data).aggregate_data()
# write_csv(output_scholar_data, 'scholar_data.csv')

# Site specfic search and special characters in search query

# topic = 'social emotional learning AND \"healthy school culture\"'
# d = Google(topic, site='edutopia.org').search()
# print(json.dumps(d, indent=2))
