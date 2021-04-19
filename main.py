#!/usr/bin/env python3

import os
import sys
import requests
import json
from pprint import pprint
from quick_sort import quick_sort_func #allows us to call the quick_sort python code


URL = "https://raw.githubusercontent.com/varora24/Find-My-Game/data/games.json"

def main():

    response = requests.get(URL).json() # accepts response from json file on github which contains information about all games
    
    pprint(response)
    
    quick_sort_func(response, 0, len(response) - 1, 'Maxplayers',False)

    pprint(response)

if __name__ == '__main__':
	main()
