# Implements preprocessing steps for data.

import pandas as pd
from imblearn.over_sampling import SMOTE # type: ignore

def preprocess_data(train_data, test_data):
    # Example preprocessing: Handling class imbalance
    smote = SMOTE()
    X_train, y_train = train_data.drop('target', axis=1), train_data['target']
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    processed_train = pd.concat([X_resampled, y_resampled], axis=1)
    processed_test = test_data  # Assuming test data is already preprocessed

    return processed_train, processed_test
