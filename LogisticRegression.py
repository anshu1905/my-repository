#Logistic Regression

#Logistic Regression fits a special s-shaped curve by taking the linear regression and transforming numeric estimate into a probability with teh following function called the sigmoid/logistic  function.
#Used for dependent variables that are categorical values.

#(theta)^T*X is the regression result (sum of variables weighted by the coefficient)
#sigma((theta)^T*X) is the sigmoid or logistic function
#The objective of Logistic Regression algo is to find the best parameter for theta


#Customer Churn 

#A telecommunications company is concerned about the number of customers leaving their land-line business for cable competitors
#Use logistic Regression to find who and why they are leaving .

import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import matplotlib.pyplot as plt



data=pd.read_csv("ChurnData1.csv")
print(data.head())
print("\n")
print(data.tail())

data=data[['tenure','age','address','income','ed','employ','equip','callcard','wireless','churn']]
data['churn']=data['churn'].astype('int')
print(data.head())
print("\n")

X=np.asarray(data[['tenure','age','address','income','ed','employ','equip']])
y=np.asarray(data['churn'])

from sklearn import preprocessing
X=preprocessing.StandardScaler().fit(X).transform(X)
print(X[0:5])
print("\n")

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)
#80% training set and 20% testing set
print('Train Set:',X_train.shape,y_train.shape)
print("\n")
print('Test Set:',X_test.shape,y_test.shape)
print("\n")

#Modeling
#Regularization technique is used to solve the overfitting problem in Ml.
#C parameter indicates inverse of regularization strength which must be a positive float.
#Small value specify stronger regularization

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
#Can refer the parameters
LR=LogisticRegression(C=0.01,solver="liblinear").fit(X_train,y_train)
print(LR)
print("\n")
yhat=LR.predict(X_test)
print(yhat)
print("\n")
yhat_prob=LR.predict_proba(X_test)
print("\n")


#Evaluation

#1.Jaccard Index
#2.Confusion Matrix ,F1 Score
#Log Loss

#1.Jaccard Index-> |y intersection y^|/(|y|+|y^|-|y intersection y^|),y is the actual values and y^ is the predicted values
from sklearn.metrics import jaccard_similarity_score
print("The jaccard index will be-> ",jaccard_similarity_score(y_test,yhat))

#2.Confusion Matrix
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

print(confusion_matrix(y_test,yhat,labels=[1,0]))#within the range

cnf_matrix=confusion_matrix(y_test,yhat,labels=[1,0])
np.set_printoptions(precision=2)

plot_confusion_matrix(cnf_matrix,classes=['churn=1','churn=0'],normalize=False,title="Confusion Matrix")
plt.show()
print("\n")
print(classification_report(y_test,yhat))
print("\n")

#Precision->  True +ve/(True +ve + False +ve)
#Recall->  True +ve/(True +ve + False -ve)
#F1 Score is the harmonic avg. of both


#3.Log Loss
#Logorithimic Loss

from sklearn.metrics import log_loss
print(log_loss(y_test,yhat_prob))

