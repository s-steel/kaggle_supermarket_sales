import os
from kaggle.api.kaggle_api_extended import KaggleApi
import logging

def setup_logger():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def data_extract(dataset: str, output_path: str) -> str:
    """
    Downloads a Kaggle dataset and returns the path to the extracted CSV file.
    """
    if not os.path.exists(os.path.expanduser("~/.kaggle/kaggle.json")):
        raise ValueError("Kaggle API credentials not found. Please place 'kaggle.json' in ~/.kaggle/.")
    
    if not os.path.exists(output_path):
        raise FileNotFoundError(f"Invalid download directory: {output_path}")
    
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=output_path, unzip=True)

    for file in os.listdir(output_path):
        if file.endswith(".csv"):
            return os.path.join(output_path, file)
    
    raise FileNotFoundError("CSV file not found in the downloaded dataset.")
