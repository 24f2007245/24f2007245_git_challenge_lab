from app import app
from model import*
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template('contact.html')
@app.route("/login")
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user= User.query.filter_by(user_email=email).first()
        if email and user.password==password:
            return render_template('contact.html', email=email)
        
        db.session.add(email=email,password=password)
        db.commit()
        return render_template('login.html')
    return render_template("login.html")
