import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

url = 'http://www.scrapethissite.com/pages/simple/' # Define URL to scrape

r = requests.get(url) # Send a get request to the URL

htmlDocument = bs4.BeautifulSoup(r.text, 'html.parser') # Parse the returned HTML string to Python

print(htmlDocument.find("h3").text) # Find the first h3 HTML document and return the text