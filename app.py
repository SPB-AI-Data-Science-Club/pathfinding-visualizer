"""
Pathfinding Visualizer
All algorithms run client-side; Flask only serves the page.
Kept as a Flask app for parity with the rest of the club's deployments.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5008)
