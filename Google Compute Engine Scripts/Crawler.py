import urllib.request

# Start urls for the crawler
urls = ["http://www.flightclub.com/new-arrivals?id=14&amp&limit=90",
        "http://www.flightclub.com/air-jordans?id=34&limit=90",
        "http://www.flightclub.com/nike?id=62&limit=90",
        "http://www.flightclub.com/footwear?id=17&limit=90"]

urlText = []

i = 1
key = 1
href = False
url = ""

# Runs through each start url
for titles in urls:

    while True:
        url = titles + "&p=" + str(i)
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        # Gets the raw html from the website
        print(url)
        urljunk = str(urllib.request.urlopen(request).read())

        # For file naming, it deletes the url and leaves the additional bit at the end
        handle = titles.replace("http://www.flightclub.com/", "")
        title = handle.partition("?")[0]

        # This writes a file at "C:/Users/[insert user here]/Desktop/Htmls/" Feel free to write anywhere
        # The extra bit at the end is for naming files by the page they were found on and the page number they were found on
        # i.e. air_jordans_2 is the second page of jordans
        file = open("C:/Users/Brian/Desktop/Htmls/" + title + "_" + str(i), 'w')
        file.write(urljunk)

        # Looks for next page button, if it doesn't exist, it means you're at the end and you move onto the next page
        if urljunk.partition("title=\"Next\"")[2] == "":
            i = 1
            href = False
            break
        i += 1
