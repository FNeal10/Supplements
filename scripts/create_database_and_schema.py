import pyodbc
import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

driver_name = os.getenv("DRIVER_NAME")
schema_name = os.getenv("SCHEMA_NAME")
server_name = os.getenv("SERVER_NAME")
db_name = os.getenv("DB_NAME")

try:
    conn_str = f"DRIVER={driver_name};SERVER={server_name};Trusted_Connection=yes"
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        with open('schema/create_db_and_schema/create_database.sql') as create_db:
            sql = create_db.read()
            sql = sql.replace('{{database_name}}', db_name)
            conn.commit()
            cursor.execute(sql)
            conn.commit()
        print(f"Database '{db_name}' created.")
except Exception as e:
    print("Error when creating database")
    print(e)
    sys.exit()


time.sleep(1)
try:
    conn_str = f"DRIVER={driver_name};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes"
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        with open('schema/create_db_and_schema/create_schema.sql') as create_schema:
            sql = create_schema.read()
            sql = sql.replace('{{schema_name}}', schema_name)
            cursor.execute(sql)
            conn.commit()
        print(f"Schema '{schema_name}' created.")
except Exception as e:
    print("Error when creating schema")
    print(e)
