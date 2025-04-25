import pyodbc
import os
import glob
import sys
from dotenv import load_dotenv

load_dotenv()

driver_name = os.getenv("DRIVER_NAME")
schema_name = os.getenv("SCHEMA_NAME")
server_name = os.getenv("SERVER_NAME")
db_name = os.getenv("DB_NAME")

create_table_files = glob.glob("schema/create_tables/*.sql")
conn_str = f"DRIVER={driver_name};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes"
try:
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        for file in create_table_files:
            try:
                with open(file) as supp:
                    sql = supp.read()
                    sql = sql.replace('{{schema_name}}', schema_name)
                    cursor.execute(sql)
                    conn.commit()
                    print(f"Executed {file} successfully.")
            except Exception as e:
                print(f"Error in file: {file}")
                print(e)
except Exception as e:
    print("Error when connecting or creating tables")
    print(e)
