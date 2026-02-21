# Load CSV data and inspect data
import pandas as pd

INPUT_FILE = "./data/data.csv"

def analyze_data(input_file: str = INPUT_FILE) -> None:
    dataFrame = pd.read_csv(INPUT_FILE, index_col=False)
    print("Summary:")
    print(dataFrame.describe())
    print("Checking any missing values...")
    print(dataFrame.isnull().values.any())

if __name__ == "__main__":
    analyze_data(input_file=INPUT_FILE)
