# main.py

from flask import Flask, render_template
# from flask import request

app = Flask(__name__)

@app.route("/") # base url = run index()
def home():
    return render_template('index.html')


CALCULATOR = """
<html>
    <head>
        <title>너나들이</title>
    </head>
    <body>
        <h1>Testing2</h1>
    </body>
</html>  
   


"""


@app.route("/nnde")
def nnde():
    return  CALCULATOR

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)