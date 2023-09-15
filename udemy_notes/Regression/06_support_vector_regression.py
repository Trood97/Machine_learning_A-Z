

#feature scaling is a must for values way lower than the apex ones.

#feature scaling is not required for dependent variables with binary values.

#feature scaling standard scalar deviation is a game changer.

#y = y.reshape(len(y),1)  # (no.of rows, columns)

#StandarScalar ------ fit_transform

sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])).reshape(-1,1))
#inverse transform because values are in standard deviation, for the output they have to be transformed back.



