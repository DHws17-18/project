#!/usr/bin/env python
import os
import json
import csv

#TODO keywords
keywords = [' Neural Network ', ' AI ', ' deep learning ', ' knn ']

f = open('dblp.csv','w')
#seek to begining to overwrite if file already exists
f.seek(0)
writer = csv.writer(f, delimiter=',')

def containsKeyWords(line):
  try:
    #parse json
    paperObj = json.loads(line)
    #loop keywords
    for keyword in keywords:
      #look for keyword
      if keyword in paperObj['abstract'] or keyword in paperObj['title']:
        #write csv
        writer.writerow([paperObj['year'], paperObj['id'], paperObj['title']])
        return 1
  #exception handeling TODO: keyError bei abstract?!? posible bad format " etc
  except KeyError:
    return 0 #print('Error in finding key in json')
  except json.decoder.JSONDecodeError:
    return 0 #print('Error in JSON in line ')

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
  #turncate if old file was larger and close outputfilestream
  f.truncate()
  f.close()
