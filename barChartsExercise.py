#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:

file_path = 'data/mocksurvey.csv'
df = pd.read_csv(file_path, index_col=0)
pd.set_option('display.max_columns', 6)
print(df.head())

# create traces using a list comprehension:
data = [go.Bar
        (y=df.index, x=df[response],
         name=response,
         orientation='h') for response in df.columns]

# create a layout, remember to set the barmode here

layout = go.Layout(title="Mock Survey", barmode='stack')

# create a fig from data & layout, and plot the fig.

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
