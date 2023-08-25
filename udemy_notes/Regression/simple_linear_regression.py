

#<editor-fold desc ="importing the libraries">
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#</editor-fold>

Importing the dataset

splitting the dataset

Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#<editor-fold desc="visualizing the training dataset">
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
#</editor-fold>

#<editor-fold desc="visualizing the testing dataset">
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
#</editor-fold>

#bonus = https://www.superdatascience.com/pages/ml-regression-bonus-1 #



