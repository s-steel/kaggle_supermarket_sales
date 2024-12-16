import pandas as pd
from typing import Tuple
import logging

def setup_logger():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def transform_data(input_file: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    # Transforms the raw dataset into two dimension tables(customers, products) and one fact table(sales).
    data = pd.read_csv(input_file)
    data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]
    data = data.dropna()

    customers = data[['city', 'customer_type', 'gender', 'branch']].drop_duplicates().reset_index(drop=True)
    customers['customer_id'] = customers.index + 1

    products = data[['product_line', 'unit_price']].drop_duplicates().reset_index(drop=True)
    products['product_id'] = products.index + 1

    sales = data[['invoice_id', 'quantity', 'total', 'date', 'payment']]
    sales = data.merge(customers, on=['gender', 'customer_type', 'city', 'branch'], how='left')
    sales = sales.merge(products, on=['product_line', 'unit_price'], how='left')
    sales['sales_id'] = sales.index + 1
    sales['average_price_per_unit'] = sales['total'] / sales['quantity']
    sales = sales.drop(columns=['product_line', 'unit_price', 'gender', 'customer_type', 'city', 'branch'])

    return customers, products, sales
