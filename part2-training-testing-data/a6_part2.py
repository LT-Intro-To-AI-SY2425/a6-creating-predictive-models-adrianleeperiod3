import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import math

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

x = x.reshape(-1,1)
# Create your training and testing datasets:
xtrainer, xtest, ytrainer, ytest = train_test_split(x, y, test_size = .2)
# Use reshape to turn the x values into 2D arrays:


# Create the model
model = LinearRegression().fit(xtrainer,ytrainer)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coefficient = float(model.coef_[0])
y_intercept = float(model.intercept_)
rsq = model.score(x,y)

# Print out the linear equation and r squared value:
print("Linear Equation of Best Fit: f(x) = ", round(coefficient,3), "x + ", round(y_intercept,3))
print("Pearson's Correlation: r = : ", math.sqrt(rsq))
'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
xtest = xtest.reshape(-1,1)
# get the predicted y values for the xtest values - returns an array of the results
prediction = model.predict(xtest)
# round the value in the np array to 2 decimal places
prediction = np.around(prediction, 5)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = prediction[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print("x value:", float(x_coord[0]), "Predicted y value:", predicted_y, "Actual y value:", actual, "Percent Error:", round(100*abs((predicted_y-actual)/actual),2),"%")


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
#sets the size of the graph
plt.figure(figsize=(5,4))

#creates a scatter plot and labels the axes
plt.scatter(xtrainer,ytrainer, c="purple", label="Training Data")
plt.scatter(xtest, ytest, c="blue", label="Testing Data")

plt.scatter(xtest, prediction, c="red", label="Predictions")

plt.xlabel("Age (Years)")
plt.ylabel("Blood Pressure (mmHg)")
plt.title("Blood Pressure vs Age")
plt.plot(x, coefficient*x + y_intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()