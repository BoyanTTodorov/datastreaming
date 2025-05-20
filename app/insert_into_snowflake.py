import sqlite3
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Local
sqlite_db = r'user'        
sqlite_table = 'user'       

# Details
snowflake_user = 'BOIAN'
snowflake_password = 'Paladinat!2#snowflake'
snowflake_account = 'DUCMXHE-DZ06332' 
snowflake_warehouse = 'COMPUTE_WH'
snowflake_database = 'DEMO_DB'
snowflake_schema = 'DEMO_SCHEMA'
snowflake_table = 'DEMO_USER'      

# Read from SQLite  
conn_sqlite = sqlite3.connect(sqlite_db)
df = pd.read_sql_query(f"SELECT * FROM {sqlite_table}", conn_sqlite)
print(df)

df.columns = map(str.upper, df.columns)

conn_sqlite.close()

# Connect to Snowflake 
conn_snowflake = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)
# model the data using dbt
# Create table in Snowflake
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {snowflake_table} (
    BADGENUMBER INTEGER,
    USERNAME STRING,
    EMAIL STRING,
    PAYRATE FLOAT
)
"""
conn_snowflake.cursor().execute(create_table_query)

# Upload data 
success, nchunks, nrows, _ = write_pandas(conn_snowflake, df, snowflake_table)

# Close connection
conn_snowflake.close()

print(f" Upload successful: {success}, Rows uploaded: {nrows}")


