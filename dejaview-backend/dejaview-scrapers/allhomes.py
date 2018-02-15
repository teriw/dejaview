from bs4 import BeautifulSoup
import requests
import re
import scraperutils


def scrapeAddress(address):
    r = requests.get("https://www.allhomes.com.au/ah/act/sale-residential/20-haines-street-curtin-canberra/1317491147911")
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    addressId = 1001
    images = ""
    #title = soup.title.string
    for script in soup.findAll("script"):
        if script.find("srcHighDef") != -1:
            quotes = re.findall('"([^"]*)"', script.text)
            counter = 0
            for quotetext in quotes:
                if quotetext.find("_hd.jpg") != -1:
                    images = images + quotetext
                    counter = counter+1
                    filename = "image" + str(counter) + ".jpg"
                    scraperutils.downloadImage(addressId, quotetext, filename)

    return str(counter) + "images returned at: " + images
