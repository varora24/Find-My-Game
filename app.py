#!/usr/bin/env python

import requests
import json 
from flask import Flask, render_template, request

app = Flask(__name__)

URL = "https://raw.githubusercontent.com/varora24/Find-My-Game/main/games.json"

response = requests.get(URL)
data = response.json()

#data = [
#{"Title":"Codenames","Minplayers":2,"Maxplayers":8,"Category":"Strategy","Description":"red and blue teams compete over who will guess all their words first","Time":30,"Price":0,"Format":"Website","URL":"https://codenames.game/","Picture":"https://cf.geekdo-images.com/F_KDEu0GjdClml8N7c8Imw__itemrep/img/e8zw8YQvQB8q8zfWkHQ48Ls920g=/fit-in/246x300/filters:strip_icc()/pic2582929.jpg"},
#{"Title":"Skribble.io","Minplayers":2,"Maxplayers":12,"Category":"Drawing","Description":"skribbl.io is a free multiplayer drawing and guessing game.","Time":10,"Price":0,"Format":"Website","URL":"https://skribbl.io/","Picture":"https://athletesforkids.org/wp-content/uploads/2020/04/Skribble-image2.png"},
#]

dataout = []

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET': # GET request is sent when html wants some information from the python script
        return render_template('index.html')
    
    if request.method == 'POST': # POST request is sent when the html is sending sdata to the python code for processing
        numplayers=request.form.get('numplayers')
        genre = request.form.get('genre')
        mode = request.form.get('mode')

        findmatches(numplayers,genre,mode)
        
        print(dataout)

    return render_template("index.html")

def findmatches(numplayers,genre,mode):
    if not numplayers:
        numplayers = "1"

    numplayers = int(numplayers.strip())
    genrematch = False
    modematch = False
    for game in data:
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

