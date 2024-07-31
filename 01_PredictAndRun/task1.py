import requests
import bs4

url = 'http://www.scrapethissite.com/pages/simple/'

r = requests.get(url)
print(r.status_code)
print(r.text)