from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
print(enc.n_values_)
#array([2, 3, 4])
print(enc.feature_indices_)
#array([0, 2, 5, 9])