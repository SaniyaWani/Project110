import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff
import random
import statistics
import math

df = pd.read_csv("Project110.csv")
a = df["reading_time"].tolist()

population_mean = statistics.mean(a)
print("maen =", population_mean)
pStd = statistics.stdev(a)
print("standardDeviation = ", pStd)
dataset=[]
for i in range(0,100):
  index=random.randint(0,len(a))
  value = a[index]
  dataset.append(value)
dataset = statistics.mean(a)
print("maen =",  dataset)
dataset = statistics.stdev(a)
print("standardDeviation = ",  dataset)  

# fig = ff.create_distplot([dataset],["average"])
# fig.show()
