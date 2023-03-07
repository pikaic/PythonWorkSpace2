from sklearn.model_selection import LeaveOneOut
# LeaveOneOut (or LOO) simple cross-validation.
X = [1, 2, 3, 4]
loo = LeaveOneOut()
for train, test in loo.split(X):
    print("%s %s" % (train, test))