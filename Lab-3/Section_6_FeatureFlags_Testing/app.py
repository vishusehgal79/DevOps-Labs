from flask import Flask, jsonify
import os

app = Flask(__name__)
FEATURE_ENABLED = os.getenv("FEATURE_FLAG", "true").lower() == "true"

@app.route("/")
def home():
    status = "ENABLED" if FEATURE_ENABLED else "DISABLED"
    return f'''
    <html>
    <head><title>DevOps Feature Flag Demo</title></head>
    <body>
        <h1>DevOps Feature Flag Application</h1>
        <h2 id="feature-status">New Feature: {status}</h2>
    </body>
    </html>
    '''

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
