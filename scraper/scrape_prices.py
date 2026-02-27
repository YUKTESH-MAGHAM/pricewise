import pandas as pd
import random
import os

# make sure data folder exists
os.makedirs("data", exist_ok=True)

dishes = ["Burger","Pizza","Biryani","Pasta","Sandwich","Fried Rice"]

restaurants = [
    "FoodHub",
    "UrbanBites",
    "RoyalTaste",
    "SpiceKitchen",
    "FoodFactory",
    "TastyCorner"
]

data = []

for i in range(200):

    dish = random.choice(dishes)
    restaurant = random.choice(restaurants)

    base_price = random.randint(100, 400)

    # simulate platform price difference
    price_swiggy = base_price + random.randint(-20, 20)
    price_zomato = base_price + random.randint(-20, 20)

    data.append([
        dish,
        restaurant,
        price_swiggy,
        price_zomato
    ])

df = pd.DataFrame(data, columns=[
    "dish",
    "restaurant",
    "price_in_swiggy",
    "price_in_zomato"
])

df.to_csv("data/raw_data.csv", index=False)

print("Dataset created successfully")