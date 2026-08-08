import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "rainfall": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "slope": [20, 25, 30, 35, 40, 45, 50, 55, 65, 75],
    "crack": [1, 1, 2, 2, 3, 4, 5, 6, 8, 10],
    "moisture": [20, 25, 30, 35, 40, 50, 60, 70, 80, 90],
    "temperature": [30, 30, 31, 31, 32, 32, 33, 33, 34, 35],
    "risk": [
        "LOW", "LOW", "LOW", "LOW", "MEDIUM",
        "MEDIUM", "MEDIUM", "HIGH", "HIGH", "HIGH"
    ]
}

df = pd.DataFrame(data)

X = df[["rainfall", "slope", "crack", "moisture", "temperature"]]
y = df["risk"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "rockfall_model.pkl")

print("Model trained successfully!")