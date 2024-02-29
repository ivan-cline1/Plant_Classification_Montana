
import pickle
import random
import numpy as np
#'data\\clean10.npy'
# data_loc= input('data file name')
# self.trainingData = np.load(f'data\\prepared\\{data_loc}',allow_pickle=True)


# X=[]
# Y=[]
# random.shuffle(self.trainingData)
# for features,label in self.trainingData:
#   if(features.shape!=(227,227,3)):
#     pass
#   else:
#     X.append(features)
#     Y.append(label)



# try:
#   X=np.array(X).reshape(-1,227,227,3)
#   X=X/255.0
#   Y=np.array(Y)

# except Exception as e:
#   print(e)

# featureNames= input('name your feature file output')
# input_features = featureNames + '.pickle'
# pickle.dump(X, open(input_features, 'wb'))

# labelNames= input('name your feature file output')
# labels = labelNames + '.pickle'
# pickle.dump(Y, open(labels, 'wb'))

class DataPreprocessor:
  def __init__(self,trainingData):
    self.trainingData = trainingData 
  def load_data(self):
      print(self.trainingData)
      input()
      X = []
      Y = []
      random.shuffle(self.trainingData)
      for features, label in self.trainingData:
          if features.shape == (227, 227, 3):
              X.append(features)
              Y.append(label)
      try:
          X = np.array(X).reshape(-1, 227, 227, 3)
          X = X / 255.0
          Y = np.array(Y)
      except Exception as e:
          print(e)
      return X, Y
  def save_features_and_labels(self, X, Y):
      input_features = f'X.pickle'
      pickle.dump(X, open(input_features, 'wb'))
      labels = f'Y.pickle'
      pickle.dump(Y, open(labels, 'wb'))


# preprocessor = DataPreprocessor()
# X_data, Y_data = preprocessor.load_data()
# preprocessor.save_features_and_labels(X_data, Y_data)
