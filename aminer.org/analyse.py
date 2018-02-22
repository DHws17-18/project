#!/usr/bin/env python
import os
import json
import csv

#TODO keywords
keywords = [' AI ', ' Artificial Intelligence ', ' knn ', ' ann ', ' artificial neural network ', ' deep learning ', ' machine learning ', " 'thinking' computer systems "]

aiCsv = open('dblp.ai.csv','w')
allCsv = open('dblp.all.csv','w')
#seek to beginning to overwrite if file already exists
aiCsv.seek(0)
allCsv.seek(0)
aiWriter = csv.writer(aiCsv, delimiter=';')
allWriter = csv.writer(allCsv, delimiter=';')

def containsKeyWords(line):
  try:    
    #parse json
    paperObj = json.loads(line)    
    #loop keywords
    relevant = False
    hits = []
    for keyword in keywords:
      #look for keyword
      if keyword in paperObj['abstract'] or keyword in paperObj['title']:
          relevant = True
          hits.append(keyword)
    #write    
    if relevant:
      aiWriter.writerow([paperObj['year'], paperObj['title'].encode('utf-8', 'ignore'), ''.join(hits)])
      return 1
    else:
      allWriter.writerow([paperObj['year'], paperObj['title'].encode('utf-8', 'ignore')])
      return 0    
  except KeyError:
    return 0
  except json.decoder.JSONDecodeError:
    return 0

if __name__ == '__main__':
  #write csv header
  #writer.writerow(['year', 'id', 'title'])
  #loop over each file in /dblp-ref
  for root, dirs, files in os.walk('./dblp-ref/'):
    for file in files:
      #check if its json
      if file.endswith('.json'):
        #read lines
        with open('./dblp-ref/' + file) as dblpfile:
          count = 0
          found = 0
          for line in dblpfile:
            count += 1 
            if containsKeyWords(line) == 1:
              found += 1
          print(file, '\tpapers:', count, '\tAI related:', found)
  #truncate if old file was larger and close outputfilestream
  aiCsv.truncate()
  aiCsv.close()
  allCsv.truncate()
  allCsv.close()
