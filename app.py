from flask import Flask #external package
from datetime import datetime #sys lib

PORT = 3000
app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "Hello world"

@app.route("/health", methods=["GET"])
def time():
    return "ok"


app.run(host='0.0.0.0', port=PORT, debug=True)
