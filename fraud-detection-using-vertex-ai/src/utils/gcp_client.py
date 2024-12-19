# GCP-specific helper functions.

from google.cloud import storage

def get_gcp_client():
    client = storage.Client()
    return client