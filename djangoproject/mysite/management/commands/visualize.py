# Create django management command to plot visualization of data from csv file
from django.core.management.base import BaseCommand, CommandError
from pipeline.visualizer import visualize_data

class Command(BaseCommand):
    help = 'Plot visualizations of data'

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Path of csv file to visualize"
        )

    def handle(self, *args, **options):
        visualize_data(options["csv_file"])
