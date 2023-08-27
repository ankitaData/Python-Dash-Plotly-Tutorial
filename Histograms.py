# import statements

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# creating a dataframe

file_path = 'data/mpg.csv'
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', 9)
print(df.head())

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=2))]
layout = go.Layout(title='Histogram')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)