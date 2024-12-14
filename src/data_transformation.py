# import pandas as pd
# from typing import Tuple

# def transform_data(input_file: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
#     """
#     Transforms the raw dataset into two dimension tables and one fact table.

#     Args:
#         input_file (str): Path to the raw CSV dataset.

#     Returns:
#         Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: Transformed dimension and fact tables.
#     """
#     # Load the dataset
#     data = pd.read_csv(input_file)

#     # Clean and preprocess data
#     data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
#     data = data.dropna()  # Drop rows with missing values

#     # Dimension: Customers
#     customers = data[['customer_id', 'customer_type', 'gender']].drop_duplicates().reset_index(drop=True)

#     # Dimension: Products
#     products = data[['product_line', 'unit_price']].drop_duplicates().reset_index(drop=True)

#     # Fact Table: Sales
#     sales = data[['invoice_id', 'branch', 'customer_id', 'product_line', 'quantity', 'total']]

#     # Add calculated fields (example)
#     sales['average_price_per_unit'] = sales['total'] / sales['quantity']

#     return customers, products, sales

# def save_transformed_data(customers: pd.DataFrame, products: pd.DataFrame, sales: pd.DataFrame, output_dir: str) -> None:
#     """
#     Saves the transformed data to CSV files.

#     Args:
#         customers (pd.DataFrame): Customers dimension table.
#         products (pd.DataFrame): Products dimension table.
#         sales (pd.DataFrame): Sales fact table.
#         output_dir (str): Directory to save the output CSV files.
#     """
#     customers.to_csv(f"{output_dir}/customers.csv", index=False)
#     products.to_csv(f"{output_dir}/products.csv", index=False)
#     sales.to_csv(f"{output_dir}/sales.csv", index=False)

# if __name__ == "__main__":
#     # Example usage
#     input_file = "path_to_downloaded_dataset/supermarket_sales.csv"
#     output_dir = "transformed_data"

#     # Transform data
#     customers_df, products_df, sales_df = transform_data(input_file)

#     # Save transformed data
#     save_transformed_data(customers_df, products_df, sales_df, output_dir)

import pandas as pd
from typing import Tuple

def transform_data(input_file: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Transforms the raw dataset into two dimension tables and one fact table.
    """
    data = pd.read_csv(input_file)
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
    data = data.dropna()

    # Dimension tables
    customers = data[['customer_id', 'customer_type', 'gender']].drop_duplicates().reset_index(drop=True)
    products = data[['product_line', 'unit_price']].drop_duplicates().reset_index(drop=True)

    # Fact table
    sales = data[['invoice_id', 'branch', 'customer_id', 'product_line', 'quantity', 'total']]
    sales['average_price_per_unit'] = sales['total'] / sales['quantity']

    return customers, products, sales
