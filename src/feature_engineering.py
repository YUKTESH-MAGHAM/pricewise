import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv("hyderabad_dish_compare_data.csv")

# ===============================
# Create Smart Pricing Features
# ===============================

# Average market price
df["avg_price"] = (
    df["swiggy"] + df["zomato"]
) / 2

# Price difference between platforms
df["price_gap"] = (
    df["swiggy"] - df["zomato"]
)

# Cheaper platform (HUMAN READABLE)
df["cheaper_platform"] = df.apply(
    lambda x: "Swiggy"
    if x["swiggy"] < x["zomato"]
    else "Zomato",
    axis=1
)

# ===============================
# Encode Text Columns for ML
# ===============================

le_dish = LabelEncoder()
le_restaurant = LabelEncoder()
le_platform = LabelEncoder()

# Encode dish and restaurant
df["dish"] = le_dish.fit_transform(df["dish"])
df["restaurant"] = le_restaurant.fit_transform(df["restaurant"])

# Create SEPARATE encoded column
df["cheaper_platform_encoded"] = le_platform.fit_transform(
    df["cheaper_platform"]
)

# ===============================
# Save Final Data
# ===============================
df.to_csv("data/final_data.csv", index=False)

print("Feature engineering completed successfully")