import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

""""
1. The relationship of Happiness vs Social Support can be found in the happiness index report by using the 2019 data:

https://www.kaggle.com/unsdsn/world-happiness#2019.csv

"""

df = pd.read_csv('Happiness.csv', delimiter = ",") #reading in the required data from the Happiness index of 2019

x = df.iloc[:, 4].values  # I've decided to work with the Social Support vs Happiness Columns with X being Social Support and Y being the happiness score
y = df.iloc[:, 2].values

x_train, x_test, y_train, y_test = train_test_split(x , y, test_size=0.2 , random_state = 0) #Splitting the training and testing data with a 80/20 split

# Train the Linear Regression model and plot a prediction

regressor = LinearRegression()
x_train=x_train.reshape(-1,1)
regressor.fit(x_train, y_train)
xx = np.linspace(0, 1.75, 5)
yy = regressor.predict(xx.reshape(xx.shape[0], 1))

# Set the degree of the Polynomial Regression model

quadratic_featurizer = PolynomialFeatures(degree=6)

# This preprocessor transforms an input data matrix into a new data matrix of a given degree

X_train_quadratic = quadratic_featurizer.fit_transform(x_train)
X_test_quadratic = quadratic_featurizer.transform(x_test.reshape(-1,1))

# Train and test the regressor_quadratic model

regressor_quadratic = LinearRegression()
regressor_quadratic.fit(X_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

# Plot the graph

plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
plt.title('Soical Support vs Happiness')
plt.xlabel('Social Support')
plt.ylabel('Happiness')
plt.grid(True)
plt.scatter(x_train, y_train)
plt.show() 