import requests # Import Requests library to send http requests

url = 'http://www.scrapethissite.com/pages/simple/' # Define URL to scrape

r = requests.get(url) # Send a get request to the URL
print(r.status_code) # Show the http status code (200: Ok, everything else: something went wrong)
print(r.text) # Show the raw HTML returned by the webserver