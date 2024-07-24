import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
  
stock_prices = pd.read_csv('chop.csv')
 
plt.figure()
  

up = stock_prices[stock_prices.Close >= stock_prices.Open]
  
down = stock_prices[stock_prices.Close < stock_prices.Open]
  
col1 = 'green'
  

col2 = 'red'
  
width = 1.5
width2 = .15

plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)

plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)
  

plt.xticks(rotation=30, ha='right')
  

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Cisco Systems")
plt.show()