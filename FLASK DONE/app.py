from flask import Flask
from flask import render_template,session ,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os


current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(current_dir,"database.sqlite3")
db = SQLAlchemy()
db.init_app(app)

# Session
app.secret_key = os.urandom(34)

from model import *
db.init_app(app)
app.app_context().push()


# Home Page
@app.route('/')
def home():
    return render_template('login.html')

# Face Check Page
@app.route('/faceAuth')
def face():
    return render_template('faceAuth.html')

# Voice Check Page
@app.route('/voiceAuth')
def voice():
    return render_template('voiceAuth.html')

@app.route('/testpage')
def test():
    return render_template('testpage.html')


# Authenticate login
@app.route('/login_user' , methods=['post'])
def login_user():
    username = request.form.get('username')
    password = request.form.get('password')
    users = User.query.filter_by(username=username, password=password)
    check = [user for user in users]
    if check:
        if "AuthenticateByFace" in request.form:
            session['user_id'] = check[0].id
            return redirect('faceAuth')
        elif "AuthenticateByVoice" in request.form:
            session['user_id'] = check[0].id
            return redirect('voiceAuth')
    else:
        print("LOGIN FAILED!!!!!!")
        return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)