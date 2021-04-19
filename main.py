#!/usr/bin/env python3

import os
import sys
import requests
import json
from pprint import pprint
from quick_sort import quick_sort_func #allows us to call the quick_sort python code

file_name = "games.json"
#URL = "https://raw.githubusercontent.com/varora24/Find-My-Game/data/games.json"

def main():

    response = open(file_name,) #requests.get(URL).json() # accepts response from json file on github which contains information about all games
    data = json.load(response);
    
    data = quick_sort_func(data, 0, len(data) - 1, 'Minplayers')

    pprint(data)

if __name__ == '__main__':
	main()

