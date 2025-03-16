from flask import Flask, redirect

app = Flask(__name__)

# Redirect Route
@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    # Here we map short codes to actual URLs
    url_mapping = {
        "abc123": "https://google.com",  # Update to google.com
        # Add more mappings here as needed
    }

    # Get the original URL based on the short code
    original_url = url_mapping.get(short_code)

    if original_url:
        # If a mapping exists, redirect to the original URL
        return redirect(original_url)
    else:
        # If no mapping exists, return a 404 error
        return "Short URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
