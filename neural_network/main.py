import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.preprocessing import StandardScaler
import pandas as pd
from imblearn.over_sampling import RandomOverSampler as ros
import os

df = pd.read_csv("../http_server/fingerdata/Allen/AllenMasterFile.csv")
df.head() # I don't understand how pandas works.
x = df[df.columns[:-1]].values # gets every column except for the last column, because that's the correct outcome
y = df[df.columns[-1]].values # gets the correct outcome, which is the last column.
X_train, X_temp, y_train, y_temp = train_test_split(x,y, test_size=0.4, random_state=0) # splits 40% of the dataset into training material
X_valid, X_temp, y_valid, y_temp = train_test_split(x,y, test_size=0.5, random_state=0) # takes 50$ of the dataset as never seen before data
model = tf.keras.Sequential([ # Defines the model
                             tf.keras.layers.Dense(16, activation = "relu"), # 2 different nodes of densely connected relu (rectifier linear unit)
                             tf.keras.layers.Dense(16, activation = "relu"), # same thing as above 16
                             tf.keras.layers.Dense(3, activation = "sigmoid") # A sigmoid 
])
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.0001), # Learning rate is low to reduce loss
              loss = tf.keras.losses.SparseCategoricalCrossentropy(), # No idea what the loss function does.
              metrics=[keras.metrics.SparseCategoricalAccuracy()]) # This calculates the accuracy
model.evaluate(X_train, y_train) # Checks the accuracy
model.evaluate(X_valid, y_valid) # checks accuracy with new data
checkpoint_path = "../model/cp.ckpt" # sets the path for where to save the model
checkpoint_dir = os.path.dirname(checkpoint_path) # does funny change directory
model.fit(X_train, y_train, batch_size=8, epochs=27, validation_data=(X_valid, y_valid)) # Epoch 27 is the most accurate with the least loss.
model.save("initial_model.h5") # saves the model
model.save_weights("initial_model_weight.h5") # saves the model weight