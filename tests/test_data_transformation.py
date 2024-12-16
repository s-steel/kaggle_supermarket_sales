import pandas as pd
import pytest
from src.data_transformation import transform_data

# Sample raw data for testing
RAW_DATA = """Invoice ID,City,Branch,Customer Type,Gender,Product line,Unit price,Quantity,Total,Date,Payment
101,Boston,A,123,Member,Male,Electronics,100.0,2,200.0,1/10/2019,Credit card
102,New York,B,124,Normal,Female,Fashion,50.0,4,200.0,3/11/2019,Ewallet
103,Seattle,A,125,Member,Male,Fashion,60.0,3,180.0,1/25/2019,Cash
"""

@pytest.fixture
def raw_csv_file(tmp_path):
    # Fixture to create a temporary raw CSV file for testing
    file_path = tmp_path / 'raw_data.csv'
    with open(file_path, 'w') as f:
        f.write(RAW_DATA)
    return file_path

def test_transform_data(raw_csv_file):
    customers, products, sales = transform_data(raw_csv_file)

    # Assert customers table
    assert len(customers) == 3
    assert set(customers.columns) == {'customer_id', 'customer_type', 'gender', 'city', 'branch'}

    # Assert products table
    assert len(products) == 3
    assert set(products.columns) == {'product_id', 'product_line', 'unit_price'}

    # Assert sales table
    assert len(sales) == 3
    assert set(sales.columns) == {
        'sales_id',
        'invoice_id',
        'customer_id',
        'product_id',
        'quantity',
        'date',
        'payment',
        'total',
        'average_price_per_unit',
    }

    assert sales['average_price_per_unit'].iloc[0] == 100.0
    assert not customers.empty, 'Customers dimension table should not be empty.'
    assert not products.empty, 'Products dimension table should not be empty.'
    assert not sales.empty, 'Sales fact table should not be empty.'
    assert 'customer_id' in customers.columns, 'Customers table missing customer_id column.'
    assert 'product_line' in products.columns, 'Products table missing product_line column.'
