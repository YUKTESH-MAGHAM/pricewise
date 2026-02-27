import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# ===============================
# Load Data
# ===============================

df = pd.read_csv("data/final_data.csv")

X = df[
    [
        "dish",
        "restaurant",
        "price_in_swiggy",
        "price_in_zomato",
        "price_gap",
        "cheaper_platform_encoded"
    ]
]

y = df["avg_price"]

# ===============================
# Split Data
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# Load Trained Model
# ===============================

model = joblib.load("models/pricing_model.pkl")

# ===============================
# Predict
# ===============================

predictions = model.predict(X_test)

# ===============================
# Evaluation Metrics
# ===============================

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("===== MODEL EVALUATION =====")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)