"""Import csv file data into the database via Django ORM."""
from mysite.models import Stock
import pandas as pd

def import_csv_to_db(csv_path: str, ticker: str) -> None:
        """
        Load csv file data into the Django database.
        Args:
            csv_path: path of csv file to load from
            ticker: stock ticker symbol of the data
        Returns:
            None
        """
        dataFrame = pd.read_csv(csv_path, index_col=False)
        # Clear database of previous ticker data for clarity
        Stock.objects.filter(ticker=ticker).delete()    
        stocks = []
        for _, row in dataFrame.iterrows():
            stocks.append(
                    Stock(
                    ticker=ticker,
                    date=pd.to_datetime(row["Date"]).date(),
                    dayOpen=row["Open"],
                    dayHigh=row["High"],
                    dayLow=row["Low"],
                    dayClose=row["Close"],
                    dayVolume=row["Volume"]
                    )
            )
        Stock.objects.bulk_create(stocks)
        print(f"Successfully imported {csv_path} into the Django ORM.") 
