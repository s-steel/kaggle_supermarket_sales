import sqlite3
import pandas as pd
import pytest
from src.data_load import load_to_sqlite

# Sample data for testing
CUSTOMERS_DATA = pd.DataFrame({
    'customer_id': [123, 124, 125],
    'customer_type': ['Member', 'Normal', 'Member'],
    'gender': ['Male', 'Female', 'Male'],
    'city': ['Yangon', 'Naypyitaw', 'Mandalay']
})

PRODUCTS_DATA = pd.DataFrame({
    'product_id': [12, 13, 14],
    'product_line': ['Electronics', 'Fashion', 'Health and beauty'],
    'unit_price': [100.0, 50.0, 23.0]
})

SALES_DATA = pd.DataFrame({
    'invoice_id': [101, 102, 103],
    'branch': ['Branch A', 'Branch B', 'Branch A'],
    'customer_id': [123, 124, 125],
    'product_id': [12, 13, 14],
    'product_line': ['Electronics', 'Fashion', 'Fashion'],
    'quantity': [2, 4, 3],
    'total': [200.0, 200.0, 180.0],
    'average_price_per_unit': [100.0, 50.0, 60.0]
})

@pytest.fixture
def sqlite_test_db(tmp_path):
    db_path = tmp_path / 'test.db'
    return db_path

def test_load_to_sqlite(sqlite_test_db):
    load_to_sqlite(CUSTOMERS_DATA, PRODUCTS_DATA, SALES_DATA, sqlite_test_db)

    conn = sqlite3.connect(sqlite_test_db)

    # Verify customers table
    customers = pd.read_sql_query('SELECT * FROM customers', conn)
    assert len(customers) == 3
    assert set(customers.columns) == {'customer_id', 'customer_type', 'gender', 'city'}

    # Verify products table
    products = pd.read_sql_query('SELECT * FROM products', conn)
    assert len(products) == 3
    assert set(products.columns) == {'product_line', 'unit_price', 'product_id'}

    # Verify sales table
    sales = pd.read_sql_query('SELECT * FROM sales', conn)
    assert len(sales) == 3
    assert set(sales.columns) == {
        'invoice_id',
        'branch',
        'customer_id',
        'product_id',
        'product_line',
        'quantity',
        'total',
        'average_price_per_unit',
    }

    conn.close()
