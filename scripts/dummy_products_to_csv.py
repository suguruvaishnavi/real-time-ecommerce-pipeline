#every time we get new dummy product data, we save it into a CSV file
import requests, time, csv

API_URL = "https://dummyjson.com/products"

def get_products_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return data

while True:
    products_data = get_products_data()
    print("🛒 New Products Data Arrived!")

    with open("products_data.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Title", "Price", "Description"])

        for product in products_data['products']:
            writer.writerow([product['title'], product['price'], product['description']])
            print(f"Saved Product: {product['title']}, Price: ${product['price']}")
            time.sleep(5)