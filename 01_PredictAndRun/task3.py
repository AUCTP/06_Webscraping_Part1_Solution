import requests
import bs4

url = 'http://www.scrapethissite.com/pages/simple/'

r = requests.get(url)

htmlDocument = bs4.BeautifulSoup(r.text, 'html.parser')

countries = htmlDocument.find_all("h3")

for country in countries:
    print(country.get_text())
