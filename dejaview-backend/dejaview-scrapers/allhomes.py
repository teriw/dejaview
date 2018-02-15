from bs4 import BeautifulSoup
import requests
import re


def printLinks(address):
    r = requests.get("https://www.allhomes.com.au/ah/act/sale-residential/20-haines-street-curtin-canberra/1317491147911")

    data = r.text
    links = address

    soup = BeautifulSoup(data, "html.parser")

    for link in soup.findAll('script'):
        #print(link.get("href"))
        #images = re.findall('"([^"]*)"', link)
        #for image in images:
            #image = image + image.text
        links = links+link.text
    return links
