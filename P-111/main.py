import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data],['responses'],show_hist = False)
fig.show()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print ('Mean is',mean)
print ('Standard deviation is',std_dev)