import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
stock = pd.read_csv('chop.csv')
x  = np.linspace(1990, 1995, 299)
y = stock.Close 
plt.subplot(2,1,1)
plt.plot(x,y)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Cisco Systems")
stock = pd.read_csv('chop.csv')
x = np.linspace(1990,1995,299)
y = (stock.Volume)
plt.subplot(2,1,2)
plt.title("Cisco Systems Stock Prices Bar Plot")
plt.xlabel("Date")
plt.ylabel("Volume (in hundreds of millions)")
plt.bar(x,y,width=0.01)
plt.tight_layout(pad=1.0)
plt.show() 