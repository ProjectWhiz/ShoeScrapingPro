import requests
from bs4 import BeautifulSoup
from main import *

def scrape_shoes(search_params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    base_url = "https://www.footlocker.com/en/category/mens/shoes.html"
    
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get all product cards
        products = soup.find_all('a', class_='ProductCard-content')
        
        found_items = []
        
        for product in products:
            product_name = product.find('span', class_='ProductName-primary')
            product_price = product.find('span', class_='ProductPrice')
            
            # Filter based on search parameters
            if 'brand' in search_params:
                if (product_name and 
                    search_params['brand'].lower() in product_name.text.lower()):
                    found_items.append({
                        'name': product_name.text if product_name else 'N/A',
                        'price': product_price.text if product_price else 'N/A',
                        'size': search_params['size']
                    })
                    
            elif 'price' in search_params:
                if product_price:
                    price_value = float(product_price.text.replace('$', '').strip())
                    if price_value <= search_params['price']:
                        found_items.append({
                            'name': product_name.text if product_name else 'N/A',
                            'price': price_value,
                            'size': search_params['size']
                        })
        
        # Print results
        if found_items:
            print("\nFound matching items:")
            for item in found_items:
                print(f"Name: {item['name']}")
                print(f"Price: ${item['price']}")
                print(f"Size: {item['size']}")
                print("-" * 50)
        else:
            print("No matching items found.")
            
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

def main():
    # Get user input
    shoe_input = ShoeInput()
    shoe_input.input_type()
    
    # Get search parameters
    search_params = shoe_input.get_search_params()
    
    # Perform scraping with parameters
    scrape_shoes(search_params)

if __name__ == "__main__":
    main()





   
   
   
   

