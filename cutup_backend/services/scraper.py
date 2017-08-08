from bs4 import BeautifulSoup
import urllib
import re

class Scraper(object):
    def bbcScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all('h3')
        for title in titles:
            title_text = title.get_text().lower()
            clean_title = re.sub(r'[\t\n]', '', title_text)
            collection.append(clean_title)
        return collection

    def nytScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all('h2', 'headline')
        for title in titles:
            title_text = title.get_text().lower()
            clean_title = re.sub(r'[\t\n]', '', title_text)
            spaced_title = re.sub(r'\s+', ' ', clean_title)
            collection.append(spaced_title)
        return collection

    def aljScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all(['h1', 'h2', 'h3', 'h4'])
        for title in titles:
            title_text = title.get_text().lower()
            clean_title = re.sub(r'[\t\n]', '', title_text)
            collection.append(clean_title)
        return collection

    def foxScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all(['h3', 'h4'])
        for title in titles:
            title_text = title.get_text().lower()
            clean_title = re.sub(r'[\t\n]', '', title_text)
            collection.append(clean_title)
        return collection

    def cnnScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html5lib')
        titles = soup.find_all('h3')
        print(titles)
        for title in titles:
            title_text = title.get_text().lower()
            clean_title = re.sub(r'[\t\n]', '', title_text)
            collection.append(clean_title)
        return collection

    def scrape(self, string):
        if string == "bbc":
            url = 'http://www.bbc.com/news'
            return self.bbcScrape(url)
        elif string == "nyt":
            url = 'https://www.nytimes.com/section/world'
            return self.nytScrape(url)
        elif string == "alj":
            url = 'http://www.aljazeera.com/'
            return self.aljScrape(url)
        elif string == "fox":
            url = 'http://www.foxnews.com/'
            return self.foxScrape(url)
        elif string == "cnn":
            url = 'http://www.cnn.com/world'
            return self.cnnScrape(url)
