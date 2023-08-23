# import statements

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# data is always a LIST
data = [go.Scatter(x=random_x, y=random_y,
                   mode='markers',
                   marker=dict(size=10,
                               color='rgb(51,204,153)',
                               symbol='circle',
                               line={'width': 2}
                               ))]

# AXIS is always a dictionary
layout = go.Layout(title='First Scatter Plot',
                   xaxis={'title': 'MY X AXIS'},
                   yaxis=dict(title='MY Y AXIS'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')
