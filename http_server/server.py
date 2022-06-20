from asyncio import Handle
from asyncore import write
from flask import Flask, current_app, request, jsonify
import socketserver
import os
import pandas as pd
import numpy as np
import csv

current_letter = input("Enter the letter: ")

with open("fingerdata/Allen/Allen_" + current_letter + ".csv", "w") as file:
    writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames = ["Thumb", "Index", "Middle", "Ring", "Pinky", "AccelX", "AccelY", "AccelZ", "GyroX", "GyroY", "GyroZ", "Letter"], lineterminator = '\n')
    writer.writeheader()


def write_data(data):
    with open("fingerdata/Allen/Allen_" + current_letter + ".csv", "a", newline='') as file:
        writer = csv.writer(file)
        for character in current_letter:
            current_letters = ord(character) - 96;
        data.append(current_letters)
        writer.writerow(data)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = request.get_data()
        data = data.decode('utf-8')
        data = data.split(", ")
        write_data(data)
        print(data)
        return "Success"
app.run(host='0.0.0.0', port=5000)
