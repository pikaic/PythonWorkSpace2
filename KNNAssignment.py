# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:16:04 2018

@author: GFS53
"""

#assignment 
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import neighbors
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline,FeatureUnion
from sklearn.model_selection import GridSearchCV

df=pd.read_csv("D:\h1b_kaggle1.csv",nrows=5000)
df1=(pd.cut(df['PREVAILING_WAGE'], 
                        bins=[0,50000,80000,1000000], 
                        labels=['LOW','MEDIUM','HIGH']))
df=(df[["SOC_NAME","JOB_TITLE","WORKSITE","FULL_TIME_POSITION"]])
df.head()

df["SOC_NAME"]=pd.factorize(df["SOC_NAME"])[0]
df["JOB_TITLE"]=pd.factorize(df["JOB_TITLE"])[0]
df["WORKSITE"]=pd.factorize(df["WORKSITE"])[0]
df["FULL_TIME_POSITION"]=pd.factorize(df["FULL_TIME_POSITION"])[0]

df['WAGE_CAT']=df1

df.head()

df["WAGE_CAT"]=pd.factorize(df["WAGE_CAT"])[0]
df.head()

train, test = train_test_split(df, test_size=0.25, random_state=30)
train["WAGE_CAT"].head()

clf= neighbors.KNeighborsClassifier(3,weights="uniform")
y=np.array(train["WAGE_CAT"].tolist())
trained_model=clf.fit(train,y)
print(trained_model)

trained_model.score(train,y)

x_test=test
df2=pd.DataFrame(trained_model.predict(x_test))
df2.head()

#standardise data
#create a standardizer
standardizer=StandardScaler()
#standardize features
#print(df.head())
X=train.values.tolist()
print(X)
X_std=standardizer.fit_transform(X)
#print(X_std)

#now fit a k nearest neighbor classifier
#let us fit a KNN classifier with 5 neighbors
knn=KNeighborsClassifier(n_neighbors=5,metric="euclidean",n_jobs=1).fit(X_std,y)

#create search space of possible values of k
# create a pipeline
pipe=Pipeline([("standardizer",standardizer),("knn",knn)])

#create a space for candidate values.we are providing the list of values for it.
search_space=[{"knn__n_neighbors":[1,2,3,4,5,6,7,8,9,10]}]

#search over possible values of k
#create grid search GridSerachCV implements a "fit" and a "score" method
clf=GridSearchCV(pipe,search_space,cv=2,verbose=0).fit(X_std,y)

#view k for best performing model 
#best neighbors size(k)
clf.best_estimator_.get_params()["knn__n_neighbors"]