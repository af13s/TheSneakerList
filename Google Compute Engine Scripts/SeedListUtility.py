import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import re

b = open('brands.txt', 'r')
brands=[]

for line in b:
    brands.append(line[:-1])
print (brands)

http = httplib2.Http()

f = open('SneakerUrlList.txt', 'r')
o = open('SeedListUnrefined.txt', 'w')

for line in f:
    print (line[:-1])
    try:
        status, response = http.request(line[:-1])
    except TimeoutError:
        print ('Blocked by' , line )
        pass

    for link in BeautifulSoup(response, 'lxml').find_all('a', href=True):
        o.write(link['href']+'\n')
    o.write('\n')

f.close()
o.close()

ur = open('SeedListUnrefined.txt', 'r')
r = open('SeedListRefined.txt', 'w')

for line in ur:
    for brand in brands:
        print ('Checking: ' , brand , 'in', line)
        if brand in line:
                r.write(line)
    if '\n' == line:
        r.write('\n')

y = open('SeedListRefined.txt', 'r')
you = open('SeedListreReRefined.txt', 'w')

bcount =0
dcount=0

alllinks = {}

for line in y:
    if line == '\n': you.write('\n')
    for char in line:
        if '/' == char:
            bcount= bcount + 1
        elif '-' == char:
            dcount = dcount + 1
    if bcount <= 3:
        if line[:-1] in alllinks.keys():
            continue
        else:
            you.write(line)
            alllinks[line[:-1]] = True
    bcount =0
