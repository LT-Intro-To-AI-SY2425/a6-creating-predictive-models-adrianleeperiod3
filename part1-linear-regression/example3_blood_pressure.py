import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
'''
Run the program and consider the following questions:
1. Look at the data points on the graph. Do age and blood pressure appear to have a linear relationship?
2. What does the value of r tell you about the relationship between age and blood pressure?
'''

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

x = x.reshape(-1, 1)

model = LinearRegression().fit(x,y)

coefficient = float(model.coef_[0])
y_intercept = float(model.intercept_)
rsq = model.score(x,y)

x_predict = 42
prediction = model.predict([[x_predict]])
print(f"Prediction when x is {x_predict}: {prediction}")

#sets the size of the graph
plt.figure(figsize=(5,4))

#labels axes and creates scatterplot
plt.xlabel("Age")
plt.ylabel("Systolic Blood Pressure")
plt.title("Systolic Blood Pressure by Age")
plt.scatter(x, y)
plt.plot(x, coefficient*x + y_intercept, c="r", label="Line of Best Fit")
print("Linear Equation of Best Fit: f(x) = ", round(coefficient,3), "x + ", round(y_intercept,3))
print("Pearson's Correlation: r = : ", math.sqrt(rsq))
plt.legend()
plt.show()
