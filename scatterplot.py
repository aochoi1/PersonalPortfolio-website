import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polygit
stock = pd.read_csv('chop')
x = stock.Close
y = stock.Volume 
plt.scatter(x,y)
plt.ylabel('Volume (in hundred of millions)')
plt.xlabel('Stock Price (Close)')
plt.legend('Volume')
plt.title('Cisco Systems Stock Prices Scatter Plot')
plt.plot(np.unique(x), np.ploy1d(x, y, 1))(np.unique(x))
plt.show()
