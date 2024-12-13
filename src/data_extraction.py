import os
import kaggle
import logging

def setup_logger():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def download_dataset(dataset: str, download_path: str) -> str:
    """
    Downloads the Kaggle dataset to the specified directory.
    Args:
        dataset (str): Kaggle dataset identifier (e.g., 'aungpyaeap/supermarket-sales').
        download_path (str): Directory where the dataset will be downloaded.
    Returns:
        str: Path to the extracted dataset file.
    """
    try:
        # Ensure Kaggle API credentials are present
        if not os.path.exists(os.path.expanduser("~/.kaggle/kaggle.json")):
            raise ValueError("Kaggle API credentials not found. Please place 'kaggle.json' in ~/.kaggle/.")
        os.makedirs(download_path, exist_ok=True)

        # Download and unzip dataset
        logging.info(f"Downloading dataset '{dataset}' to '{download_path}'...")
        kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)
        logging.info(f"Dataset downloaded and extracted to '{download_path}'.")

        # Check for CSV files in the directory
        for file in os.listdir(download_path):
            if file.endswith('.csv'):
                return os.path.join(download_path, file)

        raise Exception("No CSV file found in the extracted dataset.")
    except ValueError as e:
        logging.error(e)
        raise
    except Exception as e:
        logging.error(f"An error occurred while downloading the dataset: {e}")
        raise

def main():
    setup_logger()

    DATASET = "aungpyaeap/supermarket-sales"
    DOWNLOAD_PATH = "./data"

    try:
        csv_file_path = download_dataset(DATASET, DOWNLOAD_PATH)
        logging.info(f"Dataset ready for processing: {csv_file_path}")
    except Exception as e:
        logging.error(f"Data extraction failed: {e}")

if __name__ == "__main__":
    main()