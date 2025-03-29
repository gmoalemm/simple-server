from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy database
items = {}

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")

    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
