from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app) 
CONFIG_FILE = "/workspaces/ai-data-center/configs/sample_metrics.json"


def load_metrics():
    """Loads server metrics from JSON file."""
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "Metrics file not found"}

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """API endpoint to return live server metrics."""
    return jsonify(load_metrics())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
