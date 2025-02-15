from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Binance API URL for BTC/USDT price
BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

@app.route('/price', methods=['GET'])
def get_price():
    try:
        response = requests.get(BINANCE_URL)
        data = response.json()
        return jsonify({"symbol": data["symbol"], "price": data["price"]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
