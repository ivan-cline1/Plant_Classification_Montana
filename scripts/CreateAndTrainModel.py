import os
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, ZeroPadding2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint

class Model:

    def __init__(self, X_Train, Y_Train, X_Test, Y_Test):
        self.X_Train = X_Train
        self.Y_Train = Y_Train
        self.X_Test = X_Test
        self.Y_Test = Y_Test
        self.model = self.create_model()
        self.checkpoint_path = "models/checkpoints"
        
    def create_model(self):
        model = Sequential()
        model.add(Conv2D(96, (11, 11), padding='valid', strides=4, activation='relu', input_shape=self.X_Train.shape[1:]))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2))
        model.add(Conv2D(256, (5, 5), strides=1, activation='relu'))
        model.add(ZeroPadding2D(2))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2))
        model.add(Conv2D(384, (3, 3), strides=1, activation='relu'))
        model.add(ZeroPadding2D(1))
        model.add(Conv2D(384, (3, 3), strides=1, activation='relu'))
        model.add(ZeroPadding2D(1))
        model.add(Conv2D(256, (3, 3), strides=1, activation='relu'))
        model.add(ZeroPadding2D(1))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=2))
        model.add(Dropout(0.5))
        model.add(Flatten())
        model.add(Dense(4096, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dropout(0.5))
        model.add(Dense(4096, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax', kernel_initializer='he_uniform'))
        
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.summary()
        return model

    def train_model(self):
        checkpoint = ModelCheckpoint(filepath=self.checkpoint_path, save_weights_only=True, verbose=1, save_freq=1)
        epochs = 25
        batch_size = 64
        history = self.model.fit(self.X_Train, self.Y_Train, epochs=epochs, batch_size=batch_size, verbose=1, callbacks=[checkpoint])
        loss, accuracy = self.model.evaluate(self.X_Test, self.Y_Test, verbose=1)
        print(f"Loss: {loss}")
        print(f"Accuracy: {accuracy}")
        # Save the entire model
        self.model.save("models")

# Usage example:
# model_instance = Model(X_Train, Y_Train, X_Test, Y_Test)
# model_instance.train_model()