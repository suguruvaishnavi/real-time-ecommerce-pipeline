# Step 1: Import helpers
import requests  # This helps Python talk to websites
import time      # This helps Python wait or pause

# Step 2: Remember the API website
API_URL = "https://dummyjson.com/products"  # This is where we get fake product data

# Step 3: Make a helper machine (function) to get data
def get_sales_data():

    # Ask the website for data
    response = requests.get(API_URL)

    # If something goes wrong, stop the program and tell us
    response.raise_for_status()

    # Convert the website data into Python language (list/dictionary)
    data = response.json()

    # Return the data so the rest of the program can use it
    return data

# Step 4: Keep asking for data forever
while True:
    # Call our helper machine to get fresh sales data
    sales_data = get_sales_data()

    # Print a fun message to know new data arrived
    print("🛒 New Sales Data Arrived!")
