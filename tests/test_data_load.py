import sqlite3
import pandas as pd
import pytest
from src.data_load import load_to_sqlite

# Sample data for testing
CUSTOMERS_DATA = pd.DataFrame({
    "customer_id": [123, 124, 125],
    "customer_type": ["Member", "Normal", "Member"],
    "gender": ["Male", "Female", "Male"]
})

PRODUCTS_DATA = pd.DataFrame({
    "product_line": ["Electronics", "Fashion"],
    "unit_price": [100.0, 50.0]
})

SALES_DATA = pd.DataFrame({
    "invoice_id": [101, 102, 103],
    "branch": ["Branch A", "Branch B", "Branch A"],
    "customer_id": [123, 124, 125],
    "product_line": ["Electronics", "Fashion", "Fashion"],
    "quantity": [2, 4, 3],
    "total": [200.0, 200.0, 180.0],
    "average_price_per_unit": [100.0, 50.0, 60.0]
})

@pytest.fixture
def sqlite_test_db(tmp_path):
    """Fixture to create a temporary SQLite database for testing."""
    db_path = tmp_path / "test.db"
    return db_path

# def test_load_to_sqlite(sqlite_test_db):
#     """Test loading data into SQLite database."""
#     # Call the function
#     load_to_sqlite(CUSTOMERS_DATA, PRODUCTS_DATA, SALES_DATA, sqlite_test_db)

#     # Verify data in the database
#     conn = sqlite3.connect(sqlite_test_db)

#     # Verify customers table
#     customers = pd.read_sql_query("SELECT * FROM customers", conn)
#     assert len(customers) == 3
#     assert set(customers.columns) == {"customer_id", "customer_type", "gender"}

#     # Verify products table
#     products = pd.read_sql_query("SELECT * FROM prod
