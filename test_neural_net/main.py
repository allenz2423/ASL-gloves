from asyncio import Handle
from asyncore import write
from flask import Flask, current_app, request, jsonify
import tensorflow as tf
import os
import pandas as pd
import numpy as np
import csv

# current_letter = input("Enter the letter: ")

def init_data():
    with open("fingerdata/Allen/Allen_" + current_letter + ".csv", "w") as file:
        writer = csv.writer(file)
        writer = csv.DictWriter(file, fieldnames = ["Thumb", "Index", "Middle", "Ring", "Pinky", "AccelX", "AccelY", "AccelZ", "GyroX", "GyroY", "GyroZ", "Letter"], lineterminator = '\n')
        writer.writeheader()


def write_data(data):
    with open("fingerdata/Allen/Allen_" + current_letter + ".csv", "a", newline='') as file:
        writer = csv.writer(file)
        for character in current_letter:
            current_letters = ord(character);
        data.append(current_letters)
        writer.writerow(data)

# init_data()
model = tf.keras.models.load_model("../neural_network/initial_model.h5")
model.load_weights("../neural_network/initial_model.h5")
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = request.get_data()
        data = data.decode('utf-8')
        data = data.split(", ")
        data = [float(i) for i in data]
        print(data)
        predict = model.predict([data])
        predict = np.argmax(tf.nn.sigmoid(predict[0]))
        if predict == 0:
            predict = "A"
        elif predict == 1:
            predict = "B"
        elif predict == 2:
            predict = "C"
        # write_data(data)
        print(predict + predict + predict + predict + predict)
        return "Success"
app.run(host='0.0.0.0', port=5000)

# THIS IS FOR NEURAL NETWORK