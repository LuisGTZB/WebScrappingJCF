import requests
from bs4 import BeautifulSoup

url = 'https://jovenesconstruyendoelfuturo.stps.gob.mx/bc/avisovinc.php'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

body = soup.body

print(body)

import time

while True:
    response = requests.get(url)
    new_soup = BeautifulSoup(response.content, 'html.parser')
    new_body = new_soup.body
    
    if new_body != body:
        print("The body of the webpage has changed!")
        
    time.sleep(1800) # 1800 seconds = 30 minutes

