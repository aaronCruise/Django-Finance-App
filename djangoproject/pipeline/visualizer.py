"""Create matplotlib visualizations of csv data."""
import pandas as pd
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "./static/plots/"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "plot.png")

def visualize_data(csv_path: str) -> None:
    """
    Plot a visualization of the csv file data.
    Args:
        csv_path: path of csv file
    Returns:
        None
    """
    dataFrame = pd.read_csv(csv_path, index_col = False)
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    ax.plot(dataFrame['Date'], dataFrame['Close'])
    plt.xlabel("Date")

    # Label the midpoint
    start = dataFrame.index.min()
    end = dataFrame.index.max()
    mid = start + (end - start)/2
    plt.xticks([start, mid, end], rotation=90)

    plt.ylabel("Close")
    plt.title("Closing Price vs Date")
    plt.grid()
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    plt.savefig(OUTPUT_FILE, dpi=100, bbox_inches="tight")
    print(f"Plotted Closing Price vs Date to {OUTPUT_FILE}")
    plt.close(fig)
