import pandas as pd

#reading in csv file

df = pd.read_csv('sales.csv')
df.name = 'sales'
print(df.to_string())
list_sales = df['sales'].tolist()
total_sales = sum(list_sales)

#outputting the total sales across all months

sales_month = list(df['sales'])
print(sales_month)
total_month = sum(sales_month)
print(total_month)
