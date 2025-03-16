from flask import Flask, redirect
import json

app = Flask(__name__)

# Load URL from a JSON file or define it directly
@app.route('/')
def home():
    with open('redirect.json', 'r') as f:
        data = json.load(f)
    return redirect(data['original_url'], code=302)

if __name__ == "__main__":
    app.run(debug=True)
