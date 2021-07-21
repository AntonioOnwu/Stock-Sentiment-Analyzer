import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Blacklist import blacklist

df = pd.read_csv('/Users/antonioonwu/stonkstop/src/Backend/StockData.csv')

# common words that will be ignored from Nasdaq search

ticker = list(df['Symbol'].values)  #list of tickers
tickers = [elem for elem in ticker if elem not in blacklist] #removing tickers in blacklist





# print(tickers)