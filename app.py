from flask import Flask #external package
from datetime import datetime #sys lib

PORT = 3000
app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "Hello world"

@app.route("/time", methods=["GET"])
def time():
    return str(datetime.now())


app.run(host='0.0.0.0', port=PORT, debug=True)