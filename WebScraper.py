import requests
from bs4 import BeautifulSoup


#Fetching the wesite content
url='https://books.toscrape.com'
response = requests.get(url)

if response.status_code == 200:
    #print("Website fetched successfully")
    soup = BeautifulSoup(response.text, 'html.parser')#Parsing the HTML content
    titles = soup.find_all('h3') #Extracting needed data
    for title in titles:
        print(title.a['title'])

else:
    print("Failed to fetch website")


'''
To scrape quotes
url='https://quotes.toscrape.com'
quotes = soup.find_all('span',class_='text') #Extracting needed data
    for quote in quotes:
        print(quote.text)
'''
