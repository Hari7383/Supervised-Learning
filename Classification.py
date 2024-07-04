# -*- coding: utf-8 -*-
"""Assesment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Subhash-K45/python/blob/main/Assesment.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv('Loan_Modelling.csv')

data.drop(columns=['ID'],inplace=True)

def data_preprocessing(data):
  X_train,X_test,y_train,y_test = train_test_split(data.drop(columns=['Personal_Loan']),data['Personal_Loan'],test_size=0.2,random_state=0)
  return X_train,X_test,y_train,y_test

def svm_model(X_train,X_test,y_train,y_test):
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)
  svc = SVC(kernel='linear',random_state=0)
  svc.fit(X_train,y_train)
  y_pred = svc.predict(X_test)
  return accuracy_score(y_test,y_pred)

def logistic_regression(X_train,X_test,y_train,y_test):
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)
  lr = LogisticRegression(random_state=0)
  lr.fit(X_train,y_train)
  y_pred = lr.predict(X_test)
  return accuracy_score(y_test,y_pred)

def random_forest(X_train,X_test,y_train,y_test):
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)
  rf = RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
  rf.fit(X_train,y_train)
  y_pred = rf.predict(X_test)
  return accuracy_score(y_test,y_pred)

def knn(X_train,X_test,y_train,y_test):
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)
  knn = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
  y_pred = knn.fit(X_train,y_train).predict(X_test)
  return accuracy_score(y_test,y_pred)

X_train,X_test,y_train,y_test = data_preprocessing(data)
l = []
l.append(svm_model(X_train,X_test,y_train,y_test)*100)
l.append(logistic_regression(X_train,X_test,y_train,y_test)*100)
l.append(random_forest(X_train,X_test,y_train,y_test)*100)
l.append(knn(X_train,X_test,y_train,y_test)*100)
result = pd.DataFrame(l,columns=['Accuracy'],index=['SVM','Logistic Regression','Random Forest','KNN'])

result