#!/usr/bin/env python
from time import sleep
from bs4 import BeautifulSoup
import requests
import urllib.parse
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException

class CrawlCount:
    def __init__(self, query='hello world', startyear=1900, endyear=1900, sleeptime=1 ,sleep=True):
        self.query = '+'.join(query.split(' '))
        self.startyear = startyear
        self.endyear = endyear
        self.sleep = sleep
        self.sleeptime = sleeptime
        self.headers = {'user-agent': 'Mozilla/5.0'}
        self.result_count_dict = dict()

    def crawl_result_count(self, startyear, endyear, driver='firefox', incognito=False, browser_bin_path=None):
        year = startyear
        try:
            while year <= endyear:
                url = UrlGenerator(self.query, year, year).scholar_url
                # trying with requests
                response = requests.get(url, headers=self.headers)
                # stop using requests when blocked by google (http response 503)
                if response.status_code != 200:
                    break
                soup = BeautifulSoup(response.text, 'html.parser')
                result_count = int(soup.find(id="gs_ab_md").div.get_text().split(' ')[1].replace(',', ''))
                print(str(year) + ': ' + str(result_count))
                self.result_count_dict[year] = result_count
                if (sleep):
                    sleep(self.sleeptime)
                year += 1

            # falling back to selenium when blocked by google while crawling is unfinished
            if year <= endyear:
                self.crawl_result_count_selenium(year, endyear, driver=driver, incognito=incognito, browser_bin_path=browser_bin_path)

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Unexpected error:", sys.exc_info())
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            return

    def crawl_result_count_selenium(self, startyear, endyear, driver='firefox', incognito=False, browser_bin_path=None):
        try:
            # setup browser driver for selenium
            if driver == 'firefox':
                firefox_profile = webdriver.FirefoxProfile()
                if incognito:
                    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
                if browser_bin_path != None:
                    firefox_binary = FirefoxBinary(browser_bin_path)
                    driver = webdriver.Firefox(firefox_binary=firefox_binary, firefox_profile=firefox_profile)
                else:
                    driver = webdriver.Firefox(firefox_profile=firefox_profile)
            elif driver == 'chrome':
                chrome_options = webdriver.ChromeOptions()
                if incognito:
                    chrome_options.add_argument('--incognito')
                if browser_bin_path != None:
                    chrome_options._binary_location = browser_bin_path
                driver = webdriver.Chrome(chrome_options=chrome_options)

            for year in range(startyear, endyear + 1):
                url = UrlGenerator(self.query, year, year).scholar_url
                driver.get(url)

                try:
                    result_string_list = driver.find_element_by_id("gs_ab_md").text.split(' ')
                    print(result_string_list)
                    if result_string_list[0] == 'About':
                        result_count = int(result_string_list[1].replace(',', ''))
                    else:
                        result_count = int(result_string_list[0])

                    print(str(year) + ': ' + str(result_count))
                    self.result_count_dict[year] = result_count
                    if (sleep):
                        sleep(self.sleeptime)
                # if blocked_by_google:
                except NoSuchElementException:
                    # finding captcha and click to start solving image captcha
                    checkbox_element = driver.find_element_by_id("recaptcha")
                    checkbox_element.click()
                    # finding checkbox and continiously validate if checked
                    driver.switch_to_frame(driver.find_element_by_tag_name('iframe'))
                    recaptcha_anchor = driver.find_element_by_id("recaptcha-anchor")
                    print("found anchor")
                    print("aria-checked:" + recaptcha_anchor.get_attribute("aria-checked"))
                    while (recaptcha_anchor.get_attribute("aria-checked") == 'false'):
                        sleep(3)
                    # captcha is solved
                    print("aria-checked:" + recaptcha_anchor.get_attribute("aria-checked"))
                    driver.switch_to_default_content()
                    submit_button = driver.find_element_by_xpath("//input[@name='submit']")
                    submit_button.click()

                    result_string_list = driver.find_element_by_id("gs_ab_md").text.split(' ')
                    if result_string_list[0] == 'About':
                        result_count = int(result_string_list[1].replace(',', ''))
                    else:
                        result_count = int(result_string_list[0])
                    print(str(year) + ': ' + str(result_count))
                    self.result_count_dict[year] = result_count
                    if (sleep):
                        sleep(self.sleeptime)
            driver.quit()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Unexpected error:", exc_type)
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            try:
                driver.quit()
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                print("Unexpected error:", exc_type)
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)


    def get_result_count(self, year):
        return self.result_count_dict[str(year)]

    def get_result_count_range_sum(self, customstartyear, customendyear):
        sum = 0
        for year in range(customstartyear, customendyear + 1):
            sum += self.result_count_dict[str(year)]
        return sum


    def get_year_count_dict(self, start, end):
        return self.result_count_dict


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
