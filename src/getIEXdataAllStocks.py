#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 23:00:21 2019

@author: nileshmune
This code scraps the narket cap value from the Zacks website, for a given list of stocks.
"""

# DataFrame proessing
import pandas as pd
import requests

# Get daily chart details every minute trading : https://api.iextrading.com/1.0/stock/aapl/chart/1d
# Get company details: industry, ceo: https://api.iextrading.com/1.0/stock/aapl/company
# Earnings: https://api.iextrading.com/1.0/stock/aapl/earnings
# Dividends: https://api.iextrading.com/1.0//stock/aapl/dividends/6m
# Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.
# https://api.iextrading.com/1.0//stock/aapl/financials
# IPO Calendar: https://api.iextrading.com/1.0/stock/market/upcoming-ipos
# Important Key Stats containing all I need: https://api.iextrading.com/1.0//stock/aapl/stats

def processSymbol( sym ):
    request = requests.get("https://api.iextrading.com/1.0//stock/" + sym + "/stats")
    if ( request.ok ):
        print(sym, " : Ok")
        
        jsonRec = request.json()

        marketcap=jsonRec['marketcap']
        """        latestEPS=jsonRec['latestEPS']
        returnOnEquity=jsonRec['returnOnEquity']
        revenue=jsonRec['revenue']
        grossProfit=jsonRec['grossProfit']
        cash=jsonRec['cash']
        debt=jsonRec['debt']
        ttmEPS=jsonRec['ttmEPS']
        revenuePerShare=jsonRec['revenuePerShare']
        peRatioHigh=jsonRec['peRatioHigh']
        peRatioLow=jsonRec['peRatioLow']
        returnOnAssets=jsonRec['returnOnAssets']
        returnOnCapital=jsonRec['returnOnCapital']
        profitMargin=jsonRec['profitMargin']
        priceToSales=jsonRec['priceToSales']
        """             
        
        fLine=sym+","+str(marketcap)+"\n"
        #print(fLine)
        fCSV.write(fLine)
        
    else:
        print(sym, ": Failed.")
    

######################################################################
### M A I N

symbols = pd.read_csv("../data/combined.csv")
print(symbols) 

#request = requests.get()
fCSV = open("../data/allMktCap.csv","w")
fCSV.write("Symbol,marketcap\n")
symbols['Symbol'].apply(lambda x: processSymbol(x) )
fCSV.close()

