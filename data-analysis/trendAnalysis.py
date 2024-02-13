# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:31:37 2024

@author: sriva
"""
from pytrends.request import TrendReq
#installed pytrends matplotlib
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
from scipy.signal import find_peaks

###Function that smooths the plot using a moving average filter.
def smooth_plot(x, y, window_size=3):
    smooth_y = np.convolve(y, np.ones(window_size)/window_size, mode='valid')
    smooth_x = x[:len(smooth_y)]
    return smooth_x, smooth_y

###Function that detects the periodicitity and calls smooth_plot()
def yearly_peaks(x, y, threshold=0.8):
    peaks_per_year = []
    smooth_x, smooth_y = smooth_plot(x, y)
    #print(smooth_x[len(smooth_x)-1]) final value of smooth_x
    for year_start in range(0, len(smooth_x), 12):
        year_data = smooth_y[year_start:year_start+12]
        peaks, _ = find_peaks(year_data, height=threshold*np.max(year_data))
        if len(peaks) == 1:
            peaks_per_year.append(True)
        else:
            peaks_per_year.append(False)
    countperi = 0;
    for peri in peaks_per_year:
            if peri:
                countperi += 1      
    if countperi >=17:
        print("This item is seasonal❄️")
        return True
    else:
        print("This item is not seasonal")
        return False

###Function that detects increasing trend graphs
def increasing(x,y):
    average_per_year = []
    index = 0
    #finding index of first date over 20 in search interest
    for i in range(len(y)):
        if y[i] > 20:
            index = i
            break
    for year_start in range(index, len(x), 12):
        year_data = y[year_start:year_start+12]
        total = sum(year_data)
        average = total/len(year_data)
        average_per_year.append(average)
    count_increase = 0
    for i in range(len(average_per_year)-1):
        if average_per_year[i]<average_per_year[i+1]:
            count_increase += 1
    if count_increase> (len(average_per_year)-index/12)*.8:
        print (f"This item is increasing in trend ↑")
        return True
    # add \n count: {count_increase} index: {index}   in print statement to test
    print (f"This item is not increasing in trend")
    return False

#taking user input for the search term
user_input = input("Enter the search term: ")

#using pytrends library to fetch Google Trends data
pytrends = TrendReq(hl='en-US', tz=360);
pytrends.build_payload([user_input], timeframe='all')
trends_data = pytrends.interest_over_time()

# Save x (time) and y (interest) values into int arrays
interest_values = trends_data[user_input].values.astype(int)
year_values = np.linspace(2004,2024, interest_values.shape[0])


#plotting the graph with pandas dataframe
#plt.plot(trends_data.index, trends_data[user_input])
#plt.title(f'Pandas dataframe: Google Search Trends for "{user_input}"')
#plt.xlabel('Date')
#plt.ylabel('Search Interest')
#plt.ylim(0, 100)
#plt.show()

#plotting the graph with int x and y arrays
plt.plot(year_values, interest_values)
plt.title(f'Arrays: Google Search Trends for "{user_input}"')
plt.xlabel('Date')
plt.ylabel('Search Interest')
plt.ylim(0, 100)
# Set the x-axis limits to 2004 and 2024
# plt.xlim(2004, 2024)
# Sets x-axis tick locations to every 2 years
plt.xticks(np.arange(2004, year_values[-1]+1, step=4))
plt.show()

#Final check
yearly_peaks(year_values, interest_values)
increasing(year_values, interest_values)