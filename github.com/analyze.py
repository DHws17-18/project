#!/usr/bin/env python
import os
import json


import matplotlib.pylab as plt

placeholder = [ 'github.ai', 'github.artificial', 'github.deep', 'github.machine' ] #, 'github.repos' ]
handles = []

if __name__ == '__main__':
  
  for foldername in placeholder:
    x = []
    y = []
    year = 2009
    #loop over each file in /github.repos
    for root, dirs, files in os.walk('./'+foldername):
      for file in files:
        #check if its json
        if file.endswith('.json'):
          #read lines
          with open('./' + foldername + '/' + file, encoding='utf-8') as githubfile:
            d = json.load(githubfile)
            githubfile.close()
            year += 1
            print(d["total_count"])
            x.append(year)
            y.append(d["total_count"])
#            for repo in d["items"]:
#                #repoJson = json.loads(repo)
#                print(repo["created_at"]))
      line, = plt.plot(x, y, label=foldername.replace('github.', ''))
      handles.append(line)

  plt.legend(handles=handles)
  plt.show()
