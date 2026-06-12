import csv

# Stock prices dictionary
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")

for stock, price in stocks.items():
    print(f"{stock} : ${price}")

num = int(input("\nHow many stocks do you want to buy? "))

for i in range(num):

    print(f"\nStock {i+1}")

    stock_name = input("Enter Stock Name: ").upper()

    if stock_name in stocks:

        quantity = int(input("Enter Quantity: "))

        investment = quantity * stocks[stock_name]

        portfolio[stock_name] = {
            "Quantity": quantity,
            "Price": stocks[stock_name],
            "Investment": investment
        }

        total_investment += investment

    else:
        print("Invalid Stock Name!")

print("\n")
print("=" * 50)
print("PORTFOLIO SUMMARY")
print("=" * 50)

print(
    f"{'Stock':<10}{'Price':<10}{'Quantity':<10}{'Investment':<15}"
)

for stock, details in portfolio.items():
    print(
        f"{stock:<10}"
        f"{details['Price']:<10}"
        f"{details['Quantity']:<10}"
        f"{details['Investment']:<15}"
    )

print("\nTotal Investment Value =", total_investment)

# Save to CSV

with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Stock", "Price", "Quantity", "Investment"]
    )

    for stock, details in portfolio.items():

        writer.writerow([
            stock,
            details["Price"],
            details["Quantity"],
            details["Investment"]
        ])

    writer.writerow([])
    writer.writerow(
        ["Total Investment", "", "", total_investment]
    )

print("\nPortfolio saved successfully in portfolio.csv")