#First version of real-time fake sales polling script
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

    for item in products_data['products']:
        print(f"Product: {item['title']}, Price: ${item['price']}")
        print("Waiting 5 seconds before polling again...\n")
        time.sleep(5)

