import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os

# ===============================
# Load Data
# ===============================

df = pd.read_csv("data/final_data.csv")

# ===============================
# Define Features (X) and Target (y)
# ===============================

# We predict average market price
X = df[
    [
        "dish",
        "restaurant",
        "swiggy",
        "zomato",
        "price_gap",
        "cheaper_platform_encoded"
    ]
]

y = df["avg_price"]

# ===============================
# Train Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# Model Training
# ===============================

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ===============================
# Evaluation
# ===============================

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Model MAE:", mae)

# ===============================
# Save Model
# ===============================

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/pricing_model.pkl")

print("Model saved successfully")