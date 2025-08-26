import requests
import gzip
import io
from bs4 import BeautifulSoup

print("Script started")

Url = "https://www.footlocker.com/en/category/mens/shoes.html"


response = requests.get(Url)
print(response)

"""
if requests.get(Url).status_code == 200:
    print("Successfully connected to the first URL")
    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
        xml_content = gz.read().decode('utf-8')
    print(xml_content[:500])
#else:
    print(f"Failed to connect. Status code: {response.status_code}")
    
"""
   
   
   
   

