from facebookRawScrape import FacebookScrape, profileScrape

print("Starting FacebookScrape")


for x in range(1, 6):
    print("Scrape # " + str(x))
    FacebookScrape("jonathan", str(x))
