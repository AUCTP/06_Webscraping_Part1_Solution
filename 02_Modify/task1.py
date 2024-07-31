import requests
import bs4

url = 'http://www.scrapethissite.com/pages/simple/'

r = requests.get(url)
htmlText = r.text
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')

search = {'class': 'col-md-4 country'}

countries = htmlDocument.find_all('div', search)

searchName = {'class': 'country-name'}

for country in countries:
    countryName = (country.find('h3', searchName))
    print(countryName.text.strip())
