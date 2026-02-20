# Plot visualizations of data
import pandas as pd
import matplotlib.pyplot as plt

input_file = "../data/data.csv"
output_file = "../data/plot.png"

dataFrame = pd.read_csv(input_file, index_col = False)

fig, ax = plt.subplots()
ax.plot(dataFrame['Date'], dataFrame['Close'])
plt.xlabel("Date")
start = dataFrame.index.min()
end = dataFrame.index.max()
mid = start + (end - start)/2
plt.xticks([start, mid, end], rotation=90)
plt.ylabel("Close")
plt.title("Closing Price vs Date")
plt.grid()
plt.savefig(output_file)
print(f"Plotted Closing Price vs Date to {output_file}")
