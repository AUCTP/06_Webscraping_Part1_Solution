import requests
import bs4

url = 'https://finance.yahoo.com/quote/UBER?p=UBER&.tsrc=fin-srch'

userAgent = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

r = requests.get(url, headers=userAgent)
htmlText = r.text
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')

paragraphs = htmlDocument.find_all('fin-streamer')

for p in paragraphs:
    text = p.get_text()
    print(text)
