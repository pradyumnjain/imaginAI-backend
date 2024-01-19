import json
import os
import time

from bson.objectid import ObjectId
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
port = int(os.environ.get("PORT", 5000))
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
WASSABI_URI = os.getenv("WASSABI_URI")
MONGO_CLIENT = MongoClient(MONGO_URI)


@app.route("/health", methods=["GET"])
def get_health():
    return jsonify({"status": "200"})


@app.route("/home", methods=["GET"])
def get_data():
    DATABASE = MONGO_CLIENT["ImaginAI"]
    COLLECTION = DATABASE["stock_data"]

    # GET CURSOR AND SIZE FROM REQUEST
    cursor = request.form.get("cursor", type=int)
    size = request.form.get("size", type=int)

    if COLLECTION is None:
        return {"url_list": [], "next_cursor": 0}
    query = {}
    documents = list(COLLECTION.find(query).skip(cursor).limit(size))
    # url_list = [doc["image_url_list"][0].split("/")[-1] for doc in documents]
    url_list = [doc["image_url_list"] for doc in documents]
    next_cursor = cursor + len(url_list)
    return {"url_list":url_list,"next_cursor":next_cursor}


@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.get_json()
    return jsonify({"message": "POST request successful", "data": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
