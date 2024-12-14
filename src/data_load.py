import sqlite3
import pandas as pd

def load_to_sqlite(customers: pd.DataFrame, products: pd.DataFrame, sales: pd.DataFrame, db_path: str):
    """
    Loads dimension and fact tables into a SQLite database.
    """
    conn = sqlite3.connect(db_path)
    try:
        customers.to_sql("customers", conn, if_exists="replace", index=False)
        products.to_sql("products", conn, if_exists="replace", index=False)
        sales.to_sql("sales", conn, if_exists="replace", index=False)
    finally:
        conn.close()
