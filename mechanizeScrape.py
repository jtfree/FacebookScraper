#Mechanize Scrape


import mechanize

br = mechanize.Browser()
def scrape(search):
	result = br.open("http://www.facebook.com/public?query=" + search + "&init=ffs&nomc=0")
	f = open('result.txt', 'w')
        f.write(result)
        f.close()
