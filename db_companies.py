import psycopg2
import requests
import pandas as pd
from bs4 import BeautifulSoup

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="dse",
        user="postgres",
        password="postgre",
        port = "5432"
    )
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # Fetch the query result
    result = cursor.fetchone()

    # Print the PostgreSQL server version
    print("Connected to PostgreSQL")
    print("PostgreSQL version:", result[0])
    
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)

table_name = "company_t"
table_schema = """
                CREATE TABLE IF NOT EXISTS company_t (
                    company_id SERIAL PRIMARY KEY,
                    company_name VARCHAR(255),
                    scrip_code INTEGER,
                    trading_code VARCHAR(100),
                    sector VARCHAR(100)
                )
""".format(table=table_name)

df = pd.read_csv('companies.csv')
rows = df.shape[0]

cursor.execute(table_schema)

for i in range(0, rows):
    cursor.execute("""INSERT INTO company_t VALUES(%s, %s, %s, %s, %s);""", (i, df['Company Name'][i], int(df['Scrip Code'][i]), df['Trading Code'][i], df['Sector'][i]))

conn.commit()
cursor.close()
conn.close()