from collections import Counter
import numpy as np




##imageURL or CSV Method
##Array of items should look like this -> [[imageURL, category]...]
##imageURL, category


def CleanCSV(fileLocation):
  arrayOfPlants = []
  with open(fileLocation,encoding="utf8") as my_file:
    for line in my_file:
      
      try:
        if(line.split(',')[-1][-1:]==('\n')):
          arrayOfPlants.append(line.split(',')[-1][:-1].upper())
        else:
          arrayOfPlants.append(line.split(',')[-1].upper())
      except Exception as e:        
        print(e)

  my_file.close()
  return arrayOfPlants


def CountInstancesAndWriteToTXT(array,topPlantClassNum,nameOfCleanData):
  x = Counter(array)
  categories =[]
  with open(f'{nameOfCleanData}\\{topPlantClassNum}Classes.txt.', encoding='utf-8', mode='w') as fp: 
    for tag, count in x.most_common(topPlantClassNum):  
      fp.write(f'{tag},{count}\n')
      categories.append(tag)
    fp.close()
    return categories
  

def CreateCSVWithOnlyTopClasses(categories,fileName,nameOfCleanData,amountOfClasses):
  ListOfClassesToTest = []
  nameOfCleanData= nameOfCleanData+"\\cleanData_"+str(amountOfClasses)+".npy"
  with open(fileName,encoding="utf8") as f:
    for line in f:
      if(line.split(",")[-1][-1:]==('\n')):
          x = line.split(',')[-1][:-1].upper()
      else:
          x = line.split(',')[-1].upper()
      
      if(x in categories):
        temp = [line.split(',')[2],x]
       
        ListOfClassesToTest.append(temp)
  f.close()
  np.save(nameOfCleanData,ListOfClassesToTest)
  return ListOfClassesToTest


def cleanImages(fileName,amountOfClasses,cleanDataPath):
  Clean= CleanCSV(fileName)
  categoryArray = CountInstancesAndWriteToTXT(Clean,amountOfClasses,cleanDataPath) #amountOfClasses = 10
  CreateCSVWithOnlyTopClasses(categoryArray,fileName,cleanDataPath,amountOfClasses)




