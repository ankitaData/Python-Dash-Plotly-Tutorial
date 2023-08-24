# import statements

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# file paths
file_path = "data/nst-est2017-alldata.csv"
df = pd.read_csv(file_path)

df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True)
list_of_pop_columns = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_columns]
print(df2)

data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode='lines',
                   name=name) for name in df2.index]

pyo.plot(data)

