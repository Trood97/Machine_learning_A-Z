#feature scaling is not needed here, as it goes deep into the dataset

#training with DecisionTreeClassifier is simple as that
	from sklearn.tree import DecisionTreeRegressor

	regressor = DecisionTreeRegressor(random_state=0)
	regressor.fit(X, y) #that's it

#it takes in step , while predicting output


#for predicting the results
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#keep it simple as it is.

