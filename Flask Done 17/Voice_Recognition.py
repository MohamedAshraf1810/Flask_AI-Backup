import os
import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from Voice_Recognition_Utilities import FeatureExtraction as VoiceFeatureExtraction
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time


def VoiceRec_Model(username):
    try:
        #path to training data
        source   = "Build_Set/"   
        modelpath = "Voice_Recognition_Utilities/Testing_Models/"
        #path to training data
        source   = "Voice_Recognition_Utilities/Testing_Audio/"+username+"/"
        #path where training speakers will be saved
        modelpath = "Voice_Recognition_Utilities/Trained_Speech_Models/"
        gmm_files = [os.path.join(modelpath,fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
        #Load the Gaussian gender Models
        models    = [cPickle.load(open(fname,'rb')) for fname in gmm_files]
        speakers  = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]
        error = 0
        total_sample = 0.0

        Name = username
        FileName = Name + ".wav"


        print(source+FileName)

        sr,audio = read(source + FileName)
        vector = VoiceFeatureExtraction.extract_features(audio,sr)
        log_likelihood = np.zeros(len(models)) 

        for i in range(len(models)):
            gmm    = models[i]  #checking with each model one by one
            print("gmm is = ",gmm)   #Like Mypickle in edited File 
            scores = np.array(gmm.score(vector))
            print("scores is " , scores,"\n\n\n")
            log_likelihood[i] = scores.sum()
        print("gmmfiles",gmm_files)
        print("log likelihood",log_likelihood)
        print("------------------")
        winner = np.argmax(log_likelihood)
        print ("\tThe person in the given audio sample is detected as - ", speakers[winner])
        time.sleep(1.0)
        if speakers[winner] == Name:
            print("Speaker Identified successfully")
            return True
        else:
            print("speaker Didn't Identified")
            return False

    except Exception as e:
        print(e)



