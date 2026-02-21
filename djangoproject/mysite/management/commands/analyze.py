# Create django management command to inspect/analyze csv data
from django.core.management.base import BaseCommand, CommandError
from mysite.models import Stock
from pipeline.analyzer import analyze_data
import pandas as pd

class Command(BaseCommand):
    help = 'Load csv data and inspect/analyze data'

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Path of csv file to analyze"
        )

    def handle(self, *args, **options):
        analyze_data(options["csv_file"])
