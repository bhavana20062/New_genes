from flask import Flask, jsonify, request
from flask_cors import CORS  # Allows frontend to call backend

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Mock market data
market_data = {
    "wheat": [
        {"market": "Market1", "price": 100},
        {"market": "Market2", "price": 120}
    ],
    "corn": [
        {"market": "Market1", "price": 90},
        {"market": "Market2", "price": 110}
    ],
    "apples": [
        {"market": "Market1", "price": 50},
        {"market": "Market2", "price": 70}
    ]
}

@app.route('/get_price', methods=['GET'])
def get_price():
    product_name = request.args.get('product', '').lower()
    if product_name not in market_data:
        return jsonify({"error": "Product not found"}), 404
    
    prices = market_data[product_name]
    best_price = max(prices, key=lambda x: x['price'])

    return jsonify({
        "prices": prices,
        "recommendation": best_price
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Ensure it runs on port 5000
