import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Python"

if __name__ == "__main__":
    app.run(host='localhost', port=9123)