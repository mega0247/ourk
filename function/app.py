import os
import json
from flask import Flask, redirect, jsonify

app = Flask(__name__)

# Path to the JSON file inside the 'redirect' folder
REDIRECT_FILE = os.path.join(os.path.dirname(__file__), '..', 'redirect', 'redirect.json')

# Home Route
@app.route('/')
def home():
    try:
        # Check if the redirect.json file exists
        if not os.path.exists(REDIRECT_FILE):
            return jsonify({"error": f"{REDIRECT_FILE} not found."}), 404

        # Read the redirect URL from the JSON file
        with open(REDIRECT_FILE, 'r') as f:
            data = json.load(f)

        # Check if 'original_url' exists in the JSON file
        if 'original_url' not in data:
            return jsonify({"error": "'original_url' key missing in JSON."}), 400
        
        # Redirect to the URL specified in the JSON file
        return redirect(data['original_url'], code=302)

    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
