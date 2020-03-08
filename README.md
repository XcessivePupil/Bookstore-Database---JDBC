# Polynomial-Regression-to-Predict-Happiness

In this project, data is read in from the Happiness Index report found on Kaggle here:

https://www.kaggle.com/unsdsn/world-happiness#2019.csv

Whilst the happiness index is controversial and not meant to be interpreted as a science, its results are still interesting.

In particular the relationship of social support (close friends and family) on one's overall levels of happiness. The relationship appears to be exponential, thus the dataset made for a good opportunity to use Polynomial Regression, in order to model the curve.

As per the results of the of the survey, countries that ranked higher in the social support category appeared to have exponentially
increased levels of happiness.

In technical terms:

This project is written in Python and makes use of Matplotlib for data visualization, and Scikit Learn, for Linear and Polynomial Regression 
as well as training and testing the data.


BONUS

Whislt exploring the dataset, I also found a data visulation package called Plotly:

https://plot.ly/

Using plotly, I was able to easily and neatly graph all the datasets within the Happiness index.

One of Plotly's interesting features is the ability to label datapoints and have the label appear only when the user hovers their mouse over the point.

This allows one to interact with the graph and see exactly which countries represent each datapoint in the given graphs. 

The program is named: PlotlyGraphs.py 
