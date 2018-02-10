#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GoogleScholarResCount import CrawlCount

import json

topic = 'hello world'

crawl_counter = CrawlCount(topic)

# default: firefox, without private/incognito mode, default binary path for browser
crawl_counter.crawl_result_count(1960, 2017)
# with options
# crawl_counter.fill_res_count_dict(1960, 1962, driver='chrome', incognito=True, browser_bin_path='/bin/google-chrome-stable')

# just use selenium
# crawl_counter.crawl_result_count_selenium(1960, 2017)

topic_count_dict = crawl_counter.result_count_dict

json_obj = json.dumps(topic_count_dict, indent=4)
filename = topic.replace(' ','_') + '.json'
fp = open(filename, 'w')
print(json_obj)
print(json_obj, file=fp)
print('written to ' + filename)
fp.close()
