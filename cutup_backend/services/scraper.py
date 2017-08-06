from bs4 import BeautifulSoup
import urllib

class Scraper(object):
    def bbcScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all('h3')
        for title in titles:
            collection.append(title.get_text())
        joined_collection = ' '.join(collection)
        return joined_collection

    def nytScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all('h2', 'headline')
        for title in titles:
            collection.append(title.get_text())
        joined_collection = ' '.join(collection)
        return joined_collection

    def aljScrape(self, url):
        collection = []
        site_text = urllib.urlopen(url).read()
        soup = BeautifulSoup(site_text, 'html.parser')
        titles = soup.find_all(['h1', 'h2', 'h3', 'h4'])
        for title in titles:
            collection.append(title.get_text())
        joined_collection = ' '.join(collection)
        return joined_collection

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
        elif string == "fnews":
            url = 'http://www.foxnews.com/'
        elif string == "cnn":
            url = 'http://www.cnn.com/'
