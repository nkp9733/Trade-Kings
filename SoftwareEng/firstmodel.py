import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import numpy

#Get input data
numpy.random.seed(7)
dataset=numpy.loadtxt("aapl_4yr.csv",delimiter=",")
dataset2=numpy.loadtxt("aapl_1yr.csv")
#

model = Sequential()
model.add(Dense(12,input_dim=5,init='uniform',activation='relu'))
model.add(Dense(5,init='uniform',activation='relu'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(inputX,inputY,epochs=150,batch_size=10,verbose=2)

scores =model.evaluate(inputX,outputY)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
