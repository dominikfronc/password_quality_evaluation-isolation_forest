import plotly.graph_objects as go
import pandas as pd
import sys


df = pd.read_csv(sys.argv[1], sep=';')

password = df['password']
pcfg = df['pcfg']
if_1 = df['scaled1']
if_2 = df['scaled2']
zxcvbn = df['zxcvbn']

fig = go.Figure(data=go.Scatter(x=if_2, y=pcfg, mode='markers', text=password))
fig.update_yaxes(type="log")
fig.update_layout(xaxis_title="scale 2", yaxis_title="pcfg",)
fig.show()
