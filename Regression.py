# Load the boston data set from sklearn
import pandas as pd
from sklearn.datasets import load_boston
boston = load_boston()

print(boston.feature_names)
# ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO’ 'B' 'LSTAT’]
# Convert boston.data into a pandas data frame
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
# Add target housing prices to the bos data frame in a price column
bos['PRICE'] = boston.target
# drop the price column to get only the parameters as the X values.
X = bos.drop('PRICE', axis = 1)
# Use the least squares method as the way to estimate the coefficients.
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, bos.PRICE)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print ('Estimated coefficient:', lm.intercept_)
# Estimated coefficient: 36.4911032804
print ('Number of coefficients:', len(lm.coef_))
print ('Coefficients:', lm.coef_)
# Number of coefficients: 13