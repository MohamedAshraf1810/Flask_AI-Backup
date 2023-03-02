from flask import Flask
from flask import render_template,session ,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask import jsonify
import base64
import PIL.Image as Image
from io import BytesIO

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
    return render_template('home.html')

# login Page
@app.route('/login')
def Login():
    return render_template('login.html')



# Authenticate login
@app.route('/login_user' , methods=['post'])
def login_user():
    global username
    username = request.form.get('username')
    password = request.form.get('password')
    users = User.query.filter_by(username=username, password=password)
    check = [user for user in users]
    if check:
            session['user_id'] = check[0].id
            return render_template('faceAuth.html')
    else:
        print("LOGIN FAILED!!!!!!")
        return render_template('login.html',invalid_Login='* Invalid Username or password')



# Method That Save Image From base64 To png
@app.route('/uploadimage',methods=['POST'])
def uploadimage():
    global userAccss
    data = request.get_json() #Requist with all data
    img_data  = data['image'] # image
    prefix = 'data:image/png;base64,'
    cuttedbase64 = img_data[len(prefix):]
    png_recovered = base64.b64decode(cuttedbase64)
    with open ('face_Recognition_Utilities/SVC_Testimgs/Users_Photos/'+ username +'.png','wb') as f:
        f.write(png_recovered)
        # Call Python FaceRecognition Model
    print("importing Python File (MODEL)")
    from face_recognition_svm import FaceRec_Model
    print("(MODEL) Imported !!")
    userAccss = FaceRec_Model(username)
    print("userAccss :::" , userAccss)
    return (str(userAccss))
    
@app.route('/faceVerify', methods=['post'])
def faceVerify():
    if userAccss == True:
        return render_template('voiceAuth.html')
    else:
        return render_template('login.html',invalid_Login='*Your Last Login is Rejected!')
if __name__ == '__main__':
    app.run(debug=True)