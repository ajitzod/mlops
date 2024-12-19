Deployment Documentation

This document outlines the step-by-step process to deploy the fraud detection model on Google Cloud Vertex AI and enable end-to-end production-grade monitoring and prediction capabilities.

Prerequisites

Google Cloud Account: Ensure you have access to a Google Cloud account with billing enabled.

APIs Enabled:

Vertex AI API

Cloud Storage API

BigQuery API (if used for data storage)

IAM Roles:

Ensure your user/service account has roles:

Vertex AI Admin

Storage Admin

BigQuery Admin (if applicable)

Environment Setup:

Install Google Cloud SDK.

Authenticate using:

gcloud auth login
gcloud auth application-default login

Set the project:

gcloud config set project [PROJECT_ID]

Deployment Workflow

Step 1: Prepare Model Artifact

Train the Model:

Use the training pipeline in src/model/trainer.py.

Save the trained model locally or directly to a GCS bucket.

Export Model:

Save the trained model in a TensorFlow SavedModel format.

import tensorflow as tf
model.save('path_to_save_model')

Upload the model to a GCS bucket:

gsutil cp -r path_to_save_model gs://[BUCKET_NAME]/models/[MODEL_NAME]

Step 2: Deploy Model to Vertex AI

Create a Model Resource:

Use the following command to upload the model to Vertex AI:

gcloud ai models upload \
  --region=us-central1 \
  --display-name=[MODEL_NAME] \
  --artifact-uri=gs://[BUCKET_NAME]/models/[MODEL_NAME] \
  --container-image-uri=us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-11:latest

Deploy Model to Endpoint:

Create an endpoint:

gcloud ai endpoints create \
  --region=us-central1 \
  --display-name=[ENDPOINT_NAME]

Deploy the model:

gcloud ai endpoints deploy-model [ENDPOINT_ID] \
  --region=us-central1 \
  --model=[MODEL_ID] \
  --display-name=[DEPLOYMENT_NAME] \
  --machine-type=n1-standard-4

Step 3: Test the Deployed Model

Invoke Endpoint:

Use the endpoint for predictions by sending JSON input data:

from google.cloud import aiplatform

endpoint = aiplatform.Endpoint(endpoint_name="projects/[PROJECT_ID]/locations/us-central1/endpoints/[ENDPOINT_ID]")

response = endpoint.predict(instances=[INPUT_DATA])
print(response.predictions)

Validate Predictions:

Ensure the predictions align with expected outputs and debug if necessary.

Step 4: Enable Model Monitoring

Set Up Monitoring:

Enable drift and latency monitoring for the deployed model:

gcloud ai model-monitoring jobs create \
  --project=[PROJECT_ID] \
  --region=us-central1 \
  --display-name=[MONITOR_JOB_NAME] \
  --endpoint=[ENDPOINT_ID] \
  --input-data-schema="{schema JSON}" \
  --target-field=[TARGET_FIELD]

Configure Alerts:

Set up notifications for anomalies through Cloud Monitoring or Pub/Sub.

Step 5: Automate Pipeline

CI/CD Workflow:

Use the GitHub Actions YAML file located at .github/workflows/ci-cd.yaml.

Integrate with Vertex Pipelines:

Configure the pipeline to retrain, validate, and redeploy the model as needed.

Additional Notes

For custom Docker images, refer to infrastructure/docker/Dockerfile for building and pushing images to Google Container Registry.

Monitor logs in Vertex AI:

gcloud logging read "resource.type=ml_endpoint AND resource.labels.endpoint_id=[ENDPOINT_ID]"

Scale endpoint traffic dynamically using:

gcloud ai endpoints update [ENDPOINT_ID] --region=us-central1 --traffic-split=0=100

This deployment ensures a production-grade pipeline with reliable predictions, robust monitoring, and easy scalability.