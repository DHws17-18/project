#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GoogleScholarResCount import CrawlCount

import json

topic = 'neural network'

# topic_count = CrawlCount(topic).get_result_count(1900)
topic_count_dict = CrawlCount(topic).get_year_count_dict(1960, 1962)
json_obj = json.dumps(topic_count_dict, indent=4)
fp = open(topic.replace(' ','_') + '.json', 'w')
print(json_obj)
print(json_obj, file=fp)
fp.close()
