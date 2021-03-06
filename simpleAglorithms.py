

from dataAnalysis import getTrainData
from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors, datasets

X,y,dict=getTrainData()
print("input loaded!")

clfs=\
    [svm.SVC(),
    # NearestNeighbors(n_neighbors=7, algorithm='ball_tree'),
     neighbors.KNeighborsClassifier(15,weights='distance'),
     RandomForestClassifier(n_estimators=10)]

for clf in clfs:
    print(clf)
    scores = cross_val_score(clf, X, y)#,scoring="accuracy"
    print(scores.mean())

