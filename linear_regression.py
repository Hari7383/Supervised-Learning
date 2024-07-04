# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_1zutWxHRWbAhPy0g9EGTqFwTxNjzdHo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error,r2_score

data=pd.read_csv("/content/Student_Marks.csv")
data.head()

data.isnull().sum()

x_train = data["time_study"].iloc[:80]
y_train = data["Marks"].iloc[:80]

len(data)

from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder

# Assuming y_train is continuous and needs to be converted to categorical labels
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)

# Apply SMOTE to handle class imbalance
smote = SMOTE()
x_train, y_train = smote.fit_resample(x_train, y_train_encoded)

x_test=data["time_study"].iloc[80:]
y_test=data["Marks"].iloc[80:]

lr=LinearRegression()
lr.fit(x.values.reshape(-1,1),y)

from sklearn.tree import DecisionTreeRegressor as DecisionTree
dt=DecisionTree()
dt.fit(x_train,y_train)

y_pred=lr.predict(x_test.values.reshape(-1,1))
print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred)*100)

lr.predict([[3]])

lr.coef_,lr.intercept_

import matplotlib.pyplot as plt
w = lr.coef_
b = lr.intercept_

def plot_line(x,w,b,y):
  plt.scatter(x,y)
  plt.plot(x,w*x+b,color='red')
  plt.show()

x_test=np.array(x_test)
plot_line(x_test,w,b,y_test)