from dtlib import ClassificationTree,drawTree
import numpy as np
import pandas as pd

df = pd.read_csv("datasets/mushrooms.csv")
X = df.drop('class',axis=1)

X = pd.get_dummies(X)
y = df['class']
y = (y == 'e')
columns = X.columns

X = np.array(X)
y = np.array(y)

X_train = X[:5000,:]
y_train = y[:5000]
X_test,y_test = X[5000:,:],y[5000:]
model = ClassificationTree()
model.fit(X_train,y_train)


y_pred = np.zeros_like(y_test)

for i in range(X_test.shape[0]):
    y_pred[i] = (model.predict(X_test[i]))

print((y_pred==y_test).sum()/y_test.shape[0] * 100)

drawTree(model,columns)
