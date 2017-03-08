#import pandas as pd
import numpy as np
#df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv")
#df.head
#array1 = np.array([[24.68,164.93,114.73,26.27,19.21,28.87,63.44]])
#array2 = np.array([[24.18,164.89,114.75,26.22,19.07]])
#array3 = np.array([[23.99,164.63,115.04,25.78,19.01,27.04]])
a=np.array([[1,2]])
b=np.array([[5,6]])
#np.concatenate((array1,array2),axis=0)
c=np.concatenate((a,b),axis=0)
print(c)

d=np.arange(3)
e=np.arange(4)
f=np.concatenate((d,e))
print(f.shape)