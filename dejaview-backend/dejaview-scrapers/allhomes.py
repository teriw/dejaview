from bs4 import BeautifulSoup
import requests
import re
import scraperutils


def scrapeAddress(addressurl, addressId):
    r = requests.get(addressurl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    images = ""
    counter = 0
    #title = soup.title.string
    for script in soup.findAll("script"):
        if script.find("srcHighDef") != -1:
            quotes = re.findall('"([^"]*)"', script.text)
            for quotetext in quotes:
                if quotetext.find("_hd.jpg") != -1:
                    images = images + quotetext
                    counter = counter+1
                    filename = "image" + str(counter) + ".jpg"
                    scraperutils.downloadImage(addressId, quotetext, filename)
                    #remove line below to get all images
                    break

    return str(counter) + " images returned at: " + addressurl
