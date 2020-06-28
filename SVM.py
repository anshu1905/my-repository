#Supported Vector Machine SVM
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data=pd.read_csv("cell_samples.csv")
print(data.head())

ax=data[data['Class']==4][0:50].plot(kind='scatter',x='Clump',y='UnifSize',color="blue",label="malignent");
data[data['Class']==2][0:50].plot(kind='scatter',x='Clump',y='UnifSize',color="green",label="benign",ax=ax);
plt.show()
plt.hist(data['Class'],color="red")
plt.show()

data=data[pd.to_numeric(data['BareNuc'],errors='coerce').notnull()]
data['BareNuc']=data['BareNuc'].astype('int')
data.dtypes

feature=data[['Clump','UnifShape','UnifSize','MargAdh','SingEpiSize','BareNuc','BlandChrom','NormNucl','Mit']]
X=np.asarray(feature)
print(X[0:5])

data['Class']=data['Class'].astype('int')
y=np.asarray(data['Class'])
print(y[0:5])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)
#80% training set and 20% testing set
print('Train Set:',X_train.shape,y_train.shape)
print("\n")
print('Test Set:',X_test.shape,y_test.shape)
print("\n")

#Supported Vector Machine (SVM) uses certain kernal functions for performing the processing .
#Mapping data to a higher dimensional space is called as  kernelling
#Kernel Functions are the mathematical functions that are used.

#1.Linear
#2.Polynomial
#3.Radial Basis Function
#4.Sigmoid

from sklearn import svm
clf=svm.SVC(kernel='rbf')
clf.fit(X_train,y_train)


clf1=svm.SVC(kernel='linear')
clf1.fit(X_train,y_train)


clf2=svm.SVC(kernel='poly')
clf2.fit(X_train,y_train)


clf3=svm.SVC(kernel='sigmoid')
clf3.fit(X_train,y_train)


yhat=clf.predict(X_test)
print("RBF->",yhat[0:5])


yhat1=clf1.predict(X_test)
print("Linear->",yhat1[0:5])

yhat2=clf2.predict(X_test)
print("Polynomial->",yhat2[0:5])

yhat3=clf3.predict(X_test)
print("Sigmoid->",yhat3[0:5])


from sklearn.metrics import classification_report,confusion_matrix
import itertools
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm,classes,
                          normalize=False,
                          title="Confusion Matrix",
                          cmap=plt.cm.Blues
                          ):
    if normalize:
        cm=cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
        print("Normalized Confusion Matrix.")
    else:
        print("Confusion Matrix without normalization.")
    print(cm)

    plt.imshow(cm,interpolation="nearest",cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks=np.arange(len(classes))
    plt.xticks(tick_marks,classes,rotation=45)
    plt.yticks(tick_marks,classes)


    fmt='.2f' if normalize else 'd'
    thresh=cm.max()/2.
    for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,format(cm[i,j],fmt),
                 horizontalalignment="center",
                 color="white" if (cm[i,j]> thresh) else "black")
    plt.tight_layout()
    plt.ylabel("True Label")
    plt.xlabel("Predicted Label")


cnf_matrix=confusion_matrix(y_test,yhat,labels=[2,4])
np.set_printoptions(precision=2)

plot_confusion_matrix(cnf_matrix,classes=['Benign(2)','Malignant(4)'],normalize=False,title="Confusion Matrix")
plt.show()
print(classification_report(y_test,yhat))
print("\n")

print("Lets test the accuracy")
from sklearn.metrics import f1_score
print("The f1 score is-> ",f1_score(y_test,yhat,average="weighted"))


from sklearn.metrics import jaccard_similarity_score
print("The jaccard similarity score is-> ",jaccard_similarity_score(y_test,yhat))


