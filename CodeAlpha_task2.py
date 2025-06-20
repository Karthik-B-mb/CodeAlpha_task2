import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

print("\n💵 Stock Prices:")
for symbol, price in stock_prices.items():
    print(f"{symbol}: ${price}")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in database.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_value = 0
print("\n🧾 Investment Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

save = input("Would you like to save this to a file? (y/n): ").lower()
if save == 'y':
    filename = "portfolio_summary.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            writer.writerow([stock, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total", "", "", total_value])
    print(f"📄 Portfolio saved to {filename}")