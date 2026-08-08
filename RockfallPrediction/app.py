from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("rockfall_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    rainfall = float(data["rainfall"])
    slope = float(data["slope"])
    crack = float(data["crack"])
    moisture = float(data["moisture"])
    temperature = float(data["temperature"])

    values = [[
        rainfall,
        slope,
        crack,
        moisture,
        temperature
    ]]

    prediction = model.predict(values)[0]
    probability = max(model.predict_proba(values)[0]) * 100

    return jsonify({
        "risk": prediction,
        "score": round(probability, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)