import pandas

df = pandas.read_csv('products_data.csv')

df = df.dropna()

df = df.drop_duplicates()

df.to_csv("products_data_clean.csv", index=False, encoding="utf-8")

print("✅ Cleaned CSV saved as products_data_clean.csv")
