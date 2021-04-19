#!/usr/bin/env python3

import os
import sys
import requests
import json
import pprint
from quick_sort import quick_sort_func

URL = "https://raw.githubusercontent.com/varora24/Find-My-Game/data/games.json"

def main() :
    
    response = requests.get(URL).json()

    response_sorted = quick_sort_func(response, 0, len(response) - 1, 'Maxplayers', False)

    pprint.pprint(response_sorted)

if __name__ == '__main__' :
    main()
