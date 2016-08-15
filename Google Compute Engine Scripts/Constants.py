##################################################### RETAILER CONSTANTS ######################################################

#This may be exported into a constants.py file in the future

#Reference for all following websites can be found on this url
# http://www.complex.com/sneakers/2016/03/best-sneaker-reseller-sites/
# Goal of this script is to make it so that all 10 websites work properly and fully with the crawler and scraper.


## Flight club

#Seed urls
http://www.flightclub.com/air-jordans
http://www.flightclub.com/nike
http://www.flightclub.com/footwear

##Xpaths
//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/p/a[@href]/text()
//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/a/@href
//*[@id]/span[@class="price"]/text()
//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/ul/li/div/a/img/@src
//*/option/text()
//*[@id="entire-page-wrap"]/div[4]/div[2]/div[2]/div[3]/div[2]/div/div[3]/a/text()

=
#FLAGS
p,Next,limit=90



##Stadium Goods
//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/ul/li/div/div[1]/a/text(),
//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/ul/li/div/div[1]/a/@href,
//*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/ul/li/div/div[2]/span/span[@class]/text(),
//*[@id]/img/@src]

stseedurls=[http://www.stadiumgoods.com/air-jordan,
  http://www.stadiumgoods.com/nike,
  http://www.stadiumgoods.com/adidas,
  http://www.stadiumgoods.com/footwear]

stpginc= p

stnxpgpath= //*[@id="top"]/body/div[2]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/a/text()

stnxval= Next

##RifLA
rlpaths=[//*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/div/div[1]/a/text(),
  //*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/div/div[1]/a/@href,
  //*[@id="main"]/div[1]/table/tbody/tr[1]/td[3]/div/text(),
  //*[@id]/img/@src]

rlseedurls=["http://www.rif.la/search_item.php"]

rlpginc= page

rlnxpgpath= //*[@id="main"]/div[1]/div[2]/a[10]/text()

rlnxval= NEXT

##TO BE FILLED

## Sole Supremecy
sopaths = [ names ,
            url ,
            price ,
            image ]

soseedurls = [ http://www.solesupremacy.com/collections/all ]

sopginc =  page

sonxpgpath =  //*[@id="products"]/main/div/div[2]/div/div/div/ul/li[8]/a/@title

sonxval =  Next

## Project Blitz
pbpaths = [ names ,
            url ,
            price ,
            image ]

pbseedurls = []

pbpginc =  page

pbnxpgpath =

pbnxval =  Next

## Souled Out NYC
sonpaths = [ names ,
            url ,
            price ,
            image ]

sonseedurls = []

sonpginc =  page

sonnxpgpath =

sonnxval =  Next

## Index
idxpaths = [ names ,
            url ,
            price ,
            image ]

idxseedurls = []

idxpginc =  page

idxnxpgpath =

idxnxval =  Next

## Corgieshoe
cspaths = [ names ,
            url ,
            price ,
            image ]

csseedurls = []

cspginc =  page

csnxpgpath =

csnxval =  Next

## 23Penny
p23paths = [ names ,
            url ,
            price ,
            image ]

p23seedurls = []

p23pginc =  page

p23nxpgpath =

p23nxval =  Next

## The Collection Miami
cmpaths = [ names ,
            url ,
            price ,
            image ]

cmseedurls = []

cmpginc =  page

cmnxpgpath =

cmnxval =  Next

## Benjamin Kickz
bkpaths = [ names ,
            url ,
            price ,
            image ]

bkseedurls = []

bkpginc =  page

bknxpgpath =

bknxval =  Next

## The Holy Grail
hgpaths = [ names ,
            url ,
            price ,
            image ]

hgseedurls = []

hgpginc =  page

hgnxpgpath =

hgnxval =  Next

## weird sites kixclusive - project blitz
