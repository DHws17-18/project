#!/usr/bin/env python
from time import sleep
from bs4 import BeautifulSoup
import re
import requests
import urllib.parse

class CrawlCount:
    def __init__(self, query='hello world', startyear=1900, endyear=1900, sleep=True):
        self.query = '+'.join(query.split(' '))
        self.startyear = startyear
        self.endyear = endyear
        self.sleep = sleep
        self.headers = {'user-agent': 'Mozilla/5.0'}

    def get_result_count(self, year):
        url = UrlGenerator(self.query, year, year).scholar_url
        print('requesting: ' + url)
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print("error " + str(response.status_code))
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        result_count_str = soup.find(id="gs_ab_md").div.get_text().split(' ')[1].replace(',', '')
        result_count = int(result_count_str)
        return result_count

    def get_result_count_range(self, customstartyear, customendyear):
        url = UrlGenerator(self.query, customstartyear, customendyear).scholar_url
        print('requesting: ' + url)
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print("error " + str(response.status_code))
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        result_count_str = soup.find(id="gs_ab_md").div.get_text().split(' ')[1].replace(',', '')
        result_count = int(result_count_str)
        return result_count


    def get_year_count_dict(self, start, end):
        data = dict()
        for year in range(start, end + 1):
            if self.sleep:
                sleep(5)
            data[year] = self.get_result_count(year)
        return data


class UrlGenerator(CrawlCount):
    def __init__(self, query='hello world', startyear=1900, endyear=1900):
        CrawlCount.__init__(self, query, startyear, endyear)
        self.query = urllib.parse.quote(query, safe='+')
        self.startyear = str(self.startyear)
        self.endyear = str(self.endyear)

    #e.g. https://scholar.google.com/scholar?&q=hello+world&as_ylo=1900&as_yhi=1900&hl=en-us
    @property
    def scholar_url(self):
        url = 'https://scholar.google.com/scholar?&q=' + self.query \
                + '&as_ylo=' + self.startyear \
                + '&as_yhi=' + self.endyear \
                + '&hl=en-us'
        return url
