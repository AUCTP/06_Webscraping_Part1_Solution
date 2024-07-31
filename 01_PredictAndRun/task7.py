import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

tickers = ['UBER', 'AAPL', 'NVDA', 'AMD', 'MBG.DE'] # Define a list of stock tickers

userAgent = { # Define the user agent telling the Website we are using Google Chrome to avoid getting blocked
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

for ticker in tickers: # Iterate over the tickers
    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}' # Define the URL for the given ticker
    r = requests.get(url, headers=userAgent) # Send a get request including the ticker
    if r.status_code == 200: # Check if status code is 200 (everything went well)
        htmlText = r.text # Extract the raw HTML 
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw HTML to Python
        search = {'data-field': 'regularMarketPrice'} # Define a search for the current price
        price = htmlDocument.find('fin-streamer', search).get_text() # find the first fin-streamer element matching the search and extract the raw text
        print(f'{ticker}: {price}') # Print the ticker and the price
    else:
        print(f'{ticker}: failed (Status Code: {r.status_code})') # Inform the user that something went wrong
