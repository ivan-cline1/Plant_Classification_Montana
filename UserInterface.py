import sys
import os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

import downloadImages
import imageClean
import CreateAndTrainModel
import loadToDataset

# import CreateAndTrainModel
# import loadToDataset

class UI:
    def __init__(self):
        self.cleanDataLocation = None
        self.rawDataLocation = "data\\raw\\testRaw.csv"
        self.amountOfClasses=0
        pass

    def mainUIStart(self):
        flag = True
        while(flag):
            # try:
                firstMenuChoice = int(input('\n\nHello!\n1.) Clean raw CSV file containing images\n2.) Download and encode images, store them\n3.) Train Model\n4.) Use Model to look at user input photos, or photos in repo\n5.) Show current model, classes it is trained on, and accuracy\n6.) Quit\n\n\n'))
                
                if firstMenuChoice == 1:
                    self.amountOfClasses=int(input("How many classes would you like in your dataset?"))
                    imageClean.cleanImages(self.rawDataLocation,self.amountOfClasses,f'data\\interim')
                    
                    pass
                elif firstMenuChoice == 2:
                    downloadImages.download(f'data\\interim\\cleanData_{self.amountOfClasses}.npy',f'data\\interim\\{self.amountOfClasses}Classes.txt')
                    preprocessor = loadToDataset.DataPreprocessor(np.load(f'data\\prepared\\preparedData.npy'))
                    X_data, Y_data = preprocessor.load_data()
                    preprocessor.save_features_and_labels(X_data, Y_data)
 
                elif firstMenuChoice == 3:
                    CreateAndTrainModel.Model(f'data\\prepared\\preparedData.npy')
                    pass
                elif firstMenuChoice == 4:
                    difficulty=3
                    pass
                elif firstMenuChoice == 5:
                    difficulty=4
                    pass
                elif firstMenuChoice == 6:
                    difficulty=0
                    pass
                else:
                    print('enter a number between 1 and 5')
                    pass



            # except:
            #     pass


ui = UI()
ui.mainUIStart()
