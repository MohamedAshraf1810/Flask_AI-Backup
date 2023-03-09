# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time
import os

# Parent Directory path
parent_dir = "Testing_Audio/"

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

print("press 1 To Confirm Audio Recording")
confirm = str(input())
if(confirm == '1'):
    counter=1
    while counter <=1:
        recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
        print("Recording Started Of Audio "+str(counter)+"For 5 Seconds ...")
        sd.wait()
        write("Testing_Audio/CurrentTestAudio.wav", freq, recording)
        counter+=1
else:
    print("Sound Recording Declined")

# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)