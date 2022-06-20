import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from keras.losses import losses_utils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.preprocessing import StandardScaler
import pandas as pd
from imblearn.over_sampling import RandomOverSampler as ros
import os

df = pd.read_csv("../http_server/fingerdata/Allen/AllenMasterFile.csv")
df.head()
x = df[df.columns[:-1]].values
y = df[df.columns[-1]].values
X_train, X_temp, y_train, y_temp = train_test_split(x,y, test_size=0.4, random_state=0)
X_valid, X_temp, y_valid, y_temp = train_test_split(x,y, test_size=0.5, random_state=0)
model = tf.keras.Sequential([
                             tf.keras.layers.Dense(1024, activation = "relu"),
                             tf.keras.layers.Dense(1024, activation = "relu"),
                             tf.keras.layers.Dense(1024, activation = "sigmoid")
])
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.0001),
              loss = tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.evaluate(X_train, y_train)
model.evaluate(X_valid, y_valid)
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

model.fit(X_train, y_train, batch_size=16, epochs=100, validation_data=(X_valid, y_valid), callbacks=[cp_callback])