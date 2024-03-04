# Importing the libraries
import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/apps/details?id=tv.twitch.android.app&hl=pt_BR&gl=US'

# Getting information from the website through an HTTP request (GET)
response = requests.get(url)

# Analyzing the content of the page and creating a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Getting all the content from the chosen tag
texts = [tag.text for tag in soup.find_all('div', class_='bARER')]
texts = texts[0]

file_name = '01_web_text.txt'

# Opening the file in write mode
with open(f'.\\results\\{file_name}', 'w', encoding = 'utf-8') as arq:

    # Write the items to the file, joining them with line breaks
    arq.write(texts)