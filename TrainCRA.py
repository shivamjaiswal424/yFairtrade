import pickle
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data_set = pandas.read_csv('FTBorrower.csv')
X = data_set.iloc[:, [5, 6, 7, 8, 9, 10]]
y = data_set.iloc[:, [11]]

X = pandas.DataFrame(SimpleImputer().fit_transform(X))
y = pandas.DataFrame(SimpleImputer().fit_transform(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, shuffle=False)

scalar = StandardScaler().fit(X_train)
print(type(scalar))

with open('scalar.pkl', 'wb') as file:
    pickle.dump(scalar, file)

with open('scalar.pkl', 'rb') as file:
    nscalar = pickle.load(file)

print(type(nscalar))

X_train = pandas.DataFrame(nscalar.transform(X_train))
X_test = pandas.DataFrame(StandardScaler().fit_transform(X_test))

classifier = RandomForestClassifier(criterion='entropy').fit(X_train, y_train.values.ravel())

with open('model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

with open('model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

print(X_test.shape[1])

y_predict = pickle_model.predict(X_test)
