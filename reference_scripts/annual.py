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


data = pd.read_csv('kano1.csv', usecols = [0,3,10,19], parse_dates=[0])
data1 = pd.read_csv('calabar.csv', usecols = [0,3,10,19], parse_dates=[0])
data2 = pd.read_csv('maiduguri.csv', usecols = [0,3,10,19], parse_dates=[0])


#Define what each data column is 
data.columns = ['date','PM25','PM10','RH']
data1.columns = ['date','PM25','PM10','RH']
data2.columns = ['date','PM25','PM10','RH']

#Reading in data
#data = pd.read_csv('sao_filipe.csv', usecols = [3,8,12,20], parse_dates=[0])
#data1 = pd.read_csv('mindelo.csv', usecols = [3,8,12,20], parse_dates=[0])
#data = pd.read_csv('sao_filipe.csv', usecols = [0,3,9,19], parse_dates=[0])
#data1 = pd.read_csv('mindelo.csv', usecols = [0,3,9,19], parse_dates=[0])


#Define what each data column is 
#data.columns = ['date','PM25','PM10','RH']
#data1.columns = ['date','PM25','PM10','RH']
#data2.columns = ['date','PM25','PM10','RH']


#Define what each data column is 




fig, ax = plt.subplots(figsize=(13,13))



df = pd.DataFrame(data = data.PM25)
#df1 = pd.DataFrame(data = data1.PM25)

rolling_windows = df.rolling(7, min_periods = 0)
rolling_mean = rolling_windows.mean()

df1 = pd.DataFrame(data = data1.PM25)
rolling_windows1 = df1.rolling(7, min_periods = 0)
rolling_mean1 = rolling_windows1.mean()

df2 = pd.DataFrame(data = data2.PM25)
rolling_windows2 = df2.rolling(7, min_periods = 0)
rolling_mean2 = rolling_windows2.mean()
        

plt.plot(data.date,rolling_mean,linestyle = '-',linewidth=4,color = 'red',markersize=10)
plt.plot(data1.date, rolling_mean1,linestyle = '-',linewidth=5,color = 'green',markersize=10)
plt.plot(data2.date, rolling_mean2,linestyle = '-',linewidth =4,color = 'blue',markersize=10)

#plt.plot(data2.date, data2.PM25,'s',color = 'blue',markersize=10)
  


#Set x axis label params
ax.xaxis.set_tick_params(rotation=-45, labelsize=25)
ax.yaxis.set_tick_params(labelsize=25)

plt.axhline(y = 15, color = 'red', linewidth = 4, linestyle = '--') 
#Set x and y axis labels
ax.set_xlabel('Months', size = 29)

ax.set_ylabel('$\mu$g-m$^-3$', size = 29)



rpatch = mpatches.Patch(color = 'red', label = 'Kano')
gpatch = mpatches.Patch(color = 'green', label = 'Calabar')
bpatch = mpatches.Patch(color = 'blue', label = 'Maiduguri')

#Plot legend, title, and grid
#plt.legend(handles=[rpatch,gpatch,bpatch], fontsize = 25)
plt.legend(handles=[rpatch,gpatch,bpatch], fontsize = 25)

plt.title('Nigeria daily $PM_{2.5}$ 2021-2022', size = 33)


plt.savefig('nigeria_pm2.5.pdf',dpi=300)
plt.show()
