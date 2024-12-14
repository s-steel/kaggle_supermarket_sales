import os
from src.data_extraction import data_extract
from src.data_transformation import transform_data
from src.data_loading import load_to_sqlite

def main():
    dataset = "aungpyaeap/supermarket-sales"
    download_path = "data"
    transformed_data_dir = "transformed_data"
    db_path = "supermarket_sales.db"

    os.makedirs(download_path, exist_ok=True)
    os.makedirs(transformed_data_dir, exist_ok=True)

    # Step 1: Extract
    csv_file = data_extract(dataset, download_path)
    print(f"Dataset downloaded: {csv_file}")

    # Step 2: Transform
    customers, products, sales = transform_data(csv_file)

    # Save transformed data as CSV files
    customers.to_csv(f"{transformed_data_dir}/customers.csv", index=False)
    products.to_csv(f"{transformed_data_dir}/products.csv", index=False)
    sales.to_csv(f"{transformed_data_dir}/sales.csv", index=False)
    print("Transformed data saved to CSV files.")

    # # Step 3: Load
    # load_to_sqlite(customers, products, sales, db_path)
    # print(f"Data loaded into SQLite database: {db_path}")

if __name__ == "__main__":
    main()
