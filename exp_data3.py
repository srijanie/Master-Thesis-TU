import pandas
import matplotlib.pyplot as plt
import math
import numpy
from keras.models import Sequential,Model
from keras.layers import Dense
from keras.layers import LSTM, Input


#numpy.random.seed(7)
#dataframe = pandas.read_csv('pima-indians-diabetes.csv', usecols=[1,2], engine='python')
#dataset = dataframe.values
#dataset = dataset.astype('float32')
#print(dataset)
#plt.plot(dataset)
#plt.show()
#train_size = int(len(dataset) * 0.59)
#test_size = len(dataset) - train_size
#train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
#print(len(train), len(test))

#dataframe = pandas.read_csv('rain1.csv', usecols=[2], engine='python')
#dataset = dataframe.values
#dataset = dataset.astype('float32')
#print(dataset)
#plt.plot(dataset)
#plt.show()
#train_size = int(len(dataset) * 0.59)
#test_size = len(dataset) - train_size
#train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]


#def create_dataset(dataset, look_back=1):
#	dataX, dataY = [], []
#	for i in range(len(dataset)-look_back-1):
#		a = dataset[i:(i+look_back), 0]
#		dataX.append(a)
#		dataY.append(dataset[i + look_back, 0])
#	return numpy.array(dataX), numpy.array(dataY)



# reshape into X=t and Y=t+1
#look_back = 1
#trainX, trainY = create_dataset(train, look_back)
#testX, testY = create_dataset(test, look_back)
encoding_dim = 32
input_img = Input(shape=(84,1))

encoded = Dense(2592, activation='relu')(input_img)
encoded1 = Dense(encoding_dim, activation='relu')(encoded)

encoder = Model(input_img,encoded1)
numpy.savetxt("encoded1.csv",encoder.predict(trainX),delimiter=",")

