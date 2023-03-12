import os
print("Getting Audio Paths...")
# Training directory
train_dir = os.listdir('Voice_Samples_Training/')
# Loop through each person in the training directory
f = open("Voice_Samples_Training_Path.txt", "w+")
for person in train_dir:
    speaker = os.listdir("Voice_Samples_Training/" + person)
    # Loop through each training Voice for the current person
    for person_voice in speaker:
        print(person+'/'+person_voice)
        f.write(person+'/'+person_voice+"\n")
f.close()

def checkclose(file):
    if file.closed:
        print("")
    else:
        print("File Is Open Wait Until Closing...")
        file.close()
        checkclose(f)
# Check File
checkclose(f)

print("Audio Paths Goted successfully !!")