
import requests, time

API_URL = "https://dummyjson.com/products"

def get_products_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return data

products_data = get_products_data()
print(products_data["products"][0].keys())