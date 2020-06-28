#KNN Classifier

#Import the libraries needed

import itertools
import numpy as np
import matplotlib.ticker as NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing


#Imagine a telecommunications provider has segmented its customer base by service usage patterns, categorizing the customers into four groups.
#If demographic data can be used to predict group membership, the company can customize offers for individual prospective customers.
#It is a classification problem. That is, given the dataset, with predefined labels, we need to build a model to be used to predict class of a new or unknown case.

#The example focuses on using demographic data, such as region, age, and marital, to predict usage patterns.

#The target field, called custcat, has four possible values that correspond to the four customer groups, as follows: 1- Basic Service 2- E-Service 3- Plus Service 4- Total Service

#Our objective is to build a classifier, to predict the class of unknown cases. We will use a specific type of classification called K nearest neighbour.

df=pd.read_csv("teleCust1000t.csv")
print(df.head())

count1=df['custcat'].value_counts()
print(count1)

df.hist(column="income",bins=50)

X=df[['region','tenure','age','marital','address','income','ed','retire','gender','reside']].values.astype('float')

#Data Standardisation gives data with zero mean and unit variance

X=preprocessing.StandardScaler().fit(X).transform(X.astype('float'))
print(X[0:5])

y=df['custcat'].values
print(y[0:5])

#Out of Sample Accuracy is the percentage of correct predictions that the model makes on the data that the model has not been trained on.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)
print('Train Set:',X_train.shape,y_train.shape)
print('Test Set:',X_test.shape,y_test.shape)


        
from sklearn.neighbors import KNeighborsClassifier

#Training The Model and Prediction

k=4
neigh=KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
print(neigh)

yhat=neigh.predict(X_test)
yhat[0:5]

#Accuracy Evaluation (Accuracy Classification Score)

from sklearn import metrics
print("Train Set Accuracy:",metrics.accuracy_score(y_train,neigh.predict(X_train)))
print("Test Set Accuracy:",metrics.accuracy_score(y_test,yhat))


Ks=10
mean_acc=np.zeros((Ks-1))
std_acc=np.zeros((Ks-1))
ConfustionMx=[]

for n in range(1,Ks):
    neigh=KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
    yhat=neigh.predict(X_test)
    mean_acc[n-1]=metrics.accuracy_score(y_test,yhat)

    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])
    
print(mean_acc)

import matplotlib.pyplot as plt

plt.plot(range(1,Ks),mean_acc,'g')
plt.fill_between(range(1,Ks),mean_acc-1*std_acc,mean_acc+1*std_acc,alpha=0.10)
plt.legend(('Accuracy','+/- 3xstd'))
plt.ylabel('Accuracy')
plt.xlabel('Number of Neighbors(K)')
plt.tight_layout()
plt.show()

print("The best accuracy was with",mean_acc.max(),"with k=",mean_acc.argmax()+1)

k=1
neigh1=KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
print(neigh1)

yhat1=neigh1.predict(X_test)
yhat1[0:5]

#Accuracy Evaluation (Accuracy Classification Score)

from sklearn import metrics
tsa1=metrics.accuracy_score(y_train,neigh1.predict(X_train))
print(tsa1)
tsa2=metrics.accuracy_score(y_test,yhat1)
print(tsa2)

print("Train Set Accuracy: "+str(round((tsa1/(tsa1+tsa2))*100))+"%")
print("Test Set Accuracy: "+str(round((tsa2/(tsa1+tsa2))*100))+"%")













