from flask import Flask, redirect, jsonify
import json
import os

app = Flask(__name__)

# Determine the absolute path of redirect.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REDIRECT_FILE = os.path.join(BASE_DIR, 'redirect.json')

@app.route('/')
def home():
    try:
        # Check if redirect.json exists
        if not os.path.exists(REDIRECT_FILE):
            return jsonify({"error": f"{REDIRECT_FILE} not found."}), 404

        # Read the redirect URL from the JSON file
        with open(REDIRECT_FILE, 'r') as f:
            data = json.load(f)

        # Check if 'original_url' exists in JSON
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
