# import statements
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:

file_path = 'data/2010SantaBarbaraCA.csv'
df = pd.read_csv(file_path)
print(df.head())


data = [go.Heatmap(x=df['DAY'], y=df['LST_TIME'], z=df['T_HR_AVG'].values.tolist(),
                   colorscale='RdBu')]

layout = go.Layout(title='Santa Barbara Temperatures')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
