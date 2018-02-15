import urllib.request
import os
import datetime


def downloadImage(addressId, fileurl, filename):
    myPath = os.path.join(
        "C:" + os.sep + "3.Development" + os.sep + "Python" + os.sep + "dejaview" + os.sep + "images")
    fullfilename = os.path.join(myPath, filename)
    urllib.request.urlretrieve(fileurl, fullfilename)


def generateFileName(addressId, filesource, counter):
    #currentdatetime = datetime.strftime("%Y %H %M %S")
    #print(currentdatetime)
    currentDateTime = 0000
    return str(addressId) + "_" + filesource + "_image_" + str(currentDateTime) + "_" + str(counter) + ".jpg"