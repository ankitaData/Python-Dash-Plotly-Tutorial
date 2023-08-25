# import statements

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

file_path = 'data/mpg.csv'
df = pd.read_csv(file_path)
pd.set_option('display.max_columns', 9)
print(df.head())

data = [go.Scatter(x=df['horsepower'],
                  y=df['mpg'],
                  text=df['name'],
                  mode='markers',
                  marker=dict(size=df['weight']/300, color=df['cylinders'], showscale=True))]


layout = go.Layout(title="Bubble Chart: Horsepower vs MPG",
                   xaxis=dict(title='Horsepower'),
                   yaxis=dict(title='MPG'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
