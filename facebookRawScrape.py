#Raw Scrape

import urllib2
import requests
from bs4 import BeautifulSoup

def testFacebookScrape(search):
	#r = requests.get("https://www.facebook.com/public?query=" + search + "&init=ffs&nomc=0")
	page = urllib2.urlopen("https://www.facebook.com/public?query=" + search + "&init=ffs&nomc=0")
	soup = BeautifulSoup(page, 'lxml')
	print(soup.prettify())

testFacebookScrape("jonathan")	