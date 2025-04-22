import pyodbc
import os
import sys
from dotenv import load_dotenv

load_dotenv()

driver_name = os.getenv("DRIVER_NAME")
schema_name = os.getenv("SCHEMA_NAME")
server_name = os.getenv("SERVER_NAME")
db_name = os.getenv("DB_NAME")

try:
    conn_str = f"DRIVER={driver_name};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes"
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        with open('schema/create_db_and_schema/create_tables.sql') as supp:
            sql = supp.read()
            sql = sql.replace('{{schema_name}}', schema_name)
            conn.commit()
            cursor.execute(sql)
            conn.commit()
        print(f"Tables created.")
except Exception as e:
    print("Error when creating tables")
    print(e)
    sys.exit()
