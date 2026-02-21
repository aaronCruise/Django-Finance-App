"""Analyze data from a CSV file and check for missing values."""
import pandas as pd

INPUT_FILE = "./data/data.csv"

def analyze_data(input_file: str = INPUT_FILE) -> None:
    """
    Analyze csv file data and check for missing values.
    Args:
        input_file: Path name of csv file
    Returns:
        None
    """
    dataFrame = pd.read_csv(INPUT_FILE, index_col=False)
    print("Summary:")
    print(dataFrame.describe())
    print("Checking any missing values...")
    print(dataFrame.isnull().values.any())
