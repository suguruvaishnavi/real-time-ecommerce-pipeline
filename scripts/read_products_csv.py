# reading data from cvs file and checking if data is correct

import pandas

df = pandas.read_csv('products_data.csv')
print(df.head())

