# import importModel
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv1D, Conv2D, MaxPooling2D,ZeroPadding2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import Input
import os


class Model:

    def __init__(self,X_Train,Y_Train,X_Test,Y_Test):
        self.X_Train = X_Train
        self.Y_Train = Y_Train
        self.X_Test = X_Test
        self.Y_Test = Y_Test
        self.model = CreateModel()
        self.checkPointPath=os.path.dirname("models\\checkpoints")
    def CreateModel(self):
    #Model create
        X_Train = self.X_Train
        model = Sequential()
        model.add(Input(shape=X_Train.shape[1:]))
        model.add(Conv2D(96,(11,11),padding='valid',strides=4,activation='relu'))
        model.add(MaxPooling2D(pool_size=(3,3),strides=2))
        model.add(Conv2D(256,(5,5),strides=1,activation='relu'))
        model.add(ZeroPadding2D(2))
        model.add(MaxPooling2D(pool_size=(3,3),strides=2))
        model.add(Conv2D(384,(3,3),strides=1,activation='relu'))
        model.add(ZeroPadding2D(1))
        model.add(Conv2D(384,(3,3),strides=1,activation='relu'))
        model.add(ZeroPadding2D(1))
        model.add(Conv2D(256,(3,3),strides=1,activation='relu'))
        model.add(ZeroPadding2D(1))
        model.add(MaxPooling2D(pool_size=(3,3),strides=2))
        model.add(Dropout(.5))
        model.add(Flatten())

        model.add(Dense(4096,activation='relu',kernel_initializer='he_uniform'))
        model.add(Dropout(.5))
        model.add(Dense(4096,activation='relu',kernel_initializer='he_uniform'))
        model.add(Dense(10,activation='softmax',kernel_initializer='he_uniform'))
        #opt=Adam(learning_rate=learningRate)
        model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
        model.summary()
        return model

    def TrainModel(self,model,X_Train,Y_Train,X_Test,Y_Test):

        checkpoint = ModelCheckpoint(filepath=self.checkPointPath,
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 save_freq = 1)
        epochs=25
        batchSize=64
        hist = self.model.fit(self.X_Train,self.Y_Train,epochs=epochs,batch_size=batchSize,verbose=1, callbacks=[checkpoint])
        loss,accuracy=self.model.evaluate(self.X_Test,self.Y_Test,verbose=1)
        print(f"loss: {loss}")
        print(f"accuracy: {accuracy}")
        #save model after the 5 epochs
        model.save(os.path.dirname("models"))