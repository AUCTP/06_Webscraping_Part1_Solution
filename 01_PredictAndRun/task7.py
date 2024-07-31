import requests
import bs4

tickers = ['UBER', 'AAPL', 'NVDA', 'AMD', 'MBG.DE']

userAgent = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

for ticker in tickers:
    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'
    r = requests.get(url, headers=userAgent)
    if r.status_code == 200:
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')
        search = {'data-field': 'regularMarketPrice'}
        price = htmlDocument.find('fin-streamer', search).get_text()
        print(f'{ticker}: {price}')
    else:
        print(f'{ticker}: failed (Status Code: {r.status_code})')
