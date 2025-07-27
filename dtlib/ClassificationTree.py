import numpy as np
from .DNode import DNode as dnode

class ClassificationTree:
    # Binary Based Classification Tree

    def __init__(self,maxDepth=10):
        self.root = None
        self.maxDepth = maxDepth

    def split(self,X,y):
        nodes = []
        features = X.shape[1]

        for feature in range(features):
            nodes.append(dnode((X[:,feature],y),feature))

        return nodes


    def entropy(self,y):
        entropy = 1
        if len(y) != 0:
            p1 = len(y[y==1])/len(y)
            if p1 != 0 and p1 != 1:
                entropy = -p1 * np.log2(p1) - (1-p1) * np.log2(1-p1)
            else:
                entropy = 0

        return entropy

    def calculateIG(self,X,y):
        splits = [y[X==0],y[X==1]]

        w1 = len(splits[0])/len(y)
        w2 = len(splits[1])/len(y)

        wEntropy = w1 * self.entropy(splits[0]) + w2 * self.entropy(splits[0])

        rootEntropy = self.entropy(y)

        ig = rootEntropy - wEntropy

        return ig

    def buildTree(self,root,depth):
        isLeaf = False

        if depth > self.maxDepth:
            isLeaf = True


        if root.data[0].shape[0] < self.maxSplit:
            isLeaf = True

        if isLeaf:
            X,y = root.data
            rootPurity = len(y[y==1])/len(y)
            predClass = 0
            if rootPurity >= 0.5:
                predClass = 1

            return dnode(root.data,isleaf=True,predClass=predClass,_parent=root)

        rootX,rooty = root.data

        splitNode = self.split(rootX,rooty)

        maxNode = None
        maxIG = 0

        for node in splitNode:
            X,y = node.data
            ig = self.calculateIG(X,y)

            if ig > maxIG:
                maxIG = ig
                maxNode = node

        if maxNode is not None:
            maxNode.right = dnode((rootX[rootX[:,maxNode.ind]==0,:],rooty[rootX[:,maxNode.ind]==0]),_parent=root)
            maxNode.left = dnode((rootX[rootX[:,maxNode.ind]==1,:],rooty[rootX[:,maxNode.ind]==1]),_parent=root)
            root = maxNode

            root.right = self.buildTree(root.right,depth+1)
            root.left = self.buildTree(root.left,depth+1)
        else:
            X,y = root.data
            rootPurity = len(y[y==1])/len(y)
            predClass = 0
            if rootPurity >= 0.5:
                predClass = 1

            root = dnode(root.data,isleaf=True,predClass=predClass,_parent=root)

        return root







    def fit(self,X,y):
        self.root = dnode((X,y))

        self.root = self.buildTree(self.root,0)

    def predict(self,X):
        root = self.root

        while not root.isleaf:
            print(root.ind,root.isleaf)
            if X[root.ind] == 0:
                root = root.right
            else:
                root = root.left

        return root.predClass
