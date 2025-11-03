
import requests, time

API_URL = "https://dummyjson.com/products"

def get_products_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return data

while True:
    products_data = get_products_data()
    print("🛒 New Products Data Arrived!")

    for product in products_data['products']:
        print(f"Product: {product['title']}, Price: ${product['price']}")
        print("Waiting 5 seconds before polling again...\n")
        time.sleep(5)

