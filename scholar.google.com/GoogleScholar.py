#!/usr/bin/env python3
from time import sleep
from bs4 import BeautifulSoup
import re
import requests
import urllib.parse


class Crawler:
    def __init__(self, query='hello world', num=10, start=0, sleep=True):
        self.query = '+'.join(query.split(' '))
        self.num = num
        self.start = start
        self.sleep = sleep
        self.headers = {'user-agent': 'Mozilla/5.0'}
        self.big_soup = BeautifulSoup("<html><body></body></html>", 'html.parser')

    def search_pages(self, pages=1):
        urls = []
        for page in range(0, pages):
            url = UrlGenerator(self.query, self.num, (self.start + (10*pages))).scholar_url
            urls.append(url)
        for url in urls:
            if self.sleep:
                sleep(1)
            html = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(html, 'html.parser')
            self.big_soup.body.append(soup.body)

        results = self.scrape_scholar_result(self.big_soup)

        data = dict()
        data['source'] = 'google scholar'
        data['expected_num'] = self.num * pages
        data['received_num'] = len(results)
        data['first_page_url'] = urls[0]
        data['results'] = results

        return data

    def search_page(self, page=0):
        url = UrlGenerator(self.query, self.num, (self.start + (10*page))).scholar_url
        response = requests.get(url, headers=self.headers)

        if(response.status_code != 200):
                print("error " + response.status_code)
                return null

        soup = BeautifulSoup(response.text, 'html.parser')        
        results = self.scrape_scholar_result(soup.body) 

        data = dict()
        data['source'] = 'google scholar'
        data['expected_num'] = self.num
        data['received_num'] = len(results)
        data['page_url'] = url
        data['results'] = results

        return data

    @staticmethod
    def scrape_scholar_result(soup):
        containers = soup.find_all('div', class_='gs_ri')
        results = []

        for container in containers:
            try:
                link = container.find('a').get('href')
            except (AttributeError, TypeError):
                link = 'No link'
            # skip if invalid link
            if link[:4] != 'http':
                continue
            try:
                title = container.find('h3').a.text
            except AttributeError:
                title = container.find('h3').text.replace('[CITATION][C] ', '')
            try:
                excerpt = container.find('div', class_='gs_rs').text
            except AttributeError:
                excerpt = ''
            try:
                year = container.find('div', class_='gs_a').text
                year = re.sub(r'\D', '', year)
                if len(year) != 4:
                    year = 'NA'
            except AttributeError:
                year = 'NA'
            try:
                citations = container.find('div', class_='gs_fl').a.text.replace('Cited by ', '')
                if citations.isdigit() is False:
                    citations = 0
            except AttributeError:
                citations = 0

            links_data = {'link': link,
                          'title': title,
                          'excerpt': excerpt,
                          'year': year,
                          'citations': int(citations)
                          }
            results.append(links_data)

        return results


class UrlGenerator(Crawler):
    def __init__(self, query='hello world', num=10, start=0):
        Crawler.__init__(self, query, num, start)
        self.query = urllib.parse.quote(query, safe='+')
        self.num = str(self.num)
        self.start = str(self.start)

    #e.g. https://scholar.google.com/scholar?&q=hello+world&num=10&start=0
    @property
    def scholar_url(self):
        url = 'https://scholar.google.com/scholar?&q=' + self.query + '&num=' + self.num + '&start=' + self.start + '&hl=en-us'
        return url
