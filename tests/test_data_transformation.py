# import pandas as pd
# import pytest
# from src.data_transformation import transform_data

# @pytest.fixture
# def mock_data():
#     data = {
#         "customer_id": [1, 2],
#         "customer_type": ["Member", "Normal"],
#         "gender": ["Male", "Female"],
#         "product_line": ["Health and beauty", "Electronic accessories"],
#         "unit_price": [74.69, 15.28],
#         "invoice_id": ["750-67-8428", "751-31-5824"],
#         "branch": ["A", "B"],
#         "quantity": [7, 5],
#         "total": [522.83, 76.4],
#     }
#     return pd.DataFrame(data)

# def test_transform_data(mock_data, tmp_path):
#     # Save mock data to a CSV
#     mock_file = tmp_path / "mock_data.csv"
#     mock_data.to_csv(mock_file, index=False)

#     # Call the transformation function
#     customers, products, sales = transform_data(str(mock_file))

#     # Assertions
#     assert not customers.empty, "Customers dimension table should not be empty."
#     assert not products.empty, "Products dimension table should not be empty."
#     assert not sales.empty, "Sales fact table should not be empty."

#     assert "customer_id" in customers.columns, "Customers table missing customer_id column."
#     assert "product_line" in products.columns, "Products table missing product_line column."

import pandas as pd
import pytest
from src.data_transformation import transform_data

# Sample raw data for testing
RAW_DATA = """Invoice ID,Branch,Customer ID,Customer Type,Gender,Product line,Unit price,Quantity,Total
101,Branch A,123,Member,Male,Electronics,100.0,2,200.0
102,Branch B,124,Normal,Female,Fashion,50.0,4,200.0
103,Branch A,125,Member,Male,Fashion,60.0,3,180.0
"""

@pytest.fixture
def raw_csv_file(tmp_path):
    """Fixture to create a temporary raw CSV file for testing."""
    file_path = tmp_path / "raw_data.csv"
    with open(file_path, "w") as f:
        f.write(RAW_DATA)
    return file_path

def test_transform_data(raw_csv_file):
    """Test the transformation of raw data into dimension and fact tables."""
    # Call the function
    customers, products, sales = transform_data(raw_csv_file)

    # Assert customers dimension table
    assert len(customers) == 3
    assert set(customers.columns) == {"customer_id", "customer_type", "gender"}

    # Assert products dimension table
    assert len(products) == 3
    assert set(products.columns) == {"product_line", "unit_price"}

    # Assert sales fact table
    assert len(sales) == 3
    assert set(sales.columns) == {
        "invoice_id",
        "branch",
        "customer_id",
        "product_line",
        "quantity",
        "total",
        "average_price_per_unit",
    }

    # Check a computed column
    assert sales["average_price_per_unit"].iloc[0] == 100.0
