################## FLIGHTCLUB SCRAWLER ######################

## IMPORTS ##

import os
import requests
from lxml import html
import csv
import sys
import json
import urllib.request

################################# CLASSES ##################################################################

class ShoeObj:
    def __init__(self, name, lprice, URL, imgURL):
        self.name = name.replace('"', '*')
        self.lprice = lprice
        self.URL = URL
        self.imgURL = imgURL
        self.sizes = [0]

        # insert code to get sizes and price differences from URL
        page = requests.get(URL)
        tree = html.fromstring(page.content)
        self.sizes = list((map (str.strip, tree.xpath('//*/option/text()')))) # sizes

    def namelist (self):
        print ('\"' +self.name +'\",') ##.replace('*', '')

    def shoelist (self):
        print ('"' ,self.name, '|', self.lprice ,'|' , self.URL ,'|' , self.sizes , '|' ,self.imgURL,'",')

#################################################################################################################



################################# VARS ##############################################################

urlHandles = ["http://www.flightclub.com/air-jordans?id=34&limit=90",
              "http://www.flightclub.com/nike?id=62&limit=90",
              "http://www.flightclub.com/footwear?id=17&limit=90"]



pageNumber = 1
pageMax = 1
url = ""

urls = []
shoeName_codeName = []
lowestprice = []
shoeURL = []
imgURL = []
allShoes = {}

try:
    os.remove('shoelist.txt')
except OSError:
    pass

try:
    os.remove('namelist.txt')
except OSError:
    pass


############################################ MAIN #####################################################################

## Next we will use requests.get to retrieve the web pages with our data, parse it using the html module and save the results to parsedhtmlTREE: ##
## parsedHtmlTree will contains the whole HTML file in a nice tree structure which we can go over with XPath and selector ##

for titles in urlHandles:
    pageNumber = 1

    while pageNumber <= pageMax:

        url = titles + "&p=" + str(pageNumber)

        if pageNumber == 1:

            # Partitions HTML looking for ' <div class="page-counter"> Page 2 of 3 </div>'
            # Finds max page from this partition
            request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'})
            rawHTML = str(urllib.request.urlopen(request).read())
            rawHTML = rawHTML.partition("class=\"page-counter\">")[2]
            rawHTML = rawHTML.partition("of ")[2]
            rawHTML = rawHTML.partition(" <")[0]
            pageMax = int(rawHTML)

        urls.append(url)
        print(url)

        pageNumber += 1

commonXpath = '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/'

for urlname in urls:

    print ("Currently Collectiing Shoe Information from" , urlname)

    #print ("Currently Collecting Shoes from:", urlname)
    page = requests.get(urlname)
    parsedhtmlTREE = html.fromstring(page.content)

    # This will create a list of buyer
    shoeName_codeName = (parsedhtmlTREE.xpath(commonXpath + 'p/a[@href]/text()'))

    # This will store the shoe exact url
    shoeURL = (parsedhtmlTREE.xpath(commonXpath + 'a/@href'))

    # This will create a list of prices
    lowestprice = (parsedhtmlTREE.xpath('//*[@id]/span[@class="price"]/text()'))

    #This will create a list of images
    imgURL =  (parsedhtmlTREE.xpath(commonXpath + 'a/img/@src'))

    for x in range (0,len(shoeName_codeName)):

        #print ('\nshoe:', x, 'processing')
        #print("Checking if" , shoeName_codeName[x].strip(), "is already stored")

        if shoeURL[x] in allShoes.keys():
            #print ("Key Exists ... continuing")
            continue

        else:
            try:
                #print ("Storing New Shoe", "NAME:", shoeName_codeName[x].strip(), "PRICE:", lowestprice[x])
                allShoes[shoeURL[x]] = (ShoeObj(shoeName_codeName[x].strip(), lowestprice[x], shoeURL[x], imgURL[x]))
            except IndexError:
                #print("OUT OF RANGE ITEM")
                pass

        #print ("Process", x, "Complete")

orig_stdout = sys.stdout

shoelist = open('shoelist.txt', 'a')
sys.stdout = shoelist
for key  in allShoes.keys(): 
    allShoes[key].shoelist()
shoelist.close()

namelist = open('namelist.txt', 'a')
sys.stdout = namelist
for key in allShoes.keys():
	allShoes[key].namelist()
namelist.close()

sys.stdout = orig_stdout








