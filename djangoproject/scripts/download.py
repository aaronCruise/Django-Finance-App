# Download stock data to CSV file
import yfinance as yf
import pandas as pd

ticker = "VT"
output_file = "../data/data.csv"

print(f"Downloading stock data for {ticker}...")
stock = yf.Ticker(ticker)

header = ["Open", "High", "Low", "Close", "Volume"]

dataFrame = stock.history(period="1y")
dataFrame["Date"] = dataFrame.index.date

dataFrame.to_csv(output_file, columns=header)
print(f"Successfully downloaded data to: {output_file}")
