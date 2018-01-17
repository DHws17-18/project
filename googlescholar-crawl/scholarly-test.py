#!/usr/bin/env python

import scholarly
import time

topic = 'neural network'
numberOfPubs = 15

search_query = scholarly.search_pubs_query(topic)
for counter in range(numberOfPubs):
    out = str(counter + 1) + ': ' + next(search_query).bib['title']
    print(out)
    if (counter + 1) % 10 == 0:
        time.sleep(5)
