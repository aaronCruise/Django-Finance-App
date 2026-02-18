from django.shortcuts import render
from mysite.models import Stock

DEBUG = 1

# Create your views here.
def stock_data(request):
    table = None
    if request.method == 'POST':
        if DEBUG: print("POST received")
        table = Stock.objects.all()
        if DEBUG: print("Stock rows count:", table.count())
    return render(request, "stock_data.html", {'table':table})
