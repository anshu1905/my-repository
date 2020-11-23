import librosa
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


#mfcc: Mel Frequency Cepstral Coefficient, represents the short-term power spectrum of a sound
#chroma: Pertains to the 12 different pitch classes
#mel: Mel Spectrogram Frequency


def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
            result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}

observed_emotions=['calm', 'happy', 'fearful', 'disgust']

#feature extraction
def load_data(test_size=0.2):
    x=[]
    y=[]

    for file in glob.glob("C:\\Users\\Anshuman\\AppData\\Local\\Programs\\Python\\Python37\\Actor_*\\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
    #to check which one is true mfcc chroma mel
    #x and y are for feature and emotion respectively
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)



x_train,x_test,y_train,y_test=load_data(test_size=0.10)
print((x_train.shape[0], x_test.shape[0]))
print(f'Features extracted: {x_train.shape[1]}')
#split test and train data

model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)
#multi layer perception classfier

model.fit(x_train,y_train)
#fit the model

y_pred=model.predict(x_test)
# predict using test data

accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
#find the accuracy

print("Accuracy: {:.2f}%".format(accuracy*100))

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
data=confusion_matrix(y_test,y_pred)
import pandas as pd
df =pd.DataFrame(data)

plt.pcolor(df)
plt.show()

