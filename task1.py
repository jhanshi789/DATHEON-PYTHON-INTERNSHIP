import csv
import os
from datetime import datetime

# Store portfolio details
portfolio = {}

print("=" * 55)
print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 55)

while True:
    ticker = input("\nEnter Stock Ticker Symbol: ").upper()

    buy_price = float(input("Enter Buying Price: "))
    shares = int(input("Enter Number of Shares: "))
    current_price = float(input("Enter Current Stock Price: "))

    if buy_price <= 0 or shares <= 0 or current_price < 0:
        print("Invalid values! Please try again.")
        continue

    # Store data in dictionary
    portfolio[ticker] = {
        "buy_price": buy_price,
        "shares": shares,
        "current_price": current_price
    }

    choice = input("\nAdd another stock? (yes/no): ").lower()

    if choice != "yes":
        break

# Calculate portfolio performance
total_investment = 0
total_current_value = 0

print("\n" + "=" * 65)
print("              PORTFOLIO SUMMARY")
print("=" * 65)

print(f"{'Stock':<10}{'Investment':<15}{'Current Value':<17}{'Gain/Loss':<15}")

# Prepare CSV data
file_name = "portfolio_summary.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists or os.path.getsize(file_name) == 0:
        writer.writerow([
            "Date", "Stock", "Buy Price", "Shares",
            "Current Price", "Investment",
            "Current Value", "Gain/Loss", "Percentage"
        ])

    for ticker, data in portfolio.items():

        investment = data["buy_price"] * data["shares"]

        current_value = data["current_price"] * data["shares"]

        gain_loss = current_value - investment

        percentage = (gain_loss / investment) * 100

        total_investment += investment
        total_current_value += current_value

        print(
            f"{ticker:<10}"
            f"{investment:<15.2f}"
            f"{current_value:<17.2f}"
            f"{gain_loss:<15.2f}"
        )

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ticker,
            data["buy_price"],
            data["shares"],
            data["current_price"],
            round(investment, 2),
            round(current_value, 2),
            round(gain_loss, 2),
            round(percentage, 2)
        ])

# Calculate total portfolio performance
total_gain_loss = total_current_value - total_investment

if total_investment > 0:
    total_percentage = (total_gain_loss / total_investment) * 100
else:
    total_percentage = 0

print("=" * 65)
print(f"Total Investment    : Rs. {total_investment:.2f}")
print(f"Current Value       : Rs. {total_current_value:.2f}")
print(f"Total Gain/Loss     : Rs. {total_gain_loss:.2f}")
print(f"Percentage          : {total_percentage:.2f}%")
print("=" * 65)

print("\nPortfolio data saved successfully!")
print("CSV File:", file_name)