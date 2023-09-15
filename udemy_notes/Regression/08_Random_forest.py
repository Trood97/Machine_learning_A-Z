#average of people's guesses to guess the no. of balls in a jar, this way we are much closer to the truth.

#statistical approach to a challenge like that...

Training with Random Forest
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=0)  , no. of trees, say guesses
regressor.fit(X, y)

