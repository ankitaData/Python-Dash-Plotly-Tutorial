#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a DataFrame from  "flights" data
file_path = 'data/flights.csv'
df = pd.read_csv(file_path)
print(df.head())

# Define a data variable
data = [go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'].values.tolist(), colorscale='RdBu')]

# Define the layout
# layout = go.Layout(title='Flights',
#                    xaxis=dict(title='Year'),
#                    yaxis=dict(title='Month'),
#                    )

layout = go.Layout(title=dict(text='Flights',
                              x=0.5,  # Set x to 0.5 to center the title
                              font=dict(size=24, color='red')  # Increase font size, change the color
                              ),
                   xaxis=dict(title='Year'),
                   yaxis=dict(title='Month'))

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
