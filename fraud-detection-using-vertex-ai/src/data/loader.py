# Handles loading datasets from GCP storage.

import pandas as pd
from google.cloud import storage
from src.utils.gcp_client import get_gcp_client

def load_data():
    client = get_gcp_client()
    bucket_name = "fraud-detection-data-bucket"

    # Paths to datasets
    train_path = "data/raw/fraud_train_preprocessed.csv"
    test_path = "data/raw/fraud_test_preprocessed.csv"

    # Load datasets
    train_data = pd.read_csv(client.download_blob_to_memory(bucket_name, train_path))
    test_data = pd.read_csv(client.download_blob_to_memory(bucket_name, test_path))

    return train_data, test_data
