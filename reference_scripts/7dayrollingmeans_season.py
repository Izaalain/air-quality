# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 07:44:57 2022

@author: Alexander Massa

This script allows you to plot two 7 day rolling means ontop of each other for a city
of interest
"""

#Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches




#Reading in data
#data = pd.read_csv('HourlyCalabar12112421.csv', usecols = [0,1,6,15,22,27], parse_dates=[1])
data = pd.read_csv('kano_dry.csv', usecols = [0,3,10,19], parse_dates=[0])
data1 = pd.read_csv('calabar_dry.csv', usecols = [0,3,10,19], parse_dates=[0])
data2 = pd.read_csv('maiduguri_dry.csv', usecols = [0,3,10,19], parse_dates=[0])


#Define what each data column is 
data.columns = ['date','PM25','PM10','RH']
data1.columns = ['date','PM25','PM10','RH']
data2.columns = ['date','PM25','PM10','RH']
print(data.columns)

#Calculate PM2.5/PM10 ratio

#for i, a in enumerate (data.columns):
    
#    ratio = data.PM25 / data.PM10


fig, ax = plt.subplots(figsize=(13,13))


#Calculate the rolling mean
#df = pd.DataFrame(data = ratio)
df = pd.DataFrame(data = data.PM25)
df1 = pd.DataFrame(data = data1.PM25)
df2 = pd.DataFrame(data = data2.PM25)

rolling_windows = df.rolling(7, min_periods = 0)
rolling_mean = rolling_windows.mean()


df2 = pd.DataFrame(data = data.RH)
rolling_windows2 = df2.rolling(7, min_periods = 0)
rolling_mean2 = rolling_windows2.mean()
        

#Plot the rolling mean and ratio values
#ax.plot(data.date, rolling_mean, marker = 'o',color = 'red')
#\
plt.plot(data.date, data.PM25,'o',color = 'red',markersize=10)
plt.plot(data.date, data1.PM25,'s',color = 'green',markersize=10)
#plt.plot(data.date, data.PM25, marker = 'o',color = 'red',markersize=10)
#ax.plot(data.date, data1.PM25, marker = 's',color = 'green',markersize=10)
#ax.plot(data.date, data1.PM25, marker = 's',color = 'green',markersize=10)
plt.plot(data2.date, data2.PM25,'s',color = 'blue',markersize=10)
#ax.plot(data2.date, data2.PM25, marker = 'D',color = 'blue',markersize=10)

#ax2 = ax.twinx()
#ax2.plot(data.date, rolling_mean2, color = 'steelblue', lw = 4)



#Set x axis label params
ax.xaxis.set_tick_params(rotation=-45, labelsize=25)
ax.yaxis.set_tick_params(labelsize=25)


#Set x and y axis labels
ax.set_xlabel('Months', size = 29)

ax.set_ylabel('$\mu$g-m$^-3$', size = 29)
#ax2.yaxis.set_tick_params(labelsize = 25)


rpatch = mpatches.Patch(color = 'red', label = 'Kano')
gpatch = mpatches.Patch(color = 'green', label = 'Calabar')
bpatch = mpatches.Patch(color = 'blue', label = 'Maiduguri')

#Plot legend, title, and grid
plt.legend(handles=[rpatch,gpatch,bpatch], fontsize = 25)


plt.title('Nigeria Dry Season daily $PM_{2.5}$ 2021-2022', size = 33)


plt.savefig('dryseason_nigeriaPM.pdf')
plt.show()
