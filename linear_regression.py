# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u49EbOv9s59vWCRvHKeupbEYrwW3isoJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

data=pd.read_csv("/content/Linear Regression Dataset.csv")
data.head()

data.isnull().sum()

x_train = data["time_study"].iloc[:80]
y_train = data["Marks"].iloc[:80]

x_test=data["time_study"].iloc[80:]
y_test=data["Marks"].iloc[80:]

lr=LinearRegression()
lr.fit(x_test.values.reshape(-1,1),y_test)

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