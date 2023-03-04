from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    name = request.args.get("name")
    response = {"data":f"hello, {name} !"}
    return jsonify(response)