# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:33:02 2018

@author: GFS53
"""

#naive bayes classifier implementataion
#naive bayes is simple classfier for doing well when only small no of observations are available
#preliminaries 
from sklearn.datasets import load_iris
# load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

np.random.seed(0)
iris= load_iris()
data = pd.DataFrame(iris.data,columns=iris.feature_names)
#create out targert variables 
data["species"] = pd.Categorical.from_codes(iris.target,iris.target_names)
data[50:65]

test= pd.DataFrame()
#create some feature values for the single rows
test["sepal length (cm)"]=[5.5]
test["sepal width (cm)"]=[2.8]
test["petal length (cm)"]=[3.6]
test["petal width (cm)"]=[1.3]
test

#calculating count of each species
n_setosa=data["species"][data["species"]=="setosa"].count()
n_versicolor=data["species"][data["species"]=="versicolor"].count()
n_virginica=data["species"][data["species"]=="virginica"].count()
total=data["species"].count()
total

#calculating probability of each species
p_setosa=n_setosa/total
p_versicolor=n_versicolor/total
p_virginica=n_virginica/total

#calculating mean for each feature of each species
data_mean=data.groupby("species").mean()
data_mean

#calculating variance of each feature of each species
data_var=data.groupby("species").var()
data_var

#storing mean of each feature of each species
setosa_slen_mean=data_mean["sepal length (cm)"][data_mean.index=="setosa"].values[0]
print(setosa_slen_mean)
setosa_swid_mean=data_mean["sepal width (cm)"][data_mean.index=="setosa"].values[0]
print(setosa_swid_mean)
setosa_plen_mean=data_mean["petal length (cm)"][data_mean.index=="setosa"].values[0]
print(setosa_plen_mean)
setosa_pwid_mean=data_mean["petal width (cm)"][data_mean.index=="setosa"].values[0]
print(setosa_pwid_mean)

versi_slen_mean=data_mean["sepal length (cm)"][data_mean.index=="versicolor"].values[0]
print(versi_slen_mean)
versi_swid_mean=data_mean["sepal width (cm)"][data_mean.index=="versicolor"].values[0]
print(versi_swid_mean)
versi_plen_mean=data_mean["petal length (cm)"][data_mean.index=="versicolor"].values[0]
print(versi_plen_mean)
versi_pwid_mean=data_mean["petal width (cm)"][data_mean.index=="versicolor"].values[0]
print(versi_pwid_mean)

virgi_slen_mean=data_mean["sepal length (cm)"][data_mean.index=="virginica"].values[0]
print(virgi_slen_mean)
virgi_swid_mean=data_mean["sepal width (cm)"][data_mean.index=="virginica"].values[0]
print(virgi_swid_mean)
virgi_plen_mean=data_mean["petal length (cm)"][data_mean.index=="virginica"].values[0]
print(virgi_plen_mean)
virgi_pwid_mean=data_mean["petal width (cm)"][data_mean.index=="virginica"].values[0]
print(virgi_pwid_mean)

#storing variance for each feature of each species
setosa_slen_var=data_var["sepal length (cm)"][data_var.index=="setosa"].values[0]
print(setosa_slen_var)
setosa_swid_var=data_var["sepal width (cm)"][data_var.index=="setosa"].values[0]
print(setosa_swid_var)
setosa_plen_var=data_var["petal length (cm)"][data_var.index=="setosa"].values[0]
print(setosa_plen_var)
setosa_pwid_var=data_var["petal width (cm)"][data_var.index=="setosa"].values[0]
print(setosa_pwid_var)

versi_slen_var=data_var["sepal length (cm)"][data_var.index=="versicolor"].values[0]
print(versi_slen_var)
versi_swid_var=data_var["sepal width (cm)"][data_var.index=="versicolor"].values[0]
print(versi_swid_var)
versi_plen_var=data_var["petal length (cm)"][data_var.index=="versicolor"].values[0]
print(versi_plen_var)
versi_pwid_var=data_var["petal width (cm)"][data_var.index=="versicolor"].values[0]
print(versi_pwid_var)

virgi_slen_var=data_var["sepal length (cm)"][data_var.index=="virginica"].values[0]
print(virgi_slen_var)
virgi_swid_var=data_var["sepal width (cm)"][data_var.index=="virginica"].values[0]
print(virgi_swid_var)
virgi_plen_var=data_var["petal length (cm)"][data_var.index=="virginica"].values[0]
print(virgi_plen_var)
virgi_pwid_var=data_var["petal width (cm)"][data_var.index=="virginica"].values[0]
print(virgi_pwid_var)

#formula 
def p_x_given_y(x,mean_y,variance_y):
    #input the arguments into a prob. variance function
    p=1/(np.sqrt(2*np.pi*variance_y))*np.exp((-(x-mean_y)**2)/(2*variance_y))
    return p  

#test["sepal length (cm)"][0]
    
#finding the posterior of each species
tp_setosa=p_setosa*p_x_given_y(test["sepal length (cm)"][0],setosa_slen_mean,setosa_slen_var)*\
       p_x_given_y(test["sepal width (cm)"][0],setosa_swid_mean,setosa_swid_var)*\
       p_x_given_y(test["petal length (cm)"][0],setosa_plen_mean,setosa_plen_var)*\
        p_x_given_y(test["petal width (cm)"][0],setosa_pwid_mean,setosa_pwid_var)

print(tp_setosa)

tp_versicolor=p_versicolor*p_x_given_y(test["sepal length (cm)"][0],versi_slen_mean,versi_slen_var)*\
       p_x_given_y(test["sepal width (cm)"][0],versi_swid_mean,versi_swid_var)*\
       p_x_given_y(test["petal length (cm)"][0],versi_plen_mean,versi_plen_var)*\
        p_x_given_y(test["petal width (cm)"][0],versi_pwid_mean,versi_pwid_var)

print(tp_versicolor)

tp_virginica=p_virginica*p_x_given_y(test["sepal length (cm)"][0],virgi_slen_mean,virgi_slen_var)*\
       p_x_given_y(test["sepal width (cm)"][0],virgi_swid_mean,virgi_swid_var)*\
       p_x_given_y(test["petal length (cm)"][0],virgi_plen_mean,virgi_plen_var)*\
        p_x_given_y(test["petal width (cm)"][0],virgi_pwid_mean,virgi_pwid_var)

print(tp_virginica)
