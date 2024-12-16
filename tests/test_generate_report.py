import sqlite3
import pandas as pd
import pytest
from src.generate_report import generate_report

@pytest.fixture
def sample_db(tmp_path):
    db_path = tmp_path / 'test.db'
    conn = sqlite3.connect(db_path)

    customers = pd.DataFrame({
        'customer_id': [123, 124, 125],
        'customer_type': ['Member', 'Normal', 'Normal'],
        'gender': ['Male', 'Female', 'Female'],
        'city': ['Yangon', 'Naypyitaw', 'Mandalay']
    })
    products = pd.DataFrame({
        'product_id': [12, 13],
        'product_line': ['Electronics', 'Fashion'],
        'unit_price': [100.0, 50.0]
    })
    sales = pd.DataFrame({
        'invoice_id': [1, 2],
        'branch': ['A', 'B'],
        'customer_id': [123, 124],
        'product_id': [12, 13],
        'product_line': ['Electronics', 'Fashion'],
        'quantity': [2, 3],
        'total': [200.0, 150.0]
    })

    customers.to_sql('customers', conn, index=False, if_exists='replace')
    products.to_sql('products', conn, index=False, if_exists='replace')
    sales.to_sql('sales', conn, index=False, if_exists='replace')

    conn.close()
    return db_path

def test_generate_report(sample_db, tmp_path):
    output_csv = tmp_path / 'report.csv'

    generate_report(sample_db, output_csv)

    report_df = pd.read_csv(output_csv)
    assert len(report_df) > 0
    assert set(report_df.columns) == {
        'city', 'customer_type', 'product_line', 'total_sales', 'rank'
    }
