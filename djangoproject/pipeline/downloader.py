# Download stock data to CSV file
import yfinance as yf
import pandas as pd
import argparse as ap

OUTPUT_FILE = "./data/data.csv"

def download_data(ticker: str) -> pd.DataFrame:
    print(f"Downloading stock data for {ticker}...")
    stock = yf.Ticker(ticker)
    dataFrame = stock.history(period="1y")
    dataFrame["Date"] = dataFrame.index.date
    return dataFrame

def save_to_csv(df: pd.DataFrame, output_file: str = OUTPUT_FILE) -> None:
    header = ["Open", "High", "Low", "Close", "Volume"]
    df.to_csv(output_file, columns=header)
    print(f"Successfully downloaded data to: {OUTPUT_FILE}")

if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("ticker", help="Ticker symbol you'd like to download")
    args = parser.parse_args()

    df = download_data(args.ticker) 
    save_to_csv(df)
