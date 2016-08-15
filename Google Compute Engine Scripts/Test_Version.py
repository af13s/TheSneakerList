################## FLIGHTCLUB SCRAWLER ######################

## IMPORTS ##

import os
import requests
from lxml import html
import sys
import urllib.request
from multiprocessing import Process

allShoes = {}

def htmlTree( URL ):
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
        #tree = htmlTree(URL)
        #self.sizes = list((map (str.strip, tree.xpath()))) # sizes

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

#################################### FUNCTIONS ##################################################################

def printnamelist():
    shoelist = open('shoelist.txt', 'a')
    sys.stdout = shoelist
    for key in allShoes.keys():
        allShoes[key].shoelist()
    shoelist.close()

def printshoelist():
    namelist = open('namelist.txt', 'a')
    sys.stdout = namelist
    for key in allShoes.keys():
        allShoes[key].namelist()
    namelist.close()

def Scraper (tree, xpaths):

    # This will extract a list of shoe names on page
    shoeName_codeName = (tree.xpath(xpaths[0]))

    # This will extract list of exact urls
    shoeURL = (tree.xpath(xpaths[1]))

    # This will extract a list of shoe prices
    lowestprice = (tree.xpath(xpaths[2]))

    #This will extract a list of images
    imgURL =  (tree.xpath(xpaths[3]))

    for x in range (0,len(shoeName_codeName)): #iterate through all shoe listings on page
        if shoeURL[x] in allShoes.keys(): #if value is not unique to keys exclude
            continue
        else:
            try:
                print ("Storing New Shoe", "NAME:", shoeName_codeName[x].strip(), "PRICE:", lowestprice[x])
                allShoes[shoeURL[x]] = (ShoeObj(shoeName_codeName[x].strip(), lowestprice[x], shoeURL[x], imgURL[x]))
                #
                orig_stdout = sys.stdout
                ##
                shoelist = open('shoelist.txt', 'a')
                sys.stdout = shoelist
                allShoes[shoeURL[x]].shoelist()
                ##
                namelist = open('namelist.txt', 'a')
                sys.stdout = namelist
                allShoes[shoeURL[x]].namelist()
                #
                sys.stdout = orig_stdout

            except IndexError:
                print("OUT OF RANGE ITEM")

def Crawler ( Robj ):

    for seed in Robj.seeds: #seed urls declared in retailer class

        pnum=1

        while( True ): #will continute until the break function inside the function is triggered

            url = seed + '?' + Robj.pgr +  '=' + str(pnum) + '&' + Robj.urlflags
            print ("Scraping Site: " , url)

            tree = htmlTree (url)
            Scraper(tree, Robj.xpaths) #scrapes each page on the fly

            #print ('Does:' , tree.xpath(Robj.nxpath)[0].strip() ,'equal' , Robj.nxval) #// used for testing nxval validity

            # this searches the html page for the "next" element which varies page to page, var specific to page stored in Robj.nxval
            if (pnum == 1):
                if (tree.xpath(Robj.nxpath)[0].strip() != Robj.nxval ): #Very Important IF STATEMENT if its the first page there is no prev so next text in first position
                    break
            else:
                try:
                    if (tree.xpath(Robj.nxpath)[1].strip() != Robj.nxval ): # Every other page should have a nxval in the second position, after previous val second position
                        break
                except IndexError: # On last page there is a previous button but no next button so this is the last page
                    break
            pnum += 1




if __name__ == "__main__":

    try:
        os.remove('shoelist.txt')
    except OSError:
        pass

    try:
        os.remove('namelist.txt')
    except OSError:
        pass

##################################################### RETAILER CONSTANTS ######################################################

#This may be exported into a constants.py file in the future

#Reference for all following websites can be found on this url
# http://www.complex.com/sneakers/2016/03/best-sneaker-reseller-sites/
# Goal of this script is to make it so that all 10 websites work properly and fully with the crawler and scraper.


## Flight club
    fxpaths = ['//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/p/a[@href]/text()',
               '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/a/@href',
               '//*[@id]/span[@class="price"]/text()',
               '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/a/img/@src'
               '//*/option/text()']


    flseedurls = ["http://www.flightclub.com/air-jordans",
                  "http://www.flightclub.com/nike",
                  "http://www.flightclub.com/footwear"]

    flpginc = 'p'

    flnxpgpath = '//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/div[2]/div/div[3]/a/text()'

    flnxval = 'Next'

    flflags = 'limit=90'

## Stadium Goods
    stpaths = ['//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/ul/li/div/div[1]/a/text()',
               '//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/ul/li/div/div[1]/a/@href',
               '//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/ul/li/div/div[2]/span/span[@class]/text()',
               '//*[@id]/img/@src']

    stseedurls = ['http://www.stadiumgoods.com/air-jordan',
                  'http://www.stadiumgoods.com/nike',
                  'http://www.stadiumgoods.com/adidas',
                  'http://www.stadiumgoods.com/footwear']

    stpginc = 'p'

    stnxpgpath = '//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/a/text()'

    stnxval = 'Next'

## Rif LA
    rlpaths = ['//*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/div/div[1]/a/text()',
               '//*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/div/div[1]/a/@href',
               '//*[@id="main"]/div[1]/table/tbody/tr[1]/td[3]/div/text()',
               '//*[@id]/img/@src']

    rlseedurls = ["http://www.rif.la/search_item.php"]

    rlpginc = 'page'

    rlnxpgpath = '//*[@id="main"]/div[1]/div[2]/a[10]/text()'

    rlnxval = 'NEXT'

    ## TO BE FILLED

    ## Sole Supremecy
    sopaths = ['names',
               'url',
               'price',
               'image']

    soseedurls = ['http://www.solesupremacy.com/collections/all']

    sopginc = 'page'

    sonxpgpath = '//*[@id="products"]/main/div/div[2]/div/div/div/ul/li[8]/a/@title'

    sonxval = 'Next'

    ## Project Blitz
    pbpaths = ['names',
               'url',
               'price',
               'image']

    pbseedurls = []

    pbpginc = 'page'

    pbnxpgpath = ''

    pbnxval = 'Next'

    ## Souled Out NYC
    sonpaths = ['names',
               'url',
               'price',
               'image']

    sonseedurls = []

    sonpginc = 'page'

    sonnxpgpath = ''

    sonnxval = 'Next'

    ## Index
    idxpaths = ['names',
               'url',
               'price',
               'image']

    idxseedurls = []

    idxpginc = 'page'

    idxnxpgpath = ''

    idxnxval = 'Next'

    ## Corgieshoe
    cspaths = ['names',
               'url',
               'price',
               'image']

    csseedurls = []

    cspginc = 'page'

    csnxpgpath = ''

    csnxval = 'Next'

    ## 23Penny
    p23paths = ['names',
               'url',
               'price',
               'image']

    p23seedurls = []

    p23pginc = 'page'

    p23nxpgpath = ''

    p23nxval = 'Next'

    ## The Collection Miami
    cmpaths = ['names',
               'url',
               'price',
               'image']

    cmseedurls = []

    cmpginc = 'page'

    cmnxpgpath = ''

    cmnxval = 'Next'

    ## Benjamin Kickz
    bkpaths = ['names',
               'url',
               'price',
               'image']

    bkseedurls = []

    bkpginc = 'page'

    bknxpgpath = ''

    bknxval = 'Next'

    ## The Holy Grail
    hgpaths = ['names',
               'url',
               'price',
               'image']

    hgseedurls = []

    hgpginc = 'page'

    hgnxpgpath = ''

    hgnxval = 'Next'

    ## weird sites kixclusive - project blitz

########################################################################################################################################

    Retailers = [] #this will contain all retailer objects
    Retailers.append(RetailerObj(stpaths, stseedurls, stpginc, stnxpgpath, stnxval)) #these are the variables declared above for stadium goods
    Retailers.append(RetailerObj(fxpaths, flseedurls, flpginc, flnxpgpath, flnxval, flflags)) #these are the variables declared above for flight club

    Process_1 = Process(target=Crawler , args=(Retailers[0],)) #syntax for making the crawler function call on object 1 to be made into a process
    Process_2 = Process(target=Crawler , args=(Retailers[1],))

    #this runs the processes simultaneously, main speed problem is waiting for the http request
    Process_1.start()
    Process_2.start()


    #This forces the compiler to wait for the processes 1 and 2 to finish before it continues to the print functions
    Process_1.join()
    Process_2.join()

    #Getting printing to function properly with the multiprocessing has been a hassle, this script may need some debugging for this to function properly
    printshoelist()
    printnamelist()
