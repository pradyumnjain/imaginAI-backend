import json
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
port = int(os.environ.get("PORT", 5000))


@app.route("/")
def hello():
    return "Hello, kanika from github !!!"


@app.route("/health", methods=["GET"])
def get_health():
    return jsonify({"status": "200"})


@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "GET request successful"})


@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.get_json()
    return jsonify({"message": "POST request successful", "data": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
