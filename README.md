# Yahoo Finance Data Pipeline
A Django web application that retrieves, processes, visualizes, and stores stock data from Yahoo Finance.

### Features:
- Fetching financial data from an external API
- Exporting data to local csv files
- Analyzing and visualizing data using python libraries
- Building a Django model to represent stock data
- Rendering a Django web view that displays data

![home page](images/home_page.png)

### Tech Stack:
- HTML & CSS
- Django
- Python (pandas, matplotlib)
- SQLite (via Django ORM)

### Setup:
1. Clone the repository.

    ```bash
    git clone https://github.com/aaronCruise/Django-Finance-App.git
    cd Django-Finance-App/djangoproject
    ```

2. Install dependencies:
    
    ```bash
    pip install django yfinance pandas matplotlib dotenv
    ```

3. Generate a Django secret key and set enviornmental variable:

    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(f'DJANGO_SECRET_KEY={get_random_secret_key()}')" > .env
    ```

4. Run Django migrations:
    
    ```bash
    python manage.py migrate
    ```

5. Start server:

    ```bash
    python manage.py runserver
    ```
or ...

### Optional Manual Data Pipeline:
5. Run the data retrieval command to generate a CSV file:
    
    ```bash
    python manage.py download <ticker>
    ```

6. Check csv data:

    ```bash
    python manage.py analyze data/data.csv
    ```

7. Plot visual and save:

    ```bash
    python manage.py visualize data/data.csv
    ```

8. Import data into Django database:

    ```bash
    python manage.py import data/data.csv <ticker>
    ```

9. Then start server:

    ```bash
    python manage.py runserver
    ```
