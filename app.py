# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/user/<username>")
def dynamic(username):
    return f"<h1>Welcome {username}</h1>"


if __name__ == '__main__':
    app.run(debug=True)

