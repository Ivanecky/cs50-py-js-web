# Flask setup
from flask import Flask, render_template, request

app = Flask(__name__)

# Define main page route
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/april-anarchy-form.html', methods = ['POST', 'GET'])
def april_anarchy_form():
    email = request.form.get("email")
    return render_template("april-anarchy-form.html")