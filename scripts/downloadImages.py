from tensorflow import one_hot
from PIL import Image 
from io import BytesIO
import numpy as np
import requests
import cv2
import pickle
#There is absolutely a better way to do this- but whatever, this works for now.
#The categories you add in here will be the categories that will be included in your numpy dataset, 
#that will eventually become a .pickle file to use for training the model.


def download(cleanData,categoryDataLoc):


#This is the file that I had that included 22 classes in it (about 20000 instances)

  CleanData = np.load(cleanData, allow_pickle=True)
  # categoryDataLoc= np.load(categoryDataLoc)
  categoryDataLoc=np.genfromtxt(categoryDataLoc,dtype=str,delimiter=',')
  print(categoryDataLoc)
  print(CleanData)
  input()
  input("WAIT DO NOT GO FORWARD")
  CategoryData = [x[0] for x in categoryDataLoc]
  print(CategoryData)
  
# category input file should look something like this
# categories = ['CHAMAENERION ANGUSTIFOLIUM','ERYTHRONIUM GRANDIFLORUM',..]
  categories = CategoryData
  input("WAIT DO NOT GO FORWARD")
  #kind of noob mode/ there may be a better way to store all arrays of pixels and labels. But at the 
  # moment a 2d list will do. 
  training_data=[]
  counter=0

  for row in CleanData:
    if(row[-1]in categories):
      try:
        class_num = categories.index(row[-1])
        one_hot_categories = one_hot(class_num,depth=len(categories))
        #lots of requests to inaturalist- this may take a while.
        try:
          r = requests.get(row[0])
        ##instead of downloading image, we write it into an array directly- less total space used and size of data is homogonous
          img_array = np.array(Image.open(BytesIO(r.content)))
          new_array=cv2.resize(img_array,(227,227))
          training_data.append([new_array,one_hot_categories])
        except Exception as e:
          print(e)
        counter+=1
        if(counter%20 == 0):
          print(categories[class_num],counter)
      except Exception as e:
        print(e)
        pass
    else:
      pass

  #example of instance: [[3d img array, encoded label]]
  
  print(training_data)
  input()
  #this will export your prepared/encoded data
  np.save(f'data\\prepared\\preparedData',training_data)



