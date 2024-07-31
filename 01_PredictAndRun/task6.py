import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

url = 'https://finance.yahoo.com/quote/UBER?p=UBER&.tsrc=fin-srch' # Define URL to scrape

userAgent = { # Define the user agent telling the Website we are using Google Chrome to avoid getting blocked
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

r = requests.get(url, headers=userAgent) # Send the request including the header
htmlText = r.text # Extract the raw HTML
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw HTML to Python

paragraphs = htmlDocument.find_all('fin-streamer') # Find all HTML elements of the type fin-streamer and store them as list

for p in paragraphs: # Go through all the fin-streamer elements and print the raw text
    text = p.get_text()
    print(text)
