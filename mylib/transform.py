import requests
import mysql.connector
import csv
from io import StringIO
import os
from dotenv import load_dotenv

def csv_to_db(url):
    load_dotenv()
    db_config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME')
    }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(''' 
            SELECT COUNT(*) FROM information_schema.tables 
            WHERE table_schema = %s AND table_name = %s
        ''', (db_config['database'], 'drink'))
        table_exists = cursor.fetchone()[0]

        if table_exists:
            print(f"The table 'drink' already exists. Skipping data insertion.")
            conn.close()
            return
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

        csv_data = response.text
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS drink (
                country VARCHAR(255),
                beer_servings INT,
                spirit_servings INT,
                wine_servings INT,
                total_litres_of_pure_alcohol FLOAT
            );
        ''')
        conn.commit()

        csv_reader = csv.reader(StringIO(csv_data))
        next(csv_reader)
        for row in csv_reader:
            if len(row) == 5:
                cursor.execute('''
                    INSERT INTO drink (country, beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol)
                    VALUES (%s, %s, %s, %s, %s);
                ''', row)
                print(row)
        conn.commit()
        conn.close()
        
        print(f"Data from {url} successfully inserted into the database.")


    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
#csv_to_db("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")
