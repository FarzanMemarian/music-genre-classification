"""
GradientBoostingClassifier model

- Performs Gradient Boosting to classify the data

@author - Farzan Memarian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql.cursors
import sys, os
from   tqdm import tqdm
import time
sys.path.append( os.path.realpath("%s/.."%os.path.dirname(__file__)) )
from util import data_accessor_util
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV



# ----------------
#    models
# ----------------
from sklearn.ensemble import GradientBoostingClassifier

DEBUG = 1

# reading the data from sql table using the get_all_data method

X_train, y_train, train_le, X_test, y_test, test_le = data_accessor_util.get_all_data_sets()

classes = list(test_le.classes_)
# print test_le.inverse_transform([0, 1, 2, 3, 4, 5, 6])

# Converting data to numpy
(X_train, y_train, X_test, y_test) = data_accessor_util.convert_data_sets_to_numpy(X_train, y_train, X_test, y_test)

# method used
method = "GradientBoostingClassifier"

# iterate over classifiers
if DEBUG == 1: print "now performing: ", method
start = time.time()
clf = GradientBoostingClassifier(loss='deviance', learning_rate=0.1, n_estimators=100, subsample=1.0, \
                                 criterion='friedman_mse', min_samples_split=2, min_samples_leaf=1, \
                                 min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_split=1e-07, \
                                 init=None, random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, \
                                 warm_start=False, presort='auto')

# use a full grid over all parameters
# param_grid = {"max_depth": [3, 10, 20, None],
#               "learning_rate": [0.01, 0.1 , 0.2],
#               "n_estimators": [50, 200, 800]}

param_grid = {"max_depth": [3, 10]}

# run grid search
grid_search = GridSearchCV(clf, param_grid=param_grid)
grid_search.fit(X_train, y_train)

y_test_predict = grid_search.predict(X_test)
y_train_predict = grid_search.predict(X_train)
test_accuracy = accuracy_score(y_test, y_test_predict)
train_accuracy = accuracy_score(y_train, y_train_predict)

end = time.time()
elasped_time = end - start

file = open("GradientBoostingClassifier.txt","w")
file.close()
print "execution time of %s was %s seconds" %(method, elasped_time)
print "train accuracy of method %s is %s" % (method, train_accuracy)
print "test accuracy of method %s is %s" % (method, test_accuracy)
print classification_report(y_test, y_test_predict, target_names=classes)
entry1 = "train accuracy of " + method + " = " + str(train_accuracy) + "\n"
entry2 = "test accuracy of " + method + " = " + str(test_accuracy) + "\n\n\n"
myFile = open("GradientBoostingClassifier.txt","a")
myFile.write(entry1)
myFile.write(entry2)
print >> myFile, classification_report(y_test, y_test_predict, target_names=classes)
print >> myFile, "\n\n\n"
print >> myFile, "best params: ", grid_search.best_params_
myFile.close()
myFile.close()


















