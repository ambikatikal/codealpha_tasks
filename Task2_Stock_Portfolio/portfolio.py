# Stock Portfolio Tracker

import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("Welcome to Stock Portfolio Tracker!")
print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    portfolio.append([stock_name, quantity, stock_prices[stock_name], investment])

    print("Investment for", stock_name, ":", "$", investment)

# Save portfolio to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Investment"])

    for item in portfolio:
        writer.writerow(item)

print("\nTotal Investment Value: $", total_investment)
print("Portfolio saved to portfolio.csv")
print("Thank you for using Stock Portfolio Tracker!")