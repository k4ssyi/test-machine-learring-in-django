import pandas as pd
import numpy as np
from sklearn import datasets, model_selection, svm, metrics
from sklearn.externals import joblib

iris = datasets.load_iris()
iris_data = pd.DataFrame(data=iris.data)
iris_label = pd.Series(data=iris.target)

data_train, data_test, label_train, label_test = \
    model_selection.train_test_split(iris_data, iris_label)
print(len(data_train), len(data_test))

clf = svm.SVC()
clf.fit(data_train, label_train)
pre = clf.predict(data_test)
print(pre)

ac_score = metrics.accuracy_score(label_test, pre)
print(f'予測精度:{ac_score}')

joblib.dump(clf, 'iris.pkl')
