from flask import Flask, render_template
from model import db

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)

with app.app_context():
    db.create_all()

from routes import *

if __name__=='__main__':
    app.run(debug=True)