"""Download historical stock data from Yahoo Finance."""
import yfinance as yf
import pandas as pd
import os

OUTPUT_DIR = "./data/"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")
DEFAULT_PERIOD = "1y"

def download_data(ticker: str) -> pd.DataFrame:
    """ 
    Download data via yfinance api into a csv file.
    Args:
        ticker: Stock ticker symbol
    Returns:
        Pandas DataFrame representing the stock data.
    """
    print(f"Downloading stock data for {ticker}...")
    stock = yf.Ticker(ticker)
    dataFrame = stock.history(period=DEFAULT_PERIOD)
    dataFrame["Date"] = dataFrame.index.date
    return dataFrame

def save_to_csv(df: pd.DataFrame, output_file: str = OUTPUT_FILE) -> None:
    """
    Convert Pandas DataFrame data to local csv file.
    Args:
        df: Pandas DataFrame containing stock data
        output_file: path of csv file to save into
    Returns:
        None
    """
    header = ["Open", "High", "Low", "Close", "Volume"]

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    df.to_csv(output_file, columns=header)
    print(f"Successfully downloaded data to: {OUTPUT_FILE}")
