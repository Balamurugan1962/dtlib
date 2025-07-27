from dtlib import ClassificationTree,drawTree
import numpy as np


X_train = np.array([[1, 1, 1],
[0, 0, 1],
 [0, 1, 0],
 [1, 0, 1],
 [1, 1, 1],
 [1, 1, 0],
 [0, 0, 0],
 [1, 1, 0],
 [0, 1, 0],
 [0, 1, 0]])

y_train = np.array([1, 1, 0, 0, 1, 1, 0, 1, 0, 0])

model = ClassificationTree()
model.fit(X_train,y_train)
y_pred = np.zeros_like(y_train)

for i in range(X_train.shape[0]):
    y_pred[i] = (model.predict(X_train[i]))

print((y_pred==y_train).sum()/y_train.shape[0] * 100)

# print(model.root.right.right.predClass)
drawTree(model,["Ear Shape","Face Shape","Whiskers"])
