import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

url = 'http://www.scrapethissite.com/pages/simple/' # Define URL to scrape

r = requests.get(url) # Send a get request to the URL

htmlDocument = bs4.BeautifulSoup(r.text, 'html.parser') # Parse the returned HTML string to Python

countries = htmlDocument.find_all("h3") # Find all h3 elements and store them in a list

for country in countries: # Iterate over the h3 elements (countries) in the list
    print(country.get_text()) # Extract the raw text (name) of each country
