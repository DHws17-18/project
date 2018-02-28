#!/usr/bin/env python
import os
import json
import csv

#TODO keywords
keywords = [' AI ', ' Artificial Intelligence ', ' knn ', ' ann ', ' artificial neural network ', ' deep learning ', ' machine learning ', " 'thinking' computer systems "]

aiCsv = open('dblp.ai.csv','w')
allCsv = open('dblp.all.csv','w')
aiCsv.seek(0)
allCsv.seek(0)
aiWriter = csv.writer(aiCsv, delimiter=';')
allWriter = csv.writer(allCsv, delimiter=';')


def containsKeyWords(line):
  try:
    paperObj = json.loads(line)    
    relevant = False
    hits = []
    for keyword in keywords:
      if keyword in paperObj['abstract'] or keyword in paperObj['title']:
          relevant = True
          hits.append(keyword)
    if relevant:
      aiWriter.writerow([paperObj['year'], paperObj['title'].encode('utf-8', 'ignore'), ''.join(hits)])
      allWriter.writerow([paperObj['year'], paperObj['title'].encode('utf-8', 'ignore')])
      return 2
    else:
      allWriter.writerow([paperObj['year'], paperObj['title'].encode('utf-8', 'ignore')])
      return 1    
  except KeyError:
    #print(line)
    return 0

if __name__ == '__main__':
  count = 0
  found = 0
  notfound = 0
  emptyfielderror = 0
  decodererror = 0
  
  for root, dirs, files in os.walk('./dblp-ref/'):
    for file in files:
      if file.endswith('.json'):
        with open('./dblp-ref/' + file) as dblpfile:
          for line in dblpfile:
            count += 1
            case = containsKeyWords(line)
            if case == 2:
              found += 1
            if case == 1:
              notfound += 1
            if case == 0:
              emptyfielderror += 1
            if case == -1:
              decodererror += 1
          print(file)

  print('\nprocessed papers:',count,'\n')
  print('keyword found:',found)
  print('keyword not found:',notfound)
  print('emptyfielderror:',emptyfielderror)
  print('decodererror:',decodererror)
  print('sum', found + notfound + emptyfielderror + decodererror)

  
  #truncate if old file was larger and close outputfilestream
  aiCsv.truncate()
  aiCsv.close()
  allCsv.truncate()
  allCsv.close()
