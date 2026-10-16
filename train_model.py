import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# Demonstration dataset.
# For a real project, replace this generated data with a genuine mobile-price CSV.
def create_demo_dataset(n=1000, random_state=42):
    rng = np.random.default_rng(random_state)
    battery_power = rng.integers(800, 6000, n)
    ram = rng.integers(512, 12001, n)
    px_height = rng.integers(480, 4001, n)
    px_width = rng.integers(640, 4001, n)
    int_memory = rng.integers(8, 257, n)
    mobile_wt = rng.integers(100, 251, n)

    # A synthetic relationship for demonstration only; this is not market pricing data.
    price = (
        500
        + battery_power * 0.18
        + ram * 1.65
        + (px_height * px_width) * 0.00012
        + int_memory * 5.5
        - mobile_wt * 1.8
        + rng.normal(0, 350, n)
    )
    price = np.maximum(price, 1500).round(0)

    return pd.DataFrame({
        "battery_power": battery_power,
        "ram": ram,
        "px_height": px_height,
        "px_width": px_width,
        "int_memory": int_memory,
        "mobile_wt": mobile_wt,
        "price": price
    })

df = create_demo_dataset()
df.to_csv("mobile_data.csv", index=False)

features = ["battery_power", "ram", "px_height", "px_width", "int_memory", "mobile_wt"]
X = df[features]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Model trained successfully!")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, predictions):.2f}")
print(f"R2 Score: {r2_score(y_test, predictions):.3f}")

joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
print("Demo dataset saved as mobile_data.csv")
