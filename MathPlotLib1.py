# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:02:30 2017

@author: user
"""

import seaborn as sns
import pandas as pd
try:
    salary = pd.read_csv("./salary_table.csv")
except:
#url = 'https://raw.github.com/duchesnay/pylearn-doc/master/data/salary_table.csv'
    salary = pd.read_csv(url)
df = salary
sns.boxplot(x="education", y="salary", hue="management", data=salary, palette="PRGn")