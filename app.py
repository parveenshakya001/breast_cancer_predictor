from flask import Flask, render_template, request
import pandas as pd
from xgboost import XGBRegressor

app = Flask(__name__)

model = XGBRegressor()
model.load_model("agriculture_model.json")

df = pd.read_csv("Agriculture.csv")

# Remove invisible leading/trailing spaces that otherwise break exact matching.
TEXT_COLUMNS = ["State", "District", "Market", "Commodity", "Variety", "Grade"]
for column in TEXT_COLUMNS:
    df[column] = df[column].astype(str).str.strip()

# Keep original dataset order for model encoding.
state_map = {value: i for i, value in enumerate(df["State"].unique())}
district_map = {value: i for i, value in enumerate(df["District"].unique())}
market_map = {value: i for i, value in enumerate(df["Market"].unique())}
commodity_map = {value: i for i, value in enumerate(df["Commodity"].unique())}
variety_map = {value: i for i, value in enumerate(df["Variety"].unique())}
grade_map = {value: i for i, value in enumerate(df["Grade"].unique())}

# Complete dependency chain:
# State -> District -> Market -> Commodity -> Variety -> Grade
dependent_data = {}

for _, row in df.iterrows():
    state = row["State"]
    district = row["District"]
    market = row["Market"]
    commodity = row["Commodity"]
    variety = row["Variety"]
    grade = row["Grade"]

    dependent_data.setdefault(state, {})
    dependent_data[state].setdefault(district, {})
    dependent_data[state][district].setdefault(market, {})
    dependent_data[state][district][market].setdefault(commodity, {})
    dependent_data[state][district][market][commodity].setdefault(variety, [])

    grades = dependent_data[state][district][market][commodity][variety]
    if grade not in grades:
        grades.append(grade)

price_data = []

for _, row in df.iterrows():
    price_data.append({
        "state": row["State"],
        "district": row["District"],
        "market": row["Market"],
        "commodity": row["Commodity"],
        "variety": row["Variety"],
        "grade": row["Grade"],
        "min_price": float(row["Min_x0020_Price"]),
        "max_price": float(row["Max_x0020_Price"])
    })

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    form_data = {}

    if request.method == "POST":
        form_data = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in request.form.to_dict().items()
        }

        try:
            state = form_data["state"]
            district = form_data["district"]
            market = form_data["market"]
            commodity = form_data["commodity"]
            variety = form_data["variety"]
            grade = form_data["grade"]

            min_price = float(form_data["min_price"])
            max_price = float(form_data["max_price"])

            if min_price > max_price:
                raise ValueError("Minimum price cannot be greater than maximum price.")

            input_data = pd.DataFrame([{
                "State": state_map[state],
                "District": district_map[district],
                "Market": market_map[market],
                "Commodity": commodity_map[commodity],
                "Variety": variety_map[variety],
                "Grade": grade_map[grade],
                "Min_x0020_Price": min_price,
                "Max_x0020_Price": max_price
            }])

            prediction = float(model.predict(input_data)[0])

        except Exception as e:
            error = str(e)
            print("PREDICTION ERROR:", e)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        form_data=form_data,
        states=sorted(dependent_data.keys()),
        dependent_data=dependent_data,
        price_data=price_data
    )

if __name__ == "__main__":
    app.run(debug=True)
