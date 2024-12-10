import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtraining, xtest, ytraining, ytest = train_test_split(x,y,test_size=.2)
#create linear regression model
model = LinearRegression().fit(xtraining,ytraining)
#Find and print the coefficients, intercept, and r squared values. 
coef = np.around(model.coef_,2)
const_intercept = round(model.intercept_,2)
rsq = round(model.score(x,y),2)
#Each should be rounded to two decimal places. 
print(f"Overall Linear Equation: y={coef[0]}x1 + {coef[1]}x2 + {const_intercept}")
print("R^2:", rsq)

#Loop through the data and print out the predicted prices and the 
#actual prices
prediction = model.predict(xtest)
prediction = np.around(prediction, 2)

print("***************")
print("Testing Results")

for i in range(len(xtest)):
    actual_value = ytest[i]
    predicted_value = prediction[i]
    x_input = xtest[i]
    error = round(100*abs((predicted_value-actual_value)/actual_value),2)
    print(f"Actual Price: {actual_value} Predicted Value: {predicted_value} Error: {error}%")

x1_fp = 89000
x2_fp = 10 
first_p = coef[0]*x1_fp + coef[1]*x2_fp + const_intercept 
print(f"Prediction for 10-year-old car with 89000 miles: {round(first_p,2)}")

x1_sp = 150000
x2_sp = 20 
second_p = coef[0]*x1_sp + coef[1]*x2_sp + const_intercept 
print(f"Prediction for 20 years old with 150000: {round(second_p,2)}")