

#training polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)           #degree till 4   ,
X_poly = poly_reg.fit_transform(X)                 #X dataset
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)                #linear regression of polynomial features


#predicting salaries with linear regression model
lin_reg.predict([[6.5]])      #outer list - no. of rows,  inner list - no. of columns

#predicting with poly linear regression
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))         #just in the same format for predict of the regressor


