import threading
import time
from datetime import datetime
import os
import sqlite3
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Sync:
    def __init__(self):
        self.last_synced_id_file = 'synced_id.txt'

    def get_last_synced_id(self):
        if os.path.exists(self.last_synced_id_file):
            with open(self.last_synced_id_file, 'r') as file:
                return int(file.read().strip())
        return 0

    def update_last_synced_id(self, last_id):
        with open(self.last_synced_id_file, 'w') as file:
            file.write(str(last_id))

    def get_new_records(self, last_id):
        conn = sqlite3.connect('user')
        query = "SELECT * FROM user WHERE BADGENUMBER > ?"
        df = pd.read_sql_query(query, conn, params=(last_id,))
        conn.close()
        return df

    def sync_to_snowflake(self, df):
        if df.empty:
            return False, 0

        df.columns = map(str.upper, df.columns)

        conn_snowflake = snowflake.connector.connect(
            user='BOIAN',
            password='Paladinat!2#snowflake',
            account='DUCMXHE-DZ06332',
            warehouse='COMPUTE_WH',
            database='DEMO_DB',
            schema='DEMO_SCHEMA'
        )

        create_table_query = """
        CREATE TABLE IF NOT EXISTS DEMO_USER (
            BADGENUMBER INTEGER,
            USERNAME STRING,
            EMAIL STRING,
            PAYRATE FLOAT
        )
        """
        conn_snowflake.cursor().execute(create_table_query)

        success, nchunks, nrows, _ = write_pandas(conn_snowflake, df, 'DEMO_USER')
        conn_snowflake.close()

        return success, nrows

class App(ttk.Window):
    def __init__(self, themename="darkly"):
        super().__init__(themename=themename)
        self.sync = Sync()
        self.running = False
        self.create_widgets()

    def create_widgets(self):
        self.title("Sync with Snowflake")
        self.geometry("400x200")

        self.label = ttk.Label(self, text="Auto-syncing every 3 seconds...")
        self.label.pack(pady=10)

        self.btn_start = ttk.Button(self, text="Start Sync", bootstyle="success", command=self.start_sync)
        self.btn_start.pack(pady=10)

        self.btn_stop = ttk.Button(self, text="Stop Sync", bootstyle="danger", command=self.stop_sync)
        self.btn_stop.pack()

        self.status = ttk.Label(self, text="")
        self.status.pack(pady=10)

    def start_sync(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.poll_for_updates, daemon=True).start()
            self.status.config(text="Sync started...")

    def stop_sync(self):
        self.running = False
        self.status.config(text="Sync stopped.")

    def poll_for_updates(self):
        while self.running:
            last_id = self.sync.get_last_synced_id()
            df = self.sync.get_new_records(last_id)
            if not df.empty:
                success, rows = self.sync.sync_to_snowflake(df)
                if success:
                    new_last_id = df['BADGENUMBER'].max()
                    self.sync.update_last_synced_id(new_last_id)
                    self.update_status(f"Uploaded {rows} new rows.")
                else:
                    self.update_status("Upload failed.")
            time.sleep(3)

    def update_status(self, message):
        self.after(0, lambda: self.status.config(text=message))

if __name__ == "__main__":
    app = App()
    app.mainloop()
