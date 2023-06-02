from tensorflow import one_hot
from PIL import Image 
from io import BytesIO
import numpy as np
import requests
import cv2

#There is absolutely a better way to do this- but whatever, this works for now.
#The categories you add in here will be the categories that will be included in your numpy dataset, 
#that will eventually become a .pickle file to use for training the model.





#This is the file that I had that included 22 classes in it (about 20000 instances)
inputFile = input('type the file name that you are storing your urls in')
CleanData = np.load(f'data\\interim\\{inputFile}', allow_pickle=True)

categoryDataLoc=input('name of file where category data is stored')
CategoryData = np.load(f'data\\interim\\{categoryDataLoc}', allow_pickle=True)
# category input file should look something like this
# categories = ['CHAMAENERION ANGUSTIFOLIUM','ERYTHRONIUM GRANDIFLORUM',..]
categories = CategoryData.tolist()

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
      r = requests.get(row[0])
      ##instead of downloading image, we write it into an array directly- less total space used and size of data is homogonous
      img_array = np.array(Image.open(BytesIO(r.content)))
      new_array=cv2.resize(img_array,(227,227))
      training_data.append([new_array,one_hot_categories])
      counter+=1
      if(counter%20 == 0):
        print(categories[class_num],counter)
    except Exception as e:
      print(e)
      pass
  else:
    pass

#example of instance: [[3d img array, encoded label]]
nameOfFile= input('enter the name of the csv that you would like your data to be stored in')
#this will export your prepared and encoded data
np.save(f'data\\prepared\\{nameOfFile}',training_data)


