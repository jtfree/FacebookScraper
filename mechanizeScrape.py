#Mechanize Scrape


import mechanize
from bs4 import BeautifulSoup

def scrape(search):
	url = "http://www.facebook.com/public?query=" + search + "&init=ffs&nomc=0"; 
	print(url)

	result = mechanize.urlopen(url)
	soup = BeautifulSoup(result, 'lxml')
	links = soup.find_all("div", class_= "hidden_elem");
	
	print(links)
	
	soup2 = BeautifulSoup(links, 'lxml');
	f = open('result.txt', 'w')
        f.write(soup2.prettify().encode("UTF-8"))
        f.close()
	print("File has been written at result.txt.")


scrape("Jonathan")
