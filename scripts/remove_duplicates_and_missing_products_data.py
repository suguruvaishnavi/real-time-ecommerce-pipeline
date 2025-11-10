import pandas

df = pandas.read_csv('products_data.csv')
df = df.dropna()
df = df.drop_duplicates()

print(df)
