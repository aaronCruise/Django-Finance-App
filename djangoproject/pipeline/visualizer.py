# Plot visualizations of data
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "./data/data.csv"
OUTPUT_FILE = "./static/plots/plot.png"

def visualize_data(csv_path: str) -> None:
    dataFrame = pd.read_csv(csv_path, index_col = False)
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    ax.plot(dataFrame['Date'], dataFrame['Close'])
    plt.xlabel("Date")
    start = dataFrame.index.min()
    end = dataFrame.index.max()
    mid = start + (end - start)/2
    plt.xticks([start, mid, end], rotation=90)
    plt.ylabel("Close")
    plt.title("Closing Price vs Date")
    plt.grid()
    plt.savefig(OUTPUT_FILE, dpi=100, bbox_inches="tight")
    print(f"Plotted Closing Price vs Date to {OUTPUT_FILE}")
    plt.close(fig)

if __name__ == "__main__":
    visualize_data(INPUT_FILE)
