# Fraud Detection on Vertex AI

This project leverages Google Cloud's Vertex AI to build, deploy, and monitor an end-to-end fraud detection model. The system is designed to identify fraudulent transactions with high accuracy while ensuring scalability and reliability.

## Project Overview
- **Platform**: Google Cloud Vertex AI
- **Model**: TensorFlow-based
- **Monitoring**: Vertex AI Model Monitoring for data drift and performance monitoring

## Folder Structure
```
fraud-detection-vertex-ai/
│
├── data/                                # For datasets
│   ├── raw/                             # Raw unprocessed data
│   ├── processed/                       # Preprocessed data
│   └── README.md                        # Data documentation
│
│
├── src/                                 # Core Python modules
│   ├── config/                          # Configuration files
│   │   ├── config.yaml                  # Centralized settings
│   ├── data/                            # Data handling modules
│   │   ├── loader.py                    # Read raw data
│   │   ├── preprocessing.py             # Preprocess raw data
│   ├── model/                           # Model training and inference
│   │   ├── trainer.py                   # Train the model
│   │   ├── evaluator.py                 # Evaluate the model
│   ├── monitoring/                      # Monitoring and drift detection
│   │   ├── drift_detection.py           # Detect model/data drift
│   │   └── performance_monitor.py       # Monito
│   ├── utils/                           # Utility scripts
│   │   ├── logger.py                    # Logging utilities
│   │   ├── gcp_client.py                # GCP interaction
│   │   └── helpers.py                   # Shared helper functions
│   └── main.py                          # Entry point for the pipeline
│
├── tests/                               #
│   ├── unit.py                          # Unit tests
│   ├── integration.py                   # Testing
│
├── requirements.txt                     # Python dependencies
├── setup.py                             # Package setup
├── README.md                            # Project documentation
├── .env                                 # Environment variables
├── .gitignore                           # Ignore temp/sensitive files

```

## Key Features
1. Data preprocessing using SMOTE and SMOTETomek.
2. TensorFlow model training with hyperparameter tuning.
3. Deployment on Vertex AI with model monitoring.

## How to Use
1. **Setup Environment**: Install dependencies using `pip install -r requirements.txt`.
2. **Run Pipeline**: Use the `src/main.py` script to execute the full pipeline.
3. **Deploy Model**: Follow deployment instructions in `docs/deployment.md`.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
