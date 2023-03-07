# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:11:19 2018

@author: USER
"""
#Here we have taken education as the parameter being predicted as salary gives an impractical application

from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import numpy as np
np.random.seed(0)

sal=pd.read_csv("D:\Coding\Python\Datafiles\salary_table.csv")
df=pd.DataFrame(sal)
print(df.head())
print(df.tail())

df1=df.salary
print(df1)

#df2=df[['experience','education','management']]
#print(df2)

df["is_train"]=np.random.uniform(0,1,len(df))<0.75
print(df.head())
print(df.tail())


#df["education"]=pd.factorize(df.education)[0]
#print(df)

df["management"]=pd.factorize(df.management)[0]
print(df)


train,test=df[df["is_train"]==True],df[df["is_train"]==False]

print("no. of observations in the training data",len(train))
print("no. of observations in the test data",len(test))


print(test)

y=pd.factorize(train["education"])[0]
print(y)

feature= df[["salary","experience","management"]]
#view features
clf= RandomForestClassifier(n_jobs=2,random_state=0)
print(clf)

print(feature)
features=feature.columns[0:3]
print(features)
clf.fit(train[features],y)
print(test)

print(clf.predict(test[features]))

clf.predict_proba(test[features])[0:10]

preds=df["education"][clf.predict(test[features])]
#print(df["salary"].tolist())
preds=preds[0:len(test)].tolist()		#converted to list
preds=np.array(preds)				#converted to array
print(preds)

#print(test["salary"].head())

print(pd.crosstab(test["education"],preds,rownames=["actual education"],colnames=["predicted education"]))

#view feature importance
#view a list of the features and their importance score
print(list(zip(train[features],clf.feature_importances_)))
print(test)