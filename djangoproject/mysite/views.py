from django.shortcuts import render
from mysite.models import Stock
from pathlib import Path
from django.conf import settings

DEBUG = 1

# Create your views here.
def stock_data(request):
    table = None
    plot_path = Path(settings.BASE_DIR) / "static" / "plots" / "plot.png"
    plot_exists = plot_path.exists()
    table = Stock.objects.all()
    if DEBUG: print("Request received")
    if DEBUG: print("Stock rows count:", table.count())
    return render(request, "stock_data.html", {'table':table, 'plot_exists':plot_exists})
