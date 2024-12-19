# Fraud Detection on Vertex AI

This project leverages Google Cloud's Vertex AI to build, deploy, and monitor an end-to-end fraud detection model. The system is designed to identify fraudulent transactions with high accuracy while ensuring scalability and reliability.

## Project Overview
- **Platform**: Google Cloud Vertex AI
- **Model**: TensorFlow-based
- **Monitoring**: Vertex AI Model Monitoring for data drift and performance monitoring

## Folder Structure
```
fraud-detection-vertex-ai/
├── .github/              # GitHub-specific workflows and templates
├── docs/                 # Project documentation
├── data/                 # Data storage
├── notebooks/            # Jupyter notebooks
├── src/                  # Core project code
├── tests/                # Automated tests
├── artifacts/            # Generated artifacts (models, logs, etc.)
├── infrastructure/       # Infrastructure setup (Docker, Terraform, etc.)
├── .env                  # Environment variables
├── .gitignore            # Ignored files for Git
├── LICENSE               # Licensing information
├── README.md             # Project overview
├── requirements.txt      # Python dependencies
├── setup.py              # Installation setup
└── Makefile              # Automation commands
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