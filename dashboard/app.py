from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("hyderabad_dish_compare_data.csv")


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    matches = []
    fallback_result = None
    min_price = None
    max_price = None

    dishes = sorted(df["dish"].unique())
    restaurants = sorted(df["restaurant"].unique())

    if request.method == "POST":

        dish = request.form["dish"]
        restaurant = request.form.get("restaurant", "All")
        min_price = int(request.form["min_price"])
        max_price = int(request.form["max_price"])

        filtered = df[df["dish"] == dish]
        if restaurant != "All":
            filtered = filtered[filtered["restaurant"] == restaurant]
        all_options = []

        for _, row in filtered.iterrows():

            swiggy = row["swiggy"]
            zomato = row["zomato"]

            # Choose cheaper platform
            prices = {"Swiggy": swiggy, "Zomato": zomato}
            platform = min(prices, key=prices.get)
            best_price = prices[platform]

            option_data = {
                "restaurant": row["restaurant"],
                "platform": platform,
                "price": best_price,
                "swiggy": swiggy,
                "zomato": zomato,
                "swiggy_url": f"https://www.swiggy.com/search?query={row['restaurant'].replace(' ', '+')}",
                "zomato_url": f"https://www.zomato.com/search?q={row['restaurant'].replace(' ', '+')}",
            }

            all_options.append(option_data)

            # Check budget range
            if min_price <= best_price <= max_price:
                matches.append(option_data)

        # Sort options for fallback checks
        all_options = sorted(all_options, key=lambda x: x["price"])

        if len(matches) > 0:
            result = matches[0]
        elif len(all_options) > 0:
            cheapest_price = all_options[0]["price"]
            
            if max_price < cheapest_price:
                # User's budget is too low -> return absolute cheapest
                fallback_result = all_options[0]
            else:
                # User's budget is too high (min_price > most expensive) 
                # -> return the option whose price is closest to min_price
                
                # Sort by absolute difference to min_price
                closest_to_min = min(all_options, key=lambda x: abs(x["price"] - min_price))
                fallback_result = closest_to_min

    return render_template(
        "index.html",
        dishes=dishes,
        restaurants=restaurants,
        result=result,
        matches=matches,
        fallback_result=fallback_result,
        min_price=min_price,
        max_price=max_price
    )


if __name__ == "__main__":
    app.run(debug=True)