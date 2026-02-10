# Load CSV data and inspect data

import pandas as pd

input_file = "data.csv"

dataFrame = pd.read_csv(input_file, index_col=False)

print("Summary:")
print(dataFrame.describe())

print("Checking any missing values...")
print(dataFrame.isnull().values.any())
