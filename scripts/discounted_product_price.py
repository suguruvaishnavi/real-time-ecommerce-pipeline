import pandas

df = pandas.read_csv("products_data_clean.csv")
df['Discounted_Price'] = df['Price'] * 0.9 # 10% discount

df.to_csv("products_data_clean.csv", index=False, encoding='utf-8')
