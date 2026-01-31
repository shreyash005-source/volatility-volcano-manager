from flask import Flask, jsonify
import random

app = Flask(__name__)

# Home route (health check)
@app.route("/")
def home():
    return jsonify({
        "message": "Volatility Volcano Manager API is running 🚀"
    })

# Market volatility simulator
@app.route("/market")
def market_volatility():
    volatility = round(random.uniform(10, 80), 2)
    return jsonify({
        "volatility": volatility,
        "unit": "VIX-like index"
    })

# Risk calculation endpoint
@app.route("/risk")
def risk_score():
    volatility = random.uniform(10, 80)
    exposure = random.uniform(50, 150)

    risk = round((volatility * exposure) / 100, 2)

    return jsonify({
        "volatility": round(volatility, 2),
        "exposure": round(exposure, 2),
        "risk_score": risk
    })

if __name__ == "__main__":
    app.run(debug=True)
