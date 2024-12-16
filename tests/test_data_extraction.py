import os
import pytest
from src.data_extraction import data_extract

TEST_DATASET = 'aungpyaeap/supermarket-sales'

@pytest.fixture
def mock_download_path(tmp_path):
    return tmp_path

@pytest.fixture
def mock_kaggle_api(monkeypatch):
    def mock_download_files(dataset, path, unzip):
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'mock_dataset.csv'), 'w') as f:
            f.write('id,name,value\n1,Alice,100\n2,Bob,150')
    monkeypatch.setattr('kaggle.api.dataset_download_files', mock_download_files)

@pytest.fixture
def mock_kaggle_json(monkeypatch):
    original_exists = os.path.exists

    def mock_exists(path):
        if path == os.path.expanduser('~/.kaggle/kaggle.json'):
            return True
        return original_exists(path)  # Call the original function for other paths

    monkeypatch.setattr('os.path.exists', mock_exists)

# Test successful dataset download
def test_data_extract_success(mock_kaggle_api, mock_kaggle_json, mock_download_path):
    result = data_extract(TEST_DATASET, str(mock_download_path))

    expected_file_path = os.path.join(str(mock_download_path), 'supermarket_sales - Sheet1.csv')
    assert result == expected_file_path, f'Expected {expected_file_path}, got {result}'
    assert os.path.exists(result), 'Expected file does not exist.'

# Test failure when kaggle.json is missing
def test_data_extract_missing_kaggle_json(monkeypatch, mock_download_path):
    original_exists = os.path.exists

    def mock_exists(path):
        if path == os.path.expanduser('~/.kaggle/kaggle.json'):
            return False
        return original_exists(path)

    monkeypatch.setattr('os.path.exists', mock_exists)

    with pytest.raises(ValueError, match='Kaggle API credentials not found. Please place "kaggle.json" in ~/.kaggle/.'):
        data_extract(TEST_DATASET, str(mock_download_path))

# Test failure when download path is invalid
def test_data_extract_invalid_path(mock_kaggle_api, mock_kaggle_json):
    invalid_path = '/invalid/path/to/directory'

    with pytest.raises(Exception):
        data_extract(TEST_DATASET, invalid_path)
