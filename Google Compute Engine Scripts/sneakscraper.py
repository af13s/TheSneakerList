#Task 1: Iterate through Html files
#Task 2: Open & Parse Html files
#Task 3: Find particular elements (table listings) in html
#Task 4: Create output file with listing

import os
import requests
from lxml import html
import csv
import sys
import json

################################# CLASSES ##################################################################

class ShoeObj:

	def __init__ (self, name, lprice, URL, imgURL):
			self.name = name.replace('"', '*')
			self.lprice = lprice
			self.URL = URL
			self.imgURL = imgURL
			self.sizes = [0]

			#insert code to get sizes and price differences from URL
			page = requests.get(URL)
			tree = html.fromstring(page.content)
			self.sizes = (map (str.strip, tree.xpath('//*/option/text()')) ) #sizes
			

	def namelist (self):
		
		print '\"' +self.name.replace('*', '') +'\",'

	def shoelist (self):
		print '"' ,self.name, '|', self.lprice ,'|' , self.URL ,'|' , self.sizes , '|' ,self.imgURL,'",'
		

############################################ VARS #############################################################

urlname = 'http://www.flightclub.com/footwear/adidas/yeezy' #Insert URL NAME function call

shoeName_codeName = []
lowestprice = []
shoeURL = []
imgURL = []

allShoes = []


############################################ MAIN #####################################################################

## Next we will use requests.get to retrieve the web pages with our data, parse it using the html module and save the results to parsedhtmlTREE: ##
## parsedHtmlTree will contains the whole HTML file in a nice tree structure which we can go over with XPath and selector ##
page = requests.get(urlname)
parsedhtmlTREE = html.fromstring(page.content)

#This will create a list of shoes
shoeName_codeName = (parsedhtmlTREE.xpath('//*[@id]/div[3]/div[2]/div[2]/div[3]/ul/li/div/p/a[@href]/text()'))

#This will store the shoe exact url
shoeURL = (parsedhtmlTREE.xpath('//*[@id="entire-page-wrap"]/div[3]/div[2]/div[2]/div[3]/ul/li/div/a/@href'))

#This will create a list of prices
lowestprice =  (parsedhtmlTREE.xpath('//*[@id]/span[@class="price"]/text()'))

#This will create a list of images
imgURL =  (parsedhtmlTREE.xpath('//*[@id="entire-page-wrap"]/div[3]/div[2]/div[2]/div[3]/ul/li/div/a/img/@src'))

for x in range (0,len(shoeName_codeName)):
	allShoes.append(ShoeObj(shoeName_codeName[x].strip(), lowestprice[x], shoeURL[x], imgURL[x]))
	print 'shoe:', x, 'processing';


orig_stdout = sys.stdout

shoelist = open('shoelist.txt', 'w')
sys.stdout = shoelist
for x in allShoes: 
	x.shoelist()
shoelist.close()

namelist = open('namelist.txt', 'w')
sys.stdout = namelist
for x in allShoes:
	x.namelist()
namelist.close()


sys.stdout = orig_stdout
	

