import requests # Import Requests library to send http requests

url = 'https://www.amazon.com/' # Define URL to scrape
response = requests.get(url) # Send a get request to the URL
print(response.status_code) # Show http status code. Here we get a 503 which means "service unavailable". We get this response as amazon blocks the request made by Python
