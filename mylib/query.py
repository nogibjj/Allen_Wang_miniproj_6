import mysql.connector
from mysql.connector import Error
import os 
from dotenv import load_dotenv

def create_row(country,beer_servings,spirit_servings,wine_servings, total_litres_of_pure_alcohol):
    #load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        sql = '''INSERT INTO drink(country,beer_servings,spirit_servings,wine_servings, total_litres_of_pure_alcohol) VALUES(?, ?,?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, (country,beer_servings,spirit_servings,wine_servings, total_litres_of_pure_alcohol))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.lastrowid
    except Error as e:
        print(e)



def read_all():
    #load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        sql = '''SELECT * FROM drink'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Error as e:
        print(e)


def update_row(country, beer_servings):
    #load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        sql = '''UPDATE drink SET beer_servings = ? WHERE country = ?'''
        cursor = conn.cursor()
        cursor.execute(sql,  (beer_servings,country))
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(e)

def delete_row(country):
    #load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        sql = '''DELETE FROM drink WHERE country = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (country,))
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(e)


def general(query):
    #load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cursor = conn.cursor()
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            conn.close()
            return results
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(e)