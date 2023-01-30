# main.py

from flask import Flask
app = Flask(__name__)

@app.route("/") # base url = run index()
def index():
    return "Welcome!"

@app.route("/nnderaid")
def nnde():
    return "nnde!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)