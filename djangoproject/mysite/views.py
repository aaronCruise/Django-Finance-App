"""Control the backend logic for the home page via Django view function."""
from django.shortcuts import render
from mysite.models import Stock
from pathlib import Path
from django.conf import settings
from pipeline.downloader import download_data, save_to_csv
from pipeline.analyzer import analyze_data
from pipeline.visualizer import visualize_data
from pipeline.importer import import_csv_to_db

DEBUG = True

def stock_data(request) -> None:
    """
    Main view function for the home page.
    Contains logic to grab yfinance data using the pipeline/ functions.
    """
    table = None
    plot_exists = False

    # Request from the form submission on the home page
    if request.method == "POST":
        Stock.objects.all().delete()
        ticker = request.POST.get("ticker").upper()
        df = download_data(ticker)
        csv_path = Path(settings.BASE_DIR) / "data" / "data.csv"
        save_to_csv(df, csv_path)
        visualize_data(csv_path)
        import_csv_to_db(csv_path, ticker)
        plot_path = Path(settings.BASE_DIR) / "static" / "plots" / "plot.png"
        plot_exists = plot_path.exists()
        table = Stock.objects.order_by('-date')
        if DEBUG: print("Request received")
        if DEBUG: print("Stock rows count:", table.count())

    # Request from initial launch to home page. Assume user went through manual data pipeline.
    elif request.method == "GET":
        table = Stock.objects.order_by('-date') 
        plot_path = Path(settings.BASE_DIR) / "static" / "plots" / "plot.png"
        plot_exists = plot_path.exists()

    return render(request, "stock_data.html", {'table':table, 'plot_exists':plot_exists})
