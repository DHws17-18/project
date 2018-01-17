#!/usr/bin/env python
import os
import json


import matplotlib.pylab as plt

year = 2009

x = []
y = []

if __name__ == '__main__':
  #loop over each file in /github.repos
  for root, dirs, files in os.walk('./github.repos/'):
    for file in files:
      #check if its json
      if file.endswith('.json'):
        #read lines
        with open('./github.repos/' + file) as githubfile:
          d = json.load(githubfile)
          githubfile.close()
          year += 1
          print(d["total_count"])
          x.append(year)
          y.append(d["total_count"])
#          for repo in d["items"]:
#              #repoJson = json.loads(repo)
#              print(repo["created_at"])
  plt.plot(x, y)
  plt.show()

#TODO: 
  year = 2009

  x = []
  y = []
  
  #loop over each file in /githubdata
  for root, dirs, files in os.walk('./github.ai/'):
    for file in files:
      #check if its json
      if file.endswith('.json'):
        #read lines
        with open('./github.ai/' + file) as githubfile:
          c = json.load(githubfile)
          githubfile.close()
          year += 1
          print(c["total_count"])
          x.append(year)
          y.append(c["total_count"])
#          for repo in d["items"]:
#              #repoJson = json.loads(repo)
#              print(repo["created_at"])
  plt.plot(x, y)
  plt.show()
