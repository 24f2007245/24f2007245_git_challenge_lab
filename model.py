from flask_sqlalchemy import SQLAlchemy
from app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db=SQLAlchemy(app)

class User(db.model):
    id = db.Column(db.Integer(), primary_key =True, autoincrement=True)
    user_name = db.Column(db.String(60), nullable =False)
    user_email = db.Column(db.String(130),unique =True, nullable=False)
    password= db.Column(db.String(200), nullable =False)  