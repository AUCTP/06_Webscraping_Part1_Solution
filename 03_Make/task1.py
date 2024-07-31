import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

def get_data(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}' # Define the URL for the given ticker
    r = requests.get(url, headers=userAgent) # Send a get request including the ticker
    if r.status_code == 200: # Check if status code is 200 (everything went well)
        htmlText = r.text # Extract the raw HTML 
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw HTML to Python
        searchPrice = {'data-field': 'regularMarketPrice'} # Define a search for the current price
        searchClose = {'data-field': 'regularMarketPreviousClose'} # Define a search for the closing price
        searchOpen = {'data-field': 'regularMarketOpen'} # Define a search for the opening price
        searchMarketCap = {'data-field': 'marketCap'} # Define a search for the market cap
        searchPE = {'data-field': 'trailingPE'} # Define a search for the PE-Ratio
        price = htmlDocument.find('fin-streamer', searchPrice).get_text() # find the first fin-streamer element matching the search and extract the raw text
        close = htmlDocument.find('fin-streamer', searchClose).get_text() # find the first fin-streamer element matching the search and extract the raw text
        open = htmlDocument.find('fin-streamer', searchOpen).get_text() # find the first fin-streamer element matching the search and extract the raw text
        marketCap = htmlDocument.find('fin-streamer', searchMarketCap).get_text() # find the first fin-streamer element matching the search and extract the raw text
        pe = htmlDocument.find('fin-streamer', searchPE).get_text() # find the first fin-streamer element matching the search and extract the raw text
        print(f'{ticker}:\nPrice: {price}\nClose: {close}\nOpen: {open}\nMarket Cap: {marketCap}\nPE-Ratio: {pe}') # Print the ticker and the price
    else:
        print(f'{ticker}: failed (Status Code: {r.status_code})') # Inform the user that something went wrong

def get_choice(tickers):
    for i in range(len(tickers)):
        print(f'{i}: {tickers[i]}')
    print(f'{i+1}: Custom ticker')
    print(f'{i+2}: Shutdown')
    choice = int(input('>'))
    if choice == i + 1:
        ticker = input('Enter custom ticker: ')
    elif choice == i + 2:
        ticker = 'stop'
    else:
        ticker = tickers[choice]
    return ticker
        

userAgent = { # Define the user agent telling the Website we are using Google Chrome to avoid getting blocked
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

tickers = ['UBER', 'AAPL', 'NVDA', 'AMD', 'MBG.DE'] # Define a list of stock tickers

while True:
    ticker = get_choice(tickers)
    if ticker == 'stop':
        break
    else:
        get_data(ticker)