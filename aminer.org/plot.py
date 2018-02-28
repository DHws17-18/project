#!/usr/bin/env python
import os
import csv
import matplotlib.pylab as plt


keywords = [' AI ', ' Artificial Intelligence ', ' knn ', ' ann ', ' artificial neural network ', ' deep learning ', ' machine learning ', " 'thinking' computer systems "]
blankyears =  {'1930': 0, '1931': 0, '1932': 0, '1933': 0, '1934': 0, '1935': 0, '1936': 0, '1937': 0, '1938': 0, '1939': 0, '1940': 0, '1941': 0, '1942': 0, '1943': 0, '1944': 0, '1945': 0, '1946': 0, '1947': 0, '1948': 0, '1949': 0, '1950': 0, '1951': 0, '1952': 0, '1953': 0, '1954': 0, '1955': 0, '1956': 0, '1957': 0, '1958': 0, '1959': 0, '1960': 0, '1961': 0, '1962': 0, '1963': 0, '1964': 0, '1965': 0, '1966': 0, '1967': 0, '1968': 0, '1969': 0, '1970': 0, '1971': 0, '1972': 0, '1973': 0, '1974': 0, '1975': 0, '1976': 0, '1977': 0, '1978': 0, '1979': 0, '1980': 0, '1981': 0, '1982': 0, '1983': 0, '1984': 0, '1985': 0, '1986': 0, '1987': 0, '1988': 0, '1989': 0, '1990': 0, '1991': 0, '1992': 0, '1993': 0, '1994': 0, '1995': 0, '1996': 0, '1997': 0, '1998': 0, '1999': 0, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 0, '2005': 0, '2006': 0, '2007': 0, '2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0}
ignoreyears = [ '2017', '2018', '2019' ]
handles = []

if __name__ == '__main__':

  plt.figure(figsize=(18,8))

  with open('dblp.ai.csv', 'r') as csvfile:
    for keyword in keywords:
      years = blankyears.copy()
      reader = csv.DictReader(csvfile, fieldnames = ( 'year', 'title','keywords'), delimiter=';')
      for row in reader:
        if keyword in row['keywords']:
          years[row['year']]+=1
#      for ignore in ignoreyears:
#        years.pop(ignore)
      l = sorted(years.items())
      x, y = zip(*l)
      line, = plt.plot(x, y, label=keyword)
      handles.append(line)
      csvfile.seek(0)


  with open('dblp.all.csv', 'r') as csvfile:
    years = blankyears.copy()
    reader = csv.DictReader(csvfile, fieldnames = ( 'year', 'title','keywords'), delimiter=';')
    for row in reader:
      years[row['year']]+=1
#    for ignore in ignoreyears:
#      years.pop(ignore)
    l = sorted(years.items())
    x, y = zip(*l)
    line, = plt.plot(x, y, label=' all')
    handles.append(line)


#  ticks = list(range(1930, 2020, 10))
#  plt.xticks(ticks)
  plt.legend(handles=handles)
  plt.tight_layout()
  plt.show()
