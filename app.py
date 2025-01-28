from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Get Processor App URL from environment variable
PROCESSOR_URL = os.getenv("PROCESSOR_URL", "http://localhost:5000/data")  # Default to localhost for testing

@app.route('/')
def home():
    try:
        # Fetch data from the processor app
        response = requests.get(PROCESSOR_URL)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        messages = response.json()  # Parse the JSON response
    except requests.exceptions.RequestException as e:
        return f"Error fetching data from processor app: {e}", 500

    # Render the data in an HTML table
    return render_template('table.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
