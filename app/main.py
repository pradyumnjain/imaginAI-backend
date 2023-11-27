import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Flask API! reloaded again 3!"


@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "GET request successful"})


@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.get_json()
    return jsonify({"message": "POST request successful", "data": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
