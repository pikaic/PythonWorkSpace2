# Load the library with the iris dataset
from sklearn.datasets import load_iris

# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

# Set random seed
np.random.seed(0)

from sklearn import cross_validation
model = RandomForestClassifier(n_estimators=100)
# Simple K-Fold cross validation. 10 folds.
cv = cross_validation.KFold(len(train), n_folds=10, indices=False)
results = []
for traincv, testcv in cv:
    probas = model.fit(train[traincv], target[traincv]).predict_proba(train[testcv])
    results.append( Error_function )
# "Error_function" can be replaced by the error function used for analysis
# RepeatedKFold repeats K-Fold n times, producing different splits in each repetition.