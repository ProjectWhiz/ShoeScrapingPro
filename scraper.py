import requests
from bs4 import BeautifulSoup

print("Script started")

Url = "https://www.footlocker.com/en/category/mens/shoes.html"

response = requests.get(Url)

soup = BeautifulSoup(response.content, 'html.parser')

parse = soup.find_all('span', class_ = 'ProductName-primary')

for parse in parse:
    print(parse)





   
   
   
   

