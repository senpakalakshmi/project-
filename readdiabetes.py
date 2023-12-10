from numpy import loadtxt

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

dataset= loadtxt('pims-indians-diabetes.csv', delimiter=',')
x=dataset[:,0:8]
y=dataset[:,8]

model_json=model.to_json()
loaded_model_json=json_file.read()
json_file.close()
model=model_from_json(loaded_model_json)
model.load_weights("model.h5")
print("loaded model from disk")

predictions=model.predict(x)
for i in range(5,10):
    print('%s => %d(expected %d)'%(x[i].tolist().predictions[i],y[i]))
