#Raw Scrape

import urllib2
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

def FacebookScrape(search, pageNumber):
        page = urllib2.urlopen("https://www.facebook.com/public?query=" + search + "&init=ffs&nomc=0&page=" + pageNumber)
        soup = BeautifulSoup(page, 'lxml')
        comments = soup.find_all(string=lambda text:isinstance(text,Comment))
        
	comment = comments[1];
    
        soup2 = BeautifulSoup(comment, 'lxml')

        linkTags = soup2.find_all('a')

        stringLinks=[]
        
        for link in linkTags:
            stringLinks.append(str(link))
        
        profileLinks=[]
        
        for link in stringLinks:
            if "data-testid" in link:
                profileLinks.append(link)
                
        trueLinks = [];
        
        
        for link in profileLinks:
            soup3 = BeautifulSoup(link, 'lxml')
            trueLinks.append(soup3.find('a').get('href'))    
	
	print("Writing to file")
	        
        f = open('result' + pageNumber + '.txt', 'w')
        f.write("Name   Link \n")
     
        for link in trueLinks:
            profileScrape(link, f)
            
        f.close()

            
            
def profileScrape(link, f):
	print("Starting scrape for " + link)
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page, 'lxml')

	name = soup.find('a', class_='_2nlw').text
	f.write((name + " " + link + "\n").encode("UTF-8"))
