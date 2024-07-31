import requests

url = 'https://www.amazon.com/'
response = requests.get(url)
print(response.status_code)
