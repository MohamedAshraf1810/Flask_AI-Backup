from flask import Flask , redirect,url_for,render_template , request , session,flash,g
from flask_sqlalchemy import SQLAlchemy
import os
from flask import jsonify
import base64
import PIL.Image as Image
from io import BytesIO
from flask_login import LoginManager
from pathlib import Path
import threading
import time
sem = threading.Semaphore()

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
    session.clear()
    return render_template('login.html')

# login Page
@app.route('/login')
def Login():
    session.clear()
    return render_template('login.html')

# Authenticate login
@app.route('/login_user' , methods=['post'])
def login_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter_by(username=username, password=password)
        check = [user for user in users]
        if check:
                session['username'] = check[0].username
                return redirect(url_for("faceAuth"))
        else:
            print("LOGIN FAILED!!!!!!")
            flash('* Invalid Username or password')
            return render_template('login.html')
    else:
        return render_template('login.html')




# login Page
@app.route('/faceAuth')
def faceAuth():
    if "username" in session:
        flash('Welcome ' + session["username"])
        print(session["username"])
        g.accVoice = True
        return render_template('faceAuth.html')
    else:
        g.accVoice = False
        print("Login First")
        return render_template('login.html')



# login Page
@app.route('/voiceAuth')
def voice():
    if "username" in session:
        print(session["username"])
        flash('Welcome ' + session["username"])
        return render_template('voiceAuth.html')
    else:
        print("User Not loged in")
    return render_template('login.html')




# Method That Save Image From base64 To png
@app.route('/uploadimage',methods=['POST'])
def uploadimage():
    if "username" in session:
        user_name = session["username"]
        global userAccss
        data = request.get_json() #Requist with all data
        img_data  = data['image'] # image
        prefix = 'data:image/png;base64,'
        cuttedbase64 = img_data[len(prefix):]
        png_recovered = base64.b64decode(cuttedbase64)
        input_folder = Path('face_Recognition_Utilities/SVC_Testimgs/Users_Photos/' + user_name +'/'+user_name +'.png')
        input_folder.parent.mkdir(exist_ok=True, parents=True)
        input_folder_path = str(input_folder)
        with open (input_folder_path,'wb') as f:
            f.write(png_recovered)
            # Call Python FaceRecognition Model
        print("importing Python File (MODEL)")
        print("userName is " , user_name)
        
        sem.acquire()
        from face_recognition_svm import FaceRec_Model
        print("(MODEL) Imported !!")
        userAccss = FaceRec_Model(user_name)
        print("userAccss :::" , userAccss)
        if userAccss == True:
            sem.release()
            return str(userAccss)
        else:
            sem.release()
            return str(userAccss)

if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.11')