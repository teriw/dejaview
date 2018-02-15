import allhomes


def scrapetheworld(address):
    data = allhomes.scrapeAddress(address)
    return data;
