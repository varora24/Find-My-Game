#!/usr/bin/env python

import requests
import json 
import os
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

URL = "https://raw.githubusercontent.com/varora24/Find-My-Game/main/games.json"

response = requests.get(URL)
data = response.json()

dataout = []

@app.route('/', methods=['POST','GET'])
def index():
    response = requests.get(URL)
    data = response.json()
    data = bubble_sort_func(data, 'Maxplayers')

    if request.method == 'GET': # GET request is sent when html wants some information from the python script
        return render_template('index.html')
    
    if request.method == 'POST': # POST request is sent when the html is sending sdata to the python code for processing
        numplayers=request.form.get('numplayers')
        genre = request.form.get('genre')
        mode = request.form.get('mode')

        findmatches(numplayers, genre, mode)
        
        print(dataout)

    return render_template("index.html")


def findmatches(numplayers, genre, mode):

    if not numplayers:
        numplayers = 1

    numplayers = int(numplayers)

    for game in data:
        genrematch = False
        modematch = False
        if game["Minplayers"]<=numplayers and game["Maxplayers"]>=numplayers:
            if not genre == "all":
                if game["Category"]==genre:
                    print("genre match found")
                    genrematch= True
            else:
                print("genre all")
                genrematch = True

            if not mode == "both":
                if game["Format"]== mode:
                    print("mode match found")
                    modematch = True
            else:
                print("mode all")
                modematch = True

            if modematch == True and genrematch == True:
                dataout.append(games)


def check_valid(data):

    defaults = {'Title': 'No Name', 'Minplayers': 1, 'Maxplayers': 2, 'Category': 'Fun', 'Description': 'No Description', 'Time': 30, 'Price': 0, 'Format': 'Website', 'URL': 'No URL', 'Picture': 'https://i.ibb.co/qxjcPtZ/Untitled-design.png'}

    for attribute in defaults:
        if attribute not in data:
            data[attribute] = defaults[attribute]


def bubble_sort_func(data, index):
    
    length = len(data)

    for i in range(length-1):
        data[i] = check_valid(data[i])
        for j in range(0, length - i - 1):
            if data[j][index] > data[j + 1][index]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


