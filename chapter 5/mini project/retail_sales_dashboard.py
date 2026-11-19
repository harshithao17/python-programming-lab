import csv
import matplotlib.pyplot as plt

# Creating CSV file

with open("sales.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Product", "Sales"])

    writer.writerow(["Laptop", 50000])
    writer.writerow(["Mobile", 30000])
    writer.writerow(["Tablet", 20000])
    writer.writerow(["Headphones", 10000])
    writer.writerow(["Keyboard", 5000])


# Reading CSV file

products = []
sales = []

with open("sales.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        products.append(row["Product"])
        sales.append(int(row["Sales"]))


# Displaying sales details

print("RETAIL SALES DASHBOARD")

total_sales = sum(sales)

print("Total Sales:", total_sales)

for i in range(len(products)):
    print(products[i], ":", sales[i])


# Creating bar chart

plt.bar(products, sales)

plt.xlabel("Products")
plt.ylabel("Sales Amount")

plt.title("Retail Sales Dashboard")

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()