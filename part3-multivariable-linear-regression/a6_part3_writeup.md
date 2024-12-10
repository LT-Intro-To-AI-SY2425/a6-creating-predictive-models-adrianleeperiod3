# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

My model's R^2 came out to 0.86, meaning that a general relationship between the regression and data does exist, but it is not very strong.

2. Is your model accurate? Why or why not?

My model is not very accurate for price guessing, with guesses typically ranging at 10-20% error from actual values, with rare guesses under 5% error and a few above 100% error.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

10 y.o. car ~ $9,300 
20 y.o. car ~ $2,200

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Due to the lack of a boundary for the function's domain, x values that extrapolate to infinity result in negative outputs, as they amplify factors that depreciate the car's value: occaisionally beyond the point of logical reason (resulting in negative predictions).