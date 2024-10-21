import requests
import mysql.connector
import csv
from io import StringIO
import os
from dotenv import load_dotenv

def csv_to_db(url1,url2):
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
            DROP TABLE IF EXISTS drink;
        ''')
        conn.commit()

        response = requests.get(url1)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {url1}. Status code: {response.status_code}")

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
        print(f"Data from {url1} successfully inserted into the database.")

        cursor.execute('''
            DROP TABLE IF EXISTS drug_use;
        ''')
        conn.commit()

        # Fetch data from the URL
        response = requests.get(url2)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {url2}. Status code: {response.status_code}")

        csv_data = response.text

        # Create the drug_use table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS drug_use (
                age_group VARCHAR(50),
                number INT,
                alcohol_use FLOAT,
                alcohol_frequency FLOAt,
                marijuana_use FLOAT,
                marijuana_frequency FLOAt,
                cocaine_use FLOAT,
                cocaine_frequency FLOAt,
                crack_use FLOAT,
                crack_frequency FLOAt,
                heroin_use FLOAT,
                heroin_frequency FLOAt,
                hallucinogen_use FLOAT,
                hallucinogen_frequency FLOAt,
                inhalant_use FLOAT,
                inhalant_frequency FLOAt,
                pain_releiver_use FLOAT,
                pain_releiver_frequency FLOAt,
                oxycontin_use FLOAT,
                oxycontin_frequency FLOAt,
                tranquilizer_use FLOAT,
                tranquilizer_frequency FLOAt,
                stimulant_use FLOAT,
                stimulant_frequency FLOAt,
                meth_use FLOAT,
                meth_frequency FLOAt,
                sedative_use FLOAT,
                sedative_frequency FLOAt
            );
        ''')
        conn.commit()

        csv_reader = csv.reader(StringIO(csv_data))
        next(csv_reader)

        for row in csv_reader:
            row = [None if value == '-' else value for value in row]
            print(row)
            if len(row) == 28:
                cursor.execute('''
                    INSERT INTO drug_use (
                        age_group,
                        number,
                        alcohol_use,
                        alcohol_frequency,
                        marijuana_use,
                        marijuana_frequency,
                        cocaine_use,
                        cocaine_frequency,
                        crack_use,
                        crack_frequency,
                        heroin_use,
                        heroin_frequency,
                        hallucinogen_use,
                        hallucinogen_frequency,
                        inhalant_use,
                        inhalant_frequency,
                        pain_releiver_use,
                        pain_releiver_frequency,
                        oxycontin_use,
                        oxycontin_frequency,
                        tranquilizer_use,
                        tranquilizer_frequency,
                        stimulant_use,
                        stimulant_frequency,
                        meth_use,
                        meth_frequency,
                        sedative_use,
                        sedative_frequency
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                ''', row)
                print(row)
        
        conn.commit()
        conn.close()
        print("Data inserted successfully into the 'drug_use' table.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
#csv_to_db("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")
