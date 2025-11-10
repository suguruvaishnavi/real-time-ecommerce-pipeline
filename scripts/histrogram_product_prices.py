import matplotlib.pyplot as plt,pandas

df = pandas.read_csv("products_data_clean.csv")
df['Price'].hist(bins=10)  # make a histogram of product prices
plt.show()