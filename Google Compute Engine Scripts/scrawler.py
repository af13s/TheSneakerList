################## FLIGHTCLUB SCRAWLER ######################

## IMPORTS ##

from lxml import html
import urllib.request
import requests
from multiprocessing import Process
from gcloud import datastore
import Constants

allShoes = {}


########################################## FUNCTIONS ####################################################################

# parse html request and get get tree structure for xpath searching
def htmlTree( URL ):
        page = requests.get(URL)
        tree = html.fromstring(page.content)
        return tree

# Scrape Given URL to extract fields
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

#Iteratively search through given list of html shoe directories *seed urls* and pass url to scraper
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
################################# CLASSES ##################################################################

class ShoeObj:
    def __init__(self, name, lprice, URL, imgURL):
        self.name = name.replace('"', '*')
        self.lprice = lprice
        self.URL = URL
        self.imgURL = imgURL
        self.sizes = [0]

    #def namelist (self):
        #print ('\"' +self.name +'\",') ##.replace('*', '') #Print out shoelist names

    #def shoelist (self):
    #    print ('"' ,self.name, '|', self.lprice ,'|' , self.URL ,'|' , self.sizes , '|' ,self.imgURL,'",') #Print out full shoe information


class RetailerObj:
        def __init__(self, xpathvars, seedurls, pgincr, nextpgxpath, nxtval, urlflags=''):
            self.xpaths = xpathvars     # name,url,price,image
            self.seeds = seedurls       # Www.example.com
            self.pgr = pgincr           # 'p' or 'page'
            self.nxpath = nextpgxpath   # path to page next
            self.nxval = nxtval
            self.urlflags = urlflags           # if exists, html flags to max displays

#################################### FUNCTIONS ##################################################################
if __name__ == "__main__":

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
