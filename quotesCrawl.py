from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import json

quotesBaseUrl = "https://www.goodreads.com/quotes?page="
##https://www.goodreads.com/quotes?page=2 search over page needed


##headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

quoteMaster = []
authorMaster = []
data = {}
for i in range(1,5):
    req = Request(url=quotesBaseUrl + str(i))
    uClient = urlopen(req)
    page_html = uClient.read()
    uClient.close()
    quote_soup = soup(page_html, "html.parser")
    containers = quote_soup.findAll("div", {"class": "quoteText"})

    ##count = 0

    for container in containers:
        quotelist = container.text.split('\n')
        quoteDetail = quotelist[1][7:-1]
        quoteAuthor = quotelist[4][4:]
        quoteMaster.append(quoteDetail)
        authorMaster.append(quoteAuthor)

for i in range(len(quoteMaster)):
    data[str(i)] = {}
    data_en = data[str(i)]
    data_en["EN"] = {'author' : authorMaster[i], 'quote' : quoteMaster[i]}


#print(quoteMaster)
#print(authorMaster)
#print(json.dumps(data))
with open('quotedata.txt', 'w') as outfile:
    json.dump(data, outfile)
