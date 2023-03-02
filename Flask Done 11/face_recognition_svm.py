# Train multiple images per person
# Find and recognize faces in an image using a SVC with scikit-learn

import face_recognition
from sklearn import svm
import os
import cv2
import pickle

def FaceRec_Model(username):
        
    try:
        sucessfulAuth = False
        # Get pk File
        with open('face_Recognition_Utilities/Dumbed_Model/Trained_Model/MAIN/'+ username +'_Other.pk', 'rb') as f:
            mypickle = pickle.load(f)
        # Load the test image with unknown faces into a numpy array
        test_image = face_recognition.load_image_file('face_Recognition_Utilities/SVC_Testimgs/Users_Photos/'+username+'/'+username+'.png')
        # Find all the faces in the test image using the default HOG-based model
        face_locations = face_recognition.face_locations(test_image)
        no = len(face_locations)
        print("Number of faces detected: ", no)
        # Predict all the faces in the test image using the trained classifier
        print("Found:")
        for i in range(no):
            test_image_enc = face_recognition.face_encodings(test_image)[i]
            print("image incoding is ",test_image_enc)
            propa_name = mypickle.predict_proba([test_image_enc])
            # Getting Model Accuracy
            max_acc = propa_name.max()*100
            name = mypickle.predict([test_image_enc]) 
            predictedName = name[0]
            if (max_acc < 90 or predictedName == 'other'):
                predictedName = 'UnKnown'
                print('The Predicted Person Is : ', predictedName)
                print("The Model Accuracy Is = " , round(max_acc,2) , "%")
                # sucessfulAuth = False
                return False
            else:
                print("The Predicted Person Is : " , predictedName)
                print("The Model Accuracy Is = " , round(max_acc,2) , "%")
                # sucessfulAuth = True
                return True 
        # Print Accuracy
        print("propa_name",propa_name)
    except Exception as e:
        print(e)

    return sucessfulAuth
