import allhomes
import googlesearch

def scrapetheworld(address, addressId):
    #get the url for allhomes from a google search rather than using the allhomes search
    addressurl = googlesearch.allHomesSalesUrl(address)
    if addressurl is not None:
        data = allhomes.scrapeAddress(addressurl, addressId)
    else:
        data = "Address was unable to be found on allhomes"
    return data
