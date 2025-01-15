import pandas as pd
import csv

sales_data = pd.read_csv('sales_2025.csv')
customer_data = pd.read_csv('customers.csv')

merged_data = pd.merge(sales_data, customer_data, on='CustomerID', how='inner')
print(merged_data)

merged_data["Total_Sales"] = merged_data["Price"] * merged_data["Quantity"]
print(merged_data)

#drop = sales_data["Price"].dropna()
#print(drop)

isNull = sales_data["Price"].isnull().sum()
print(isNull)


# with open('newSales.csv', 'w') as newSales:
#     writer = csv.writer(newSales)
#     writer.writerow(sales_data)

merged_data.to_csv('newSales.csv', index=False)

