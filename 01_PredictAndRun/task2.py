import requests
import bs4

url = 'http://www.scrapethissite.com/pages/simple/'

r = requests.get(url)

htmlDocument = bs4.BeautifulSoup(r.text, 'html.parser')

print(htmlDocument.find("h3").text)