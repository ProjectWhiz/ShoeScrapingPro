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
        
        """
        print("HTML Content Preview:") #Finding Tags
        print(response.text[:100000])
        """
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get all product cards
        products = soup.find_all('div', class_='ProductCard')
        
        found_items = []
        
        for product in products:
            product_name = product.find('span', class_='ProductName-primary')
            product_price = product.find('div', class_='ProductPrice')
            
            # Filter based on search parameters
            if 'brand' in search_params:
                if (product_name and 
                    search_params['brand'].lower() in product_name.text.lower()):
                    found_items.append({
                        'name': product_name.text if product_name else 'N/A',
                        'price': product_price.text if product_price else 'N/A',
                            
                    })
                    
            elif 'price' in search_params:
                if product_price:
                    price_value = float(product_price.text.replace('$', '').strip())
                    if price_value <= search_params['price']:
                        found_items.append({
                            'name': product_name.text if product_name else 'N/A',
                            'price': price_value,
                            
                        })
        
        # Print results
        if found_items:
            print("\nFound matching items:")
            for item in found_items:
                print(f"Name: {item['name']}")
                print(f"Price: {item['price']}")
                
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





   
   
   
   

