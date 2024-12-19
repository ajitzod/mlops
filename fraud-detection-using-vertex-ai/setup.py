from setuptools import setup, find_packages

setup(
    name="fraud_detection_vertex_ai",
    version="1.0.0",
    description="End-to-end fraud detection pipeline on Vertex AI",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "tensorflow",
        "google-cloud-aiplatform",
        "google-cloud-storage",
        "alibi-detect",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)