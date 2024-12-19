# Monitors data drift.

def detect_drift(new_data, baseline_data):
    # Example drift detection logic
    drift_metric = abs(new_data.mean() - baseline_data.mean())
    print(f"Drift Metric: {drift_metric}")