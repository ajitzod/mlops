# Evaluates model performance.

def evaluate_model(model, metrics):
    print("Model Metrics:")
    print(metrics)

## File: model/deployer.py
# Deploys model to Vertex AI.

from google.cloud import aiplatform

def deploy_model(model):
    aiplatform.init(project="fraud-detection-mlops", location="us-central1")

    # Save the model to a temp directory and upload to GCP bucket
    model_dir = "/tmp/fraud_model"
    model.save(model_dir)

    endpoint = aiplatform.Endpoint.create(
        display_name="fraud-detection-endpoint",
        model=model,
    )

    print(f"Model deployed to endpoint: {endpoint.name}")