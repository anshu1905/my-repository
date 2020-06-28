#Decision Trees
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("drug200.csv",delimiter=",")
print(data.head())
print("\n")
print(data.tail())
print("\n")

print("The length of the dataset is-> "+str(len(data))+".")
print("\n")
print("Enter the range in which you want to find the data")
print("\n")
a=int(input("Enter the lower limit-> "))
b=int(input("Enter the upper limit-> "))

#X as the Feature Matrix
#y as the response vector

X=data[['Age','Sex','BP','Cholesterol','Na_to_K']].values
print("\n")
print(X[a:b])

#Sex,BP and Cholestrol are categorical variables
#We can convert them into numerical variables pandas.get_dummies()

from sklearn import preprocessing

le_sex=preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1]=le_sex.transform(X[:,1])

le_BP=preprocessing.LabelEncoder()
le_BP.fit(['LOW','NORMAL','HIGH'])
X[:,2]=le_BP.transform(X[:,2])

le_Chol=preprocessing.LabelEncoder()
le_Chol.fit(['NORMAL','HIGH'])
X[:,3]=le_Chol.transform(X[:,3])
#Taking all the rows from column 1,2,3
print("\n")
print("This is the dataset after replacing categorical values with different levels starting form zero.")
print("\n")
print(X[a:b])

#The Drug is the response or the target variable hence y
y=data['Drug']

#Setting Up a Decision Tree

from sklearn.model_selection import train_test_split
X_trainset,X_testset,y_trainset,y_testset=train_test_split(X,y,test_size=0.3,random_state=3)
#70% training set and 30% testing set
print("\n")
print('Train Set:',X_trainset.shape,y_trainset.shape)
print("\n")
print('Test Set:',X_testset.shape,y_testset.shape)


#Modeling
drugTree=DecisionTreeClassifier(criterion="entropy",max_depth=4)
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
#To understand each parameter of the above functions
print("\n")
print("The decision Tree output is:",drugTree)
drugTree.fit(X_trainset,y_trainset)
predictTree=drugTree.predict(X_testset)
print("\n")
print("The predicted output is:",predictTree[0:5])
print("\n")
print("y_testset :\n",y_testset[0:5])

#Evaluation
from sklearn import metrics
import matplotlib.pyplot as plt
print("\n")
print("Decision Trees Accuracy-> "+str(metrics.accuracy_score(y_testset,predictTree)*100)+"%")


#Visualization

from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree

dot_data=StringIO()
filename="drugtree.png"
featureNames=data.columns[0:5]
targetNames=data["Drug"].unique().tolist()
out=tree.export_graphviz(drugTree,feature_names=featureNames,out_file=dot_data,class_names=np.unique(y_trainset),filled=True,special_characters=True,rotate=False)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png(filename)
img=mpimg.imread(filename)
plt.figure(figsize=(100,200))
plt.imshow(img,interpolations="nearest")


