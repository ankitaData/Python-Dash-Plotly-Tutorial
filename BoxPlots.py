# import statements
import plotly.offline as pyo
import plotly.graph_objs as go

y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20, 20, 23, 24, 26, 27, 27, 28, 29, 33, 54]

# IQR = Q3 - Q1
# data points which fall below (Q1 – 1.5 IQR) or above (Q3 + 1.5 IQR) are outliers.

data = [go.Box(y=y,
               boxpoints='all',  # display the original data points
               jitter=0.3,  # spread them out so they all appear
               pointpos=-1.8)]  # offset them to the left of the box

# negative value of pointpos => offset to the left
# positive value of pointpos => offset to the right

pyo.plot(data)

# data = [go.Box(y=y, boxpoints='outliers' # display only outlying data points)]
# pyo.plot(data)
