from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/birthday")
def birthday():
    return "August 26th, 1979"

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    return num1 + num2
