import pyodbc
import os
import csv
from dotenv import load_dotenv

load_dotenv()

driver_name = os.getenv("DRIVER_NAME")
schema_name = os.getenv("SCHEMA_NAME")
server_name = os.getenv("SERVER_NAME")
db_name = os.getenv("DB_NAME")

conn_str = f"DRIVER={driver_name};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def load_supplements():
        
    catalog_file_path = "data/silver/supplements_catalog.csv"
    with open(catalog_file_path, "r", encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            supplement_name = row[0]
            overview = row[1]
            sideeffects = row[2]
            precautions = row[3]
            dosing = row[4]
            print(supplement_name)
            
            sql = f"""
            INSERT INTO {schema_name}.supplement_catalog (SupplementName, Overview, SideEffects, Precautions, Dosing)
            VALUES (?, ?, ?, ?, ?)
            """

            cursor.execute(sql, supplement_name, overview, sideeffects, precautions, dosing)

    conn.commit()

if __name__ == "__main__":
    load_supplements()