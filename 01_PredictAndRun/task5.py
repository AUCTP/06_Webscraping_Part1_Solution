import requests

url = 'https://www.amazon.com/'

userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

response = requests.get(url, headers=userAgent)

print(response.status_code)