
# Anscombe quartet

All models cannot follow linear regression, we have to take a look at the dataset

Assumptions play a vital role

#categorical variables should be taken care of.

#if there are two dummy variables, always omit one dummy variable

#Training to the multiple linear regression on a test set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predicting the test results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

bonus link for multiple linear regresssion :
https: // www.superdatascience.com / pages / ml - regression - bonus - 2

#Making a single prediction (for example the profit of a startup with R&D Spend = 160000, Administration Spend = 130000, Marketing Spend = 300000 and State = 'California')

print(regressor.predict([[1, 0, 0, 160000, 130000, 300000]]))