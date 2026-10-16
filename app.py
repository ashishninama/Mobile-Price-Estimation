from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

FEATURES = ["battery_power", "ram", "px_height", "px_width", "int_memory", "mobile_wt"]

@app.route("/")
def home():
    return render_template("index.html", prediction=None, values={})

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = {
            "battery_power": float(request.form["battery_power"]),
            "ram": float(request.form["ram"]),
            "px_height": float(request.form["px_height"]),
            "px_width": float(request.form["px_width"]),
            "int_memory": float(request.form["int_memory"]),
            "mobile_wt": float(request.form["mobile_wt"]),
        }
        if any(v <= 0 for v in values.values()):
            return render_template("index.html", prediction=None, values=values,
                                   error="Please enter positive values for all features.")

        input_data = np.array([[values[f] for f in FEATURES]])
        price = max(0, float(model.predict(input_data)[0]))
        return render_template("index.html", prediction=round(price, 2), values=values)
    except (ValueError, KeyError):
        return render_template("index.html", prediction=None, values={},
                               error="Please enter valid numeric values.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
