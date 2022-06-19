from asyncio import Handle
from flask import Flask, request, jsonify
import socketserver
import os
import pandas as pd
import numpy as np
import csv


with open("fingerdata/Allen/Allen_S.csv", "w") as file:
    writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames = ["Thumb", "Index", "Middle", "Ring", "Pinky", "AccelX", "AccelY", "AccelZ", "GyroX", "GyroY", "GyroZ", "Letter"], lineterminator = '\n')
    writer.writeheader()


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = request.get_data()
        data = data.decode('utf-8')
        data = data.split(", ")
        data.append("S")
        file = open("fingerdata/Allen/Allen_S.csv", "a", newline='')
        writer = csv.writer(file)
        writer.writerow(data)
        print(data)
        return "Success"    
app.run(host='0.0.0.0', port=5000)