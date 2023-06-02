
import pickle
import random
import numpy as np
#'data\\clean10.npy'
data_loc= input('data file name')
training_data = np.load(f'data\\prepared\\{data_loc}',allow_pickle=True)


X=[]
Y=[]
random.shuffle(training_data)
for features,label in training_data:
  if(features.shape!=(227,227,3)):
    pass
  else:
    X.append(features)
    Y.append(label)



try:
  X=np.array(X).reshape(-1,227,227,3)
  X=X/255.0
  Y=np.array(Y)

except Exception as e:
  print(e)

featureNames= input('name your feature file output')
input_features = featureNames + '.pickle'
pickle.dump(X, open(input_features, 'wb'))

labelNames= input('name your feature file output')
labels = labelNames + '.pickle'
pickle.dump(Y, open(labels, 'wb'))

