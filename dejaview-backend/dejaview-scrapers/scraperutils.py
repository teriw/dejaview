import urllib.request
import os

def downloadImage(addressId, fileurl, filename):
    myPath = os.path.join(
        "C:" + os.sep + "3.Development" + os.sep + "Python" + os.sep + "dejaview" + os.sep + "images" + os.sep + str(addressId))
    fullfilename = os.path.join(myPath, filename)
    urllib.request.urlretrieve(fileurl, fullfilename)