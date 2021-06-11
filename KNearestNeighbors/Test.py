import KNearestNeighbors
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris_data = pd.read_csv('KNearestNeighbors/Iris.csv')
iris_data = iris_data.drop(['Id'], axis=1)

y = iris_data['Species'].values.tolist()
X = iris_data.drop(['Species'], axis=1).values.tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y)

for k in range(1, 10):
    clf = KNearestNeighbors.KNearestNeighbors(k)
    clf.fit(X_train, y_train)
    predictions = clf.predict_list(X_test)
    print(accuracy_score(y_test, predictions))