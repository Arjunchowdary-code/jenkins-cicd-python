from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="Jenkins CI/CD working!", build=os.getenv("BUILD_TAG", "local"))

@app.get("/health")
def health():
    return jsonify(status="ok")
