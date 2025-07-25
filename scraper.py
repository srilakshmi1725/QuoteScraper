import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com/"

# Send GET request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote blocks
quotes = soup.find_all('div', class_='quote')

# Loop through each quote block
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f'"{text}" - {author}')
