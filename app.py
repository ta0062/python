from flask import Flask, jsonify, request
import requests
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask app running successfully on EC2 with PM2!"

@app.route('/api/time')
def get_time():
    now = datetime.utcnow()
    return jsonify({"utc_time": now.strftime("%Y-%m-%d %H:%M:%S")})

@app.route('/api/random')
def random_numbers():
    """Return 5 random numbers generated using NumPy"""
    numbers = np.random.randint(1, 100, 5).tolist()
    return jsonify({"random_numbers": numbers})

@app.route('/api/data')
def sample_data():
    """Return sample DataFrame as JSON"""
    data = {
        "Name": ["Ali", "Sara", "John", "Fatima"],
        "Age": [24, 29, 35, 31],
        "City": ["Lahore", "Karachi", "London", "New York"]
    }
    df = pd.DataFrame(data)
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/external')
def external_api():
    """Fetch a random joke from a public API"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@app.route('/api/sum', methods=['POST'])
def calculate_sum():
    """Accept JSON body like {'numbers': [1,2,3]} and return sum"""
    data = request.get_json()
    numbers = data.get('numbers', [])
    total = sum(numbers)
    return jsonify({"sum": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

