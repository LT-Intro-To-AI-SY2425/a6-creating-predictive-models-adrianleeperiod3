# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

When StandardScaler and its transform are commented out, the system loses about 16% of its accuracy (69% accuracy alone), making its correct predictions a bit more likely than a coin toss.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

With Standard Scaler in the model is about 85% accurate, which is more reliable than expected. However, even with testing with small sample sizes, there is a good chance incorrect predictions will occur.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

While there does to seem to be better accuracy with standardized data points around zero, a strong correlatio for incorrect predictions doesn't seem to be discernable by simply observing cases. Without plotting these incorrect predictions en masse, it would be hard to draw an empirically backed conclusion.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

The model predicted that she would not purchase an SUV.