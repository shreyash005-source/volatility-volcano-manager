from flask import Flask, jsonify
from risk_engine import (
    generate_volatility,
    generate_exposure,
    calculate_risk
)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Volatility Volcano Manager API is running 🚀"
    })

@app.route("/market")
def market_volatility():
    volatility = generate_volatility()
    return jsonify({
        "volatility": volatility,
        "unit": "VIX-like index"
    })

@app.route("/risk")
def risk_score():
    volatility = generate_volatility()
    exposure = generate_exposure()
    risk = calculate_risk(volatility, exposure)

    return jsonify({
        "volatility": volatility,
        "exposure": exposure,
        "risk_score": risk
    })

if __name__ == "__main__":
    app.run(debug=True)
