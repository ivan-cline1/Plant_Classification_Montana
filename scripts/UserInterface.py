import downloadImages
import imageClean
# import CreateAndTrainModel
# import loadToDataset

class UI:
    def __init__(self):
        self.cleanDataLocation = None
        self.rawDataLocation = "ALL.csv"
        pass

    def mainUIStart(self):
        flag = True
        while(flag):
            try:
                firstMenuChoice = int(input('\n\nHello!\n1.) Clean raw CSV file containing images\n2.) Download and encode images, store them\n3.) Train Model\n4.) Use Model to look at user input photos, or photos in repo\n5.) Show current model, classes it is trained on, and accuracy\n6.) Quit\n\n\n'))
                
                if firstMenuChoice == 1:
                    amountOfClasses=int(input("How many classes would you like in your dataset?"))
                    imageClean.cleanImages(self.rawDataLocation,amountOfClasses)
                    downloadImages.download()
                    pass
                elif firstMenuChoice == 2:
                    
                    pass
                elif firstMenuChoice == 3:
                    difficulty=2
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



            except:
                pass


ui = UI()
ui.mainUIStart()
