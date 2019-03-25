# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 02:05:01 2019

@author: Aidin
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = pd.read_csv("Data/energydata.csv")

#%%
df['month'] = pd.DatetimeIndex(df['date']).month
df['dayofmonth'] = pd.DatetimeIndex(df['date']).days_in_month
df['dayofweek'] = pd.DatetimeIndex(df['date']).dayofweek
df['hour'] = pd.DatetimeIndex(df['date']).hour
#%%
# barplot for months
fig, ax = plt.subplots()

bar_width = 0.35
opacity = 0.8
ind = range(1,6)
df_groupby_month = (df.groupby(['month']).sum())
rects1 = plt.bar(ind,df_groupby_month['Appliances'], bar_width,
alpha=opacity,
color='b',
label='Appliances')
 
rects2 = plt.bar(ind,df_groupby_month['lights'], bar_width,
alpha=opacity,
color='g',
bottom = df_groupby_month['Appliances'],
label='lights')
 
 
plt.xlabel('Months')
plt.ylabel('Energy Usage')
plt.legend()
 
plt.tight_layout()
plt.show()

#%%
# barplot for hours
fig, ax = plt.subplots()

bar_width = 0.35
opacity = 0.8
ind = range(1,25)
df_groupby_hour = (df.groupby(['hour']).sum())
rects1 = plt.bar(ind,df_groupby_hour['Appliances'], bar_width,
alpha=opacity,
color='b',
label='Appliances')
 
rects2 = plt.bar(ind,df_groupby_hour['lights'], bar_width,
alpha=opacity,
color='g',
bottom = df_groupby_hour['Appliances'],
label='lights')
 
 
plt.xlabel('Hours')
plt.ylabel('Energy Usage')
plt.legend()
 
plt.tight_layout()
plt.show()
#%%
# barplot for days of week
fig, ax = plt.subplots()

bar_width = 0.35
opacity = 0.8
ind = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
df_groupby_daysOfWeek = (df.groupby(['dayofweek']).sum())
rects1 = plt.bar(ind,df_groupby_daysOfWeek['Appliances'], bar_width,
alpha=opacity,
color='b',
label='Appliances')
 
rects2 = plt.bar(ind,df_groupby_daysOfWeek['lights'], bar_width,
alpha=opacity,
color='g',
bottom = df_groupby_daysOfWeek['Appliances'],
label='lights')
 
 
plt.xlabel('Day of Week')
plt.ylabel('Energy Usage')
plt.legend()
 
plt.tight_layout()
plt.show()

#%%
fig = plt.figure()
fig.add_subplot(2,1,1)
plt.hist(df['Appliances'], bins=60)
plt.ylabel('Frequency');

fig.add_subplot(2,1,2)
plt.boxplot(df['Appliances'], vert=False)
plt.xlabel('Energy Usage');
plt.tight_layout()
#%%

g = sns.pairplot(df, vars=['Appliances','lights','T1','RH_1','T2','RH_2','T3','RH_3'],kind="reg",plot_kws={'line_kws':{'color':'red'}})