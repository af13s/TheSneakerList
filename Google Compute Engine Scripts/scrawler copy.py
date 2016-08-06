################## FLIGHTCLUB SCRAWLER ######################

## IMPORTS ##

import os
import requests
from lxml import html
import csv
import sys
import json
import urllib.request

def htmlTree:
    def __init__(self, URL):
        page = requests.get(URL)
        tree = html.fromstring(page.content)
        return tree

################################# CLASSES ##################################################################

class ShoeObj:
    def __init__(self, name, lprice, URL, imgURL):
        self.name = name.replace('"', '*')
        self.lprice = lprice
        self.URL = URL
        self.imgURL = imgURL
        self.sizes = [0]

        # code to get sizes and price differences from URL
        tree = htmlTree(URL)
        self.sizes = list((map (str.strip, tree.xpath('//*/option/text()')))) # sizes

    def namelist (self):
        print ('\"' +self.name +'\",') ##.replace('*', '') #Print out shoelist names

    def shoelist (self):
        print ('"' ,self.name, '|', self.lprice ,'|' , self.URL ,'|' , self.sizes , '|' ,self.imgURL,'",') #Print out full shoe information


class RetailerObj:
        def __init__(self, xpathvars, seedurls, pgincr, nextpgxpath, nxtval, urlflags=''):
            self.xpaths = xpathvars     # name,url,price,image
            self.seeds = seedurls       # Www.example.com
            self.pgr = pgincr           # 'p' or 'page'
            self.nxpath = nextpgxpath   # path to page next
            self.nxval = nxtval
            self.urlflags = urlflags           # if exists, html flags to max displays



##################################################### RETAILER CONSTANTS ######################################################

global allShoes = {}

## Flight club
    fxpaths = ['//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/p/a[@href]/text()',
                '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/a/@href',
                '//*[@id]/span[@class="price"]/text()',
                '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/a/img/@src']
                
    flseedurls = ["http://www.flightclub.com/air-jordans?id=34&limit=90",
                    "http://www.flightclub.com/nike?id=62&limit=90",
                    "http://www.flightclub.com/footwear?id=17&limit=90"]

    flpginc = 'p'

    flnxpgpath = '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/div[2]/div/div[3]/a[2]/text()'

    flnxval = 'Next'

    flflags = 'limit=90'

## Stadium Goods
    stpaths = ['//name',
                '//url',
                '//price',
                '//imgurl']
                
    stseedurls = ['http://www.stadiumgoods.com/air-jordan',
                    'http://www.stadiumgoods.com/nike',
                    'http://www.stadiumgoods.com/adidas',
                    'http://www.stadiumgoods.com/footwear']

    stpginc = 'p'

    stnxpgpath = '//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/a[2]/text()'

    stnxval = 'Next'



#################################### FUNCTIONS ##################################################################

def Scraper (tree, xpaths):

    # This will create a list of buyer
    shoeName_codeName = (tree.xpath(xpaths[0]))

    # This will store the shoe exact url
    shoeURL = (tree.xpath(xpaths[1]))

    # This will create a list of prices
    lowestprice = (tree.xpath(xpaths[2]))

    #This will create a list of images
    imgURL =  (tree.xpath(xpaths[3]))

    for x in range (0,len(shoeName_codeName)):
        if shoeURL[x] in allShoes.keys():
            continue
        else:
            try:
                print ("Storing New Shoe", "NAME:", shoeName_codeName[x].strip(), "PRICE:", lowestprice[x])
                allShoes[shoeURL[x]] = (ShoeObj(shoeName_codeName[x].strip(), lowestprice[x], shoeURL[x], imgURL[x]))
            except IndexError:
                print("OUT OF RANGE ITEM")

def Crawler ( Robj ):

    allShoes =  {}
    shoe = None

    for seed in Robj.seeds:

        pnum=1

        while( True ):

            url = seed + '?' + Robj.pgr +  '=' + str(pnum) + '&' Robj.urlflags

            print ("Currently Collectiing Shoe Information from" , url)
            tree = htmlTree (url)
            Scraper(tree, Robj.xpaths)

            if (tree.xpath(Robj.nxpath) != Robj.nxval ): #Very Important IF STATEMENT
                break

            pnum += 1

    return allShoes

if __name__ == "__main__":

Retailers = []
Retailers.append(RetailerObj(fxpaths, flseedurls, flpginc, flnxpgpath, flnxval, flflags))

for retailer in Retailers:

    Crawler (retailer)

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


















