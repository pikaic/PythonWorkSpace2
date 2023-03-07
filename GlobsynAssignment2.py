# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:55:24 2018

@author: GFS51
"""

import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns
hb = pd.read_csv("D:\\h1b_kaggle.csv",nrows=5000)
df=hb
df1=hb
df2=hb
sdf=df
sdf=(sdf.groupby(['WORKSITE'])) #GROUPING ALL THE DATA BY THE NAME OF THE WORKSITE
print(sdf.PREVAILING_WAGE.mean())  #FINDING MEAN FOR EACH WORKSITE
df[['city','state']] = df['WORKSITE'].str.split(',',expand=True)    #SPLITTING THE WORKSITE INTO TWO COLUMNS AS CITY AND STATE
df= (df.groupby(['state'])) #GROUPING ALL THE STATES TOGETHER
print(df.PREVAILING_WAGE.mean())
df1=round(df1.PREVAILING_WAGE,-3)   #ROUNDING THE WAGES VALUE TO THE NEAREST THOUSAND
print(df1)
#df2=df2[0:5000] NOT TAKING THE WHOLE DATA AS IT DOES NOT REVEAL THE PLOT PROPERLY
df2=df2[0:50]
sns.boxplot(x="FULL_TIME_POSITION",y="PREVAILING_WAGE",hue="FULL_TIME_POSITION",data=df2)   #BOXPLOT USING THE DATA IN df2 AND LABEL AS IN X AND Y 
