# import statements

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

file_path = 'data/2018WinterOlympics.csv'
df = pd.read_csv(file_path)
print(df.head())

# data = [go.Bar(x=df['NOC'], y=df['Total'], name='Total')]

trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': '#FFD700'})

trace2 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker={'color': '#9EA0A1'})

trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})

data = [trace1, trace2, trace3]

layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
