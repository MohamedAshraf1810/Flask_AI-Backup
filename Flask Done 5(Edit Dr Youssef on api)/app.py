from flask import Flask
from flask import render_template,session ,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask import jsonify
import base64
import PIL.Image as Image
from io import BytesIO
from face_recognition_svm import FaceRec_Model
current_dir = os.path.abspath(os.path.dirname(__file__))
username = None
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
# @app.route('/')
# def home():
#     return render_template('login.html')

@app.route('/')
def home():
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
    # from face_recognition_svm import FaceRec_Model
    print("(MODEL) Imported !!")
    userAccss = FaceRec_Model(username)
    print("userAccss :::" , userAccss)
    if userAccss == True:
        return jsonify(userAccss , "response1") 
    else:
        return jsonify(userAccss , "response2") 
    



if __name__ == '__main__':
    app.run(debug=True)