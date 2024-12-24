# Deployment Documentation

This document is designed to guide you step-by-step through deploying the fraud detection model to **Google Cloud Vertex AI**. It ensures seamless integration of model training, deployment, and monitoring for real-world fraud detection scenarios.

---

## Prerequisites

Before diving into deployment, make sure you’ve got the essentials covered:

1. **Google Cloud Setup**:
   - Active Google Cloud account with billing enabled.
   - Required APIs activated:
     - Vertex AI API
     - Cloud Storage API
     - BigQuery API (if using BigQuery for data storage).

2. **Permissions**:
   - Ensure your service account or user has these roles:
     - Vertex AI Admin
     - Storage Admin
     - BigQuery Admin (if applicable).

3. **Local Environment**:
   - Install Google Cloud SDK and authenticate:
     ```bash
     gcloud auth login
     gcloud auth application-default login
     ```
   - Configure your project:
     ```bash
     gcloud config set project [PROJECT_ID]
     ```

---

## Deployment Workflow

### Step 1: Model Preparation

1. **Train Your Model**:
   - Use the training script in `src/model/trainer.py` to train the model.
   - Ensure the trained model is saved in TensorFlow’s `SavedModel` format.

2. **Save the Model**:
   - Export the trained model:
     ```python
     import tensorflow as tf
     model.save('path_to_model')
     ```
   - Upload it to your Google Cloud Storage bucket:
     ```bash
     gsutil cp -r path_to_model gs://[BUCKET_NAME]/models/[MODEL_NAME]
     ```

---

### Step 2: Model Deployment to Vertex AI

1. **Upload the Model**:
   - Register the model with Vertex AI:
     ```bash
     gcloud ai models upload \
       --region=us-central1 \
       --display-name=[MODEL_NAME] \
       --artifact-uri=gs://[BUCKET_NAME]/models/[MODEL_NAME] \
       --container-image-uri=us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-11:latest
     ```

2. **Deploy the Model to an Endpoint**:
   - Create an endpoint:
     ```bash
     gcloud ai endpoints create \
       --region=us-central1 \
       --display-name=[ENDPOINT_NAME]
     ```
   - Deploy the model to the endpoint:
     ```bash
     gcloud ai endpoints deploy-model [ENDPOINT_ID] \
       --region=us-central1 \
       --model=[MODEL_ID] \
       --display-name=[DEPLOYMENT_NAME] \
       --machine-type=n1-standard-4
     ```

---

### Step 3: Validate the Deployment

1. **Test the Endpoint**:
   - Use the endpoint for predictions:
     ```python
     from google.cloud import aiplatform

     endpoint = aiplatform.Endpoint(endpoint_name="projects/[PROJECT_ID]/locations/us-central1/endpoints/[ENDPOINT_ID]")

     response = endpoint.predict(instances=[INPUT_DATA])
     print(response.predictions)
     ```

2. **Debugging Tips**:
   - Use Vertex AI logs to troubleshoot:
     ```bash
     gcloud logging read "resource.type=ml_endpoint AND resource.labels.endpoint_id=[ENDPOINT_ID]"
     ```

---

### Step 4: Monitor the Model

1. **Enable Monitoring**:
   - Set up data drift detection and latency monitoring:
     ```bash
     gcloud ai model-monitoring jobs create \
       --region=us-central1 \
       --endpoint=[ENDPOINT_ID] \
       --display-name=[MONITOR_JOB_NAME] \
       --input-data-schema="{schema JSON}" \
       --target-field=[TARGET_FIELD]
     ```

2. **Alerts and Notifications**:
   - Use Cloud Monitoring or Pub/Sub for anomaly alerts.

---

### Step 5: Automate the Pipeline

1. **CI/CD Integration**:
   - Leverage the CI/CD workflow in `.github/workflows/ci-cd.yaml` to automate deployments.

2. **Vertex Pipelines**:
   - Automate retraining, validation, and redeployment steps using Vertex Pipelines for a fully managed pipeline.

---

This document combines hands-on deployment steps with best practices, enabling you to manage a production-ready fraud detection pipeline confidently.
