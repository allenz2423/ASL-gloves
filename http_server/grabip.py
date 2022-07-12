from flask import Flask, current_app, request, jsonify
import os
import time as t

ipAddresses = []



app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if(request.method == "POST"):
        data = request.get_data()
        data = data.decode('utf-8')
        if data == "TAKE MY IP": 
            if request.remote_addr in ipAddresses:
                print("Already in array", ipAddresses)
                print(len(ipAddresses))
                return "Already in array"
            else :
                ipAddresses.append(request.remote_addr)
                print("Not in array")
                return "Not in array"
    elif request.method == "GET":
        if len(ipAddresses) == 3:
            return ipAddresses
        else:
            return "Not enough IP addresses. Sorry later"
    if len(ipAddresses > 0) and len(ipAddresses < 3):
        t.sleep(5)
        ipAddresses.clear()
        print("Took too long, clearned the list.")
app.run(host='0.0.0.0', port=730)