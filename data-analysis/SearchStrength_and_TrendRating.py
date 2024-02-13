# -*- coding: utf-8 -*-
"""
This program returns the search strength and trend rating from 1-5

Created on Tue Feb 13 13:10:47 2024

@author: sriva
"""
from pytrends.request import TrendReq
import numpy as np

def search_strength(interest_values):
    return interest_values[len(interest_values)-1]

def trend_rating(final_search_interest):
    if(final_search_interest>80):
        return 5
    if(final_search_interest>60):
        return 4
    if(final_search_interest>40):
        return 3
    if(final_search_interest>20):
        return 2
    return 1
    
#taking user input for the search term
user_input = input("Enter the search term: ")

#using pytrends library to fetch Google Trends data
pytrends = TrendReq(hl='en-US', tz=360);
pytrends.build_payload([user_input], timeframe='all')
trends_data = pytrends.interest_over_time()

# Save x (time) and y (interest) values into int arrays
interest_values = trends_data[user_input].values.astype(int)
year_values = np.linspace(2004,2024, interest_values.shape[0])


print("Search strength: ")
strength = search_strength(interest_values)
print(strength)
print("Trend rating: ")
print(trend_rating(strength))


