import os
import pandas as pd
import numpy as np
import xlrd
#data in th excel format
data=pd.read_csv(r"ArogyaSetu1.csv")
#data frame
df=pd.DataFrame(data)
df['RECOVERY RATE(%)']=round((df['RECOVERED'].astype('float')/df['CONFIRMED'])*100)
df['DEATH RATE(%)']=round((df['DEATH'].astype('float')/df['CONFIRMED'])*100)
print(df.head(10))

print("\n")
print("\n")
#correlation and causation(relationship between cause and the effect)
from scipy import stats
pearson_coef,p_value=stats.pearsonr(df['CONFIRMED'].astype('float'),df['RECOVERED'].astype('float'))
print(pearson_coef)
print(p_value)
if(p_value<=0.001 and 0<pearson_coef<1):
    print('The confirmed cases and the recovery are stronlgy +ve related')
elif(p_value<=0.001 and -1<pearson_coef<0):
    print('The confirmed cases and the recovery are stronlgy -ve related')
else:
    print("No relation")

from scipy import stats
pearson_coef,p_value=stats.pearsonr(df['DEATH'].astype('float'),df['RECOVERED'].astype('float'))
print(pearson_coef)
print(p_value)
if(p_value<=0.001 and 0<pearson_coef<1):
    print(' The deaths and the recovery are stronlgy +ve related ')
elif(p_value<=0.001 and -1<pearson_coef<0):
    print('The deaths and the recovery are stronlgy -ve related')
else:
    print("No relation")

print("\n")
print("\n")
LABELS=df['STATE'].tolist()


import matplotlib.pyplot as plt

df['CONFIRMED'].plot(kind='bar',figsize=(12,8),color='blue',align='center')
plt.xticks(range(len(df['CONFIRMED'])),LABELS)
plt.title('CONFIRMED CASES IN EACH STATE')
plt.xlabel('STATE')
plt.ylabel('COUNT')
plt.show()

df['RECOVERED'].plot(kind='bar',figsize=(12,8),color='green',align='center')
plt.xticks(range(len(df['RECOVERED'])),LABELS)
plt.title('RECOVERED CASES IN EACH STATE')
plt.xlabel('STATE')
plt.ylabel('COUNT')
plt.show()

df['DEATH'].plot(kind='bar',figsize=(12,8),color='red',align='center')
plt.xticks(range(len(df['DEATH'])),LABELS)
plt.title('DEATHS IN EACH STATE')
plt.xlabel('STATE')
plt.ylabel('COUNT')
plt.show()

#LINEAR REGRESSION
#Y:RESPONSE VARIABLE AND X:PREDICTOR VARIABLE
#y=b0+b1*x
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
X=df[['CONFIRMED']]
Y=df[['RECOVERED']]
model1=lm.fit(X,Y)
print(model1)
Yhat=lm.predict(X)
print('The coeficient for our model is as follows',lm.coef_)
print('The intercept for our model is as follows',lm.intercept_)
choice=int(input('Enter the choice of data you want looking at the data set:'))
print('The recovery estimation for'+str(df['STATE'].loc[choice])+'is'+str(Yhat[choice]))#enter any value to predict the value of Y
#for finding R^2 error
print('The R sqaure error is :',lm.score(X,Y))

#for finding mean squared error that is MSE
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(df['RECOVERED'].astype('float'),Yhat)
print("The mean squared error is :",mse)


#MODEL EVALUATION WITH VISUALIZATION
import seaborn as sns
import matplotlib.pyplot as plt

#regression plot
plt.figure(figsize=(10,5))
sns.regplot(x=df['CONFIRMED'].astype('float'),y=df['RECOVERED'].astype('float'),data=df)
plt.ylim(0,)
plt.title('Regression Plot')
plt.show()

#residual plot
plt.figure(figsize=(10,5))
sns.residplot(df['CONFIRMED'].astype('float'),df['RECOVERED'].astype('float'),data=df)
plt.title('Residual Plot')
plt.show()

#distribution plot
plt.figure(figsize=(10,5))
ax1=sns.distplot(df['RECOVERED'].astype('float'),hist=False,color='red',label='Actual Value')
sns.distplot(Yhat,hist=False,color='blue',label='Predicted Value',ax=ax1)
plt.title('Distribution Plot')
plt.xlabel('CONFIRMED')
plt.ylabel('RECOVERED')
plt.show()


print("\n")
print("\n")

#MULTIPLE REGRESSION
#LINEAR REGRESSION
#Y:RESPONSE VARIABLE AND X:PREDICTOR VARIABLE
#y=b0+b1*x
from sklearn.linear_model import LinearRegression
lm1=LinearRegression()
Z=df[['CONFIRMED','DEATH']]
Y=df[['RECOVERED']]
model2=lm1.fit(Z,Y)
print(model2)
Yhat1=lm1.predict(Z)
print('The coeficient for our model is as follows',lm1.coef_)
print('The intercept for our model is as follows',lm1.intercept_)

choice1=int(input("Enter the state depending ont the data set:"))
print('The prediction for the recovery of '+str(df['STATE'].loc[choice1])+'is'+str(Yhat1[choice1]))


plt.figure(figsize=(10,5))
ax1=sns.distplot(df['RECOVERED'].astype('float'),hist=False,color='red',label='Actual Value')
sns.distplot(Yhat1,hist=False,color='blue',label='Predicted Value',ax=ax1)
plt.title('Distribution Plot')
plt.xlabel('CONFIRMED')
plt.ylabel('RECOVERED')
plt.show()

print("\n")






