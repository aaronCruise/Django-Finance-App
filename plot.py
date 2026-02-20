# Plot visualizations of data
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from django.conf import settings

input_file = "data.csv"
output_file = "plot.png"
plot_path = Path(settings.BASE_DIR) / "static" / "plots" / output_file

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
plt.savefig(plot_path)
print(f"Plotted Closing Price vs Date to {output_file}")
