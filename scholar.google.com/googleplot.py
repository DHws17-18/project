#!/usr/bin/env python
import os
import sys
import json
import csv
import traceback
import matplotlib.pylab as plt

print('Google scholar plotting')
directiories = [
    'data-backups',
    'data-backups-1'
]
try:
    years = list(range(1920, 2018))
    handles = []
    # directory = 'data-backups'
    for directory in directiories:
        for fn in os.listdir(directory):
            json_data = json.load(open(directory + '/' + fn))
            result_data = []
            for year in years:
                result_data.append(json_data['results'][str(year)])
            label = directory + '/' + str(fn) + ' ' + json_data['datetime']
            line, = plt.plot(years, result_data, label=label)
            handles.append(line)

    plt.legend(handles=handles)

    ticks = list(range(min(years), max(years)+1, 5))
    print('Ticks', ticks)
    plt.xticks(ticks)
    # plt.savefig('googlescholar_plot.png')
    plt.show()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Unexpected error:", exc_type)
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
