#!/usr/bin/env python
import os
import json
import csv
import matplotlib.pylab as plt

years = {}
f = open('dblp.csv','r')

if __name__ == '__main__':
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    if not row[0] in years:
      years.update({ row[0] : 1 })
    else:
      years[row[0]]+=1

  #remove 2018
  years.pop('2018', None)

  l = sorted(years.items()) 
  print(l)
  x, y = zip(*l)
  
  plt.plot(x, y)
  plt.show()
