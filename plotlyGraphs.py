import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('Happiness.csv')

fig = px.scatter(df, x = ' Social support ', y = ' Score ', title=' Social Support vs Happiness' , hover_name=" Country or region ")
fig.show()

fig = px.scatter(df, x = ' GDP per capita ', y = ' Score ', title=' GDP per capita vs Happiness ' , hover_data=[" Country or region "])
fig.show()

fig = px.scatter(df, x =  ' Perceptions of corruption', y = ' Score ', title=' Perceptions of corruption vs Happiness ' , hover_data=[" Country or region "])
fig.show()

fig = px.scatter(df, x =  ' Freedom to make life choices ', y = ' Score ', title=' Freedom to make life choices vs Happiness ' , hover_data=[" Country or region "])
fig.show()

fig = px.scatter(df, x =  ' Healthy life expectancy ', y = ' Score ', title='  Healthy life expectancy vs Happiness ' , hover_data=[" Country or region "])
fig.show()

fig = px.scatter(df, x =  ' Generosity ', y = ' Score ', title='  Generosity  vs Happiness ' , hover_data=[" Country or region "])
fig.show()