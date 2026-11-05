
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my AppSec laboratory!"

@app.route("/search")
def search():
    query = request.args.get("q", "")

    return render_template("search.html", query=query)

if __name__ == "__main__":
    app.run(debug=False)
