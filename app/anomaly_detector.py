import joblib
import pandas as pd
from pathlib import Path

class AnomalyDetector:
    def __init__(self, model_path: str):
        """
        Initializes the detector by loading the pre-trained model.
        """
        # Build a path relative to this file to ensure it works from anywhere
        base_path = Path(__file__).parent.parent
        self.model = joblib.load(base_path / model_path)

    def predict(self, latency_ms: int) -> dict:
        """
        Predicts if a given latency value is an anomaly.
        """
        # The model expects a 2D array, so we create a DataFrame
        data = pd.DataFrame({'latency_ms': [latency_ms]})
        
        # model.predict returns -1 for anomalies and 1 for inliers (normal)
        prediction = self.model.predict(data)[0]
        
        is_anomaly = True if prediction == -1 else False
        
        return {
            "latency_ms": latency_ms,
            "is_anomaly": is_anomaly,
            "assessment": "Anomaly Detected" if is_anomaly else "Normal"
        }

# Instantiate the detector once to be imported by the main app
# This ensures the model is loaded only once on startup.
detector = AnomalyDetector(model_path="models/isolation_forest.joblib")