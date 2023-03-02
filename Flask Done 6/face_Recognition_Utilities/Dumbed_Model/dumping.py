import face_recognition
from sklearn import svm
import os
import pickle

# Training the SVC classifier

# The training data would be all the face encodings from all the known images and the labels are their names
encodings = []
names = []

# Training directory
train_dir = os.listdir('face_Recognition_Utilities/train_dir/')

# Loop through each person in the training directory
for person in train_dir:
    pix = os.listdir("face_Recognition_Utilities/train_dir/" + person)

    # Loop through each training image for the current person
    for person_img in pix:
        print("Checking Train Images ..." , person_img)
        # Get the face encodings for the face in each image file
        face = face_recognition.load_image_file("face_Recognition_Utilities/train_dir/" + person + "/" + person_img)
        face_bounding_boxes = face_recognition.face_locations(face)

        # If training image contains exactly one face
        if len(face_bounding_boxes) == 1:
            face_enc = face_recognition.face_encodings(face)[0]
            # Add face encoding for current image with corresponding label (name) to the training data
            encodings.append(face_enc)
            names.append(person)
        else:
            print(person + "/" + person_img + " was skipped and can't be used for training")

# Create and train the SVC classifier
clf = svm.SVC(gamma='scale')
clf = svm.SVC(probability=True)
clf.fit(encodings,names)

with open ('face_Recognition_Utilities/Dumbed_Model/Trained_Model/MAIN/other2_Other.pk','wb') as f:
    pickle.dump(clf,f)
print("trainning Completed")
