# Handles model training.

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(train_data, test_data):
    X_train, y_train = train_data.drop('target', axis=1), train_data['target']
    X_test, y_test = test_data.drop('target', axis=1), test_data['target']

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate on training set
    predictions = model.predict(X_test)
    metrics = classification_report(y_test, predictions)

    return model, metrics
