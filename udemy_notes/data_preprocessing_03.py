
#<editor-fold desc="dataset creation">
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
#</editor-fold>

#<editor-fold desc= "scikit imputer ">
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')      #from scikit class
imputer.fit(X[:, 1:3])                   #fitting the X dataset from : rows to 1st and 2nd column
X[:, 1:3] = imputer.transform(X[:, 1:3])         #to finally transform the data
#</editor-fold>

#<editor-fold desc = "one hot encoder">
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# transformer = [(encoder, transformer itself, the index of the column to be transformed)]
X = np.array(ct.fit_transform(X))         #transform the X dataset using ct object (predefined) , numpy array essential
#</editor-fold>

#<editor-fold desc= "Label encoder">
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = (le.fit_transform(Y))
#</editor-fold>

#Feature scaling cannot be done before training set because there is a possiblity of leakage of information to the test set.

#<editor-fold desc="splitting the dataset into the training and testing section">
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
# train_test_split function 4 items which is X train,test and y, Train,test,, test_size = 0.2(20%), and random state, randomly picks elements.
#</editor-fold>

#  normalization 0 to 1,       standardization -3 to +3(standard deviation)
#fit means to extract the values and transform applies the equation , its like staging and commiting

#<editor-fold desc="feature scaling">
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:,3:] = sc.fit_transform(X_train[:,3:])
X_test[:,3:] = sc.transform(X_test[:,3:])
#</editor-fold>