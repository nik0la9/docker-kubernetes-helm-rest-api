from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/champions")
def champions():
    return jsonify(message="Chelsea is Champions of the world")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)