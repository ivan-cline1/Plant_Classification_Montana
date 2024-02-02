import importModel
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv1D, Conv2D, MaxPooling2D,ZeroPadding2D
from tensorflow.keras.models import Sequential
from tensorflow.keras import Input



def CreateModel(X_Train):
#Model create
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

def TrainModel(model,X_Train,Y_Train,X_Test,Y_Test):
    
    epochs=25
    batchSize=64
    hist = model.fit(X_Train,Y_Train,epochs=epochs,batch_size=batchSize,verbose=1)
    loss,accuracy=model.evaluate(X_Test,Y_Test,verbose=1)
    print(f"loss: {loss}")
    print(f"accuracy: {accuracy}")
    #save model after the 5 epochs
    model.save('10ClassModel.model')


def main():
    X_Train,Y_Train,X_Test,Y_Test = importModel.importDataSet('10ClassLABELS.pickle','10ClassIMAGE.pickle')
    model = CreateModel(X_Train)
    TrainModel(model,X_Train,Y_Train,X_Test,Y_Test)


main()