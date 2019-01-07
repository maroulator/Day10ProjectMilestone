# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 23:09:29 2019

@author: chris
"""

import pandas as pd
from pandas_datareader import data as pdr

ticker=['MSFT','AMZN','AAPL','GOOG','NFLX','TSLA','FB','DRI','DIN','DAL','DENN','TXRH',
        'CNK','APPB','WMT','RRGB','CBRL','AABA','VZ','DELL','VMW','TWTR']

start_date = '2015-01-01'
end_date = '2018-01-31'

data=pd.DataFrame()

for x in ticker:
    panel_data = pdr.DataReader(x, 'yahoo', start_date, end_date)
    panel_data['ticker']=x
    data = data.append(panel_data)