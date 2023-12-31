#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
file_path = 'data/abalone.csv'
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', 9)
print(df.head())

# take two random samples of different sizes:
a = np.random.choice(df['rings'], 30, replace=False)
b = np.random.choice(df['rings'], 100, replace=False)

# create a data variable with two Box plots:

data = [go.Box(y=a, name='A'),
        go.Box(y=b, name='B')]

# add a layout

layout = go.Layout(title='Comparison of two samples taken from the same population')

# create a fig from data & layout, and plot the fig

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
