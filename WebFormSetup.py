# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:09:27 2019

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


from flask import Flask,render_template,request
myapp = Flask(__name__)

myapp.vars={}

@myapp.route('/index_lulu',methods=['GET','POST'])
def index_lulu():
    if request.method == 'GET':
        return render_template('userinfo_lulu_CM.html')
    else:
        #request was a POST
        myapp.vars['ticker'] = request.form['ticker']

        f = open('%s_%s.txt'%(myapp.vars['ticker']),'w')
        f.write('Ticker: %s\n'%(myapp.vars['ticker']))
        f.close()

        return render_template('layout_lulu_CM.html')

if __name__ == "__main__":
    myapp.run(debug=True) 
    

   


