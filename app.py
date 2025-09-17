from flask import Flask, render_template

app=Flask(__name__)

from model import *

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)