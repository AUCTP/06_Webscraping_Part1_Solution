import requests # Import Requests library to send http requests

url = 'https://www.amazon.com/' # Define URL to scrape

userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'} # Define the user agent. We tell amazon that the request comes from a Google Chrome Browser and not from Python.

response = requests.get(url, headers=userAgent) # Send a get request to the URL including the user agent we defined in the header

print(response.status_code) # Show http status code. This time we get a 200 meaning that everything went fine.