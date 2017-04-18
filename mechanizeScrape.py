#Mechanize Scrape


import mechanize

def scrape(search):
	url = "http://www.facebook.com/public?query=" + search + "&init=ffs&nomc=0"; 
	print(url)
	result = mechanize.urlopen(url)
	f = open('result.txt', 'w')
        f.write(result.read())
        f.close()
scrape("Jonathan")
