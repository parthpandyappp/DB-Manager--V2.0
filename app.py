import os
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courseregistration.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    course = db.Column(db.String(100), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/auth')
def hello_world():
    return render_template("auth.html")

database={'nachi':'123','james':'aac','karthik':'asdsf','khushal': '1234' }

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']

    users = User.query.all()

    if name1 not in database:
	    return render_template('auth.html',info='Invalid Username')
    else:
        if database[name1]!=pwd:
            return render_template('auth.html',info='Invalid Username or Password')
        else:
	         return render_template('registered.html',users=users)

@app.route("/register" , methods = ["GET","POST"])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        email =request.form.get("email")
        course = request.form.get("Course")
        
        user = User(name=name,email= email, course = course)
        db.session.add(user)
        db.session.commit()
        return redirect("/auth")

@app.route("/logout", methods = ["POST"])
def logout():
    return redirect("/auth")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

