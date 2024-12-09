# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?

This model is able to test and assess its line of best fit on unseen data to determine whether its methods are effective or not. This is more effective than Part 1, which blindly takes all data into account when making the model: leaving no method of evaluation.

2. What does the R squared coefficient tell you about the model?

The R^2 value tells me whether or not the data is strongly correlated to the best fit line. A R^2 close to 1 resembles a near perfect fit while an R^2 of 0 represents complete incoherence between the line and data. 

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.

I would say that my model is relatively accurate most of the time. For a majority of test runs, the prediction's percent error was under 10% for tested values, with an occasional point being between 10-20% error. This low error allows us to feel confident that our model provides a decent ballpark estimate for blood pressure. However, it must be kept in mind that occasional outliers do exist, and that for a model predicting blood pressure with medical precision, a more intricate method needs to be taken. 
