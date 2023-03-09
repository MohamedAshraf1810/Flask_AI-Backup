# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time
import os

print("Enter Your Name")
name  = input()+"-001"

# Directory
directory = name

# Parent Directory path
parent_dir = "Voice_Samples_Training/"

# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path)
# Sampling frequency
freq = 44100

# Recording duration
duration = 5

counter=1
while counter <=5:
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    print("Recording Audio "+str(counter)+"...")
    print("Recording Start For 5 Seconds")
    sd.wait()
    write("Voice_Samples_Training/"+name+"/"+str(name+"_"+str(counter)), freq, recording)
    counter+=1

# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)