# Shared helper functions.

def validate_data(data):
    if data.isnull().sum().sum() > 0:
        raise ValueError("Data contains null values")