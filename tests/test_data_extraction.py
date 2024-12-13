import os
import pytest
from src.data_extraction import download_dataset

# Mock dataset identifier for testing
TEST_DATASET = "aungpyaeap/supermarket-sales"

# Reusable path for temporary test data
@pytest.fixture
def mock_download_path(tmp_path):
    return tmp_path

# Reusable function to simulate Kaggle API behavior
@pytest.fixture
def mock_kaggle_api(monkeypatch):
    def mock_download_files(dataset, path, unzip):
        # Simulate successful file creation for the mock dataset
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "mock_dataset.csv"), "w") as f:
            f.write("id,name,value\n1,Alice,100\n2,Bob,150")
    monkeypatch.setattr("kaggle.api.dataset_download_files", mock_download_files)

# Mock the existence of kaggle.json
@pytest.fixture
def mock_kaggle_json(monkeypatch):
    original_exists = os.path.exists

    def mock_exists(path):
        if path == os.path.expanduser("~/.kaggle/kaggle.json"):
            return True
        return original_exists(path)  # Call the original function for other paths

    monkeypatch.setattr("os.path.exists", mock_exists)

# Test successful dataset download
def test_download_dataset_success(mock_kaggle_api, mock_kaggle_json, mock_download_path):
    result = download_dataset(TEST_DATASET, str(mock_download_path))

    expected_file_path = os.path.join(str(mock_download_path), "mock_dataset.csv")
    assert result == expected_file_path, f"Expected {expected_file_path}, got {result}"
    assert os.path.exists(result), "Expected file does not exist."

# Test failure when kaggle.json is missing
def test_download_dataset_missing_kaggle_json(monkeypatch, mock_download_path):
    original_exists = os.path.exists

    def mock_exists(path):
        if path == os.path.expanduser("~/.kaggle/kaggle.json"):
            return False
        return original_exists(path)

    monkeypatch.setattr("os.path.exists", mock_exists)

    with pytest.raises(ValueError, match="Kaggle API credentials not found. Please place 'kaggle.json' in ~/.kaggle/."):
        download_dataset(TEST_DATASET, str(mock_download_path))

# Test failure when download path is invalid
def test_download_dataset_invalid_path(mock_kaggle_api, mock_kaggle_json):
    invalid_path = "/invalid/path/to/directory"

    with pytest.raises(Exception):
        download_dataset(TEST_DATASET, invalid_path)
