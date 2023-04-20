import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

t = pd.read_csv('05_04_2023_Torpedo Moscow_players.xlsx - Main statistics.csv')
t = t.rename(columns={'Unnamed: 0':'No', 'Unnamed: 1':'Name'})

t['InStat Index']= t['InStat Index'].replace({'-': '1'}).astype(int)
t['Matches played'] = t['Matches played'].astype(int, errors = 'ignore')
t['Challenges won, %'] = t['Challenges won, %'].astype(int, errors = 'ignore')
t['Challenges'] = t['Challenges'].str.replace(',', '.').astype(float)
t['Ball interceptions'] = t['Ball interceptions'].replace('-', '1,0')
t['Ball interceptions'] = t['Ball interceptions'].str.replace(',', '.').astype(float)
t['Passes']=t['Passes'].str.replace(',', '.').astype(float)

fig = px.scatter(t, x="Matches played", y="Challenges", 
                 hover_name="Name",
                 color="InStat Index", size ="Passes", size_max = 45)
fig.show()
fig.write_html("file.html")
