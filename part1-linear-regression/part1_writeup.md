# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?

The r value itself is about 0.79. This means that while the data points do not all fall onto a linear line of best fit, a linear model would still do a relatively good job at predicting the general trend in data and where future points may fall.

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?

For a person that is 42 years old, the model predicts a blood pressure of numerical value: 136.5.

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?

Although I think that this model may at least make accurate guesses within an order of magnitude, there are definitely further intracacies that must be considered to create a better model. By simply plotting blood pressure vs. age, the spread on the data is too large to be certain that guesses are accurate beyond an order of magnitude. Some examples of other variables that may be considered to improve accuracy are things like a measure of physical activity, health history, and potential health hazards.