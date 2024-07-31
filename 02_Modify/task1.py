import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

url = 'http://www.scrapethissite.com/pages/simple/' # Define URL to scrape

r = requests.get(url) # Send the request
htmlText = r.text # Extract the raw HTML
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw HTML to Python

search = {'class': 'col-md-4 country'} # Define the search to find the country elements

countries = htmlDocument.find_all('div', search) # Extract all divs matching the search (country elements) and store them to a list

searchName = {'class': 'country-name'} # Define the search to find the name of a country
searchCapital = {'class': 'country-capital'} # Define the search to find the capital of a country
searchPopulation = {'class': 'country-population'} # Define the search to find the population of a country
searchArea = {'class': 'country-area'} # Define the search to find the area of a country

countriesDict = {} # Create an empty dictionary to store all the information on a country

for country in countries: # Iterate over the country elements
    countryName = country.find('h3', searchName).text.strip() # Find the first h3 matching the search criteria defined in searchName
    countryCapital = country.find('span', searchCapital).text.strip() # Find the first span matching the search criteria defined in searchCapital
    countryPopulation = country.find('span', searchPopulation).text.strip() # Find the first span matching the search criteria defined in searchPopulation
    countryArea = country.find('span', searchArea).text.strip() # Find the first span matching the search criteria defined in searchArea
    countriesDict[countryName] = { # Add the country to the outer dictionary using the name as the key and the additional information as values in an inner dictionary
        'capital': countryCapital,
        'population': countryPopulation,
        'area': countryArea
    }

print('Name\tCapital\tPopulation\tArea'.expandtabs(30))
for name, details in countriesDict.items():
    print(f"{name[:20]}\t{details['capital']}\t{details['population']}\t{details['area']}".expandtabs(30))