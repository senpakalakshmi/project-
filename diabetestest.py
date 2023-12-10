from numpy import loadtxt

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

dataset= loadtxt('pims-indians-diabetes.xlsx', delimiter=',')
x=dataset[:,0:8]
y=dataset[:,8]
print("Input:",x)
print("Output:",y)


